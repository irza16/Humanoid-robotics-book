// RAG Chatbot Widget - Vanilla JavaScript Implementation
// Floating chat widget for the Physical AI & Humanoid Robotics book

(function() {
    'use strict';

    // Configuration
    const CONFIG = {
        backendUrl: (function() {
            // Try to get backend URL from data attribute on script tag, or use default
            const script = document.querySelector('script[src*="chatbot-widget.js"]');
            if (script && script.dataset.backendUrl) {
                return script.dataset.backendUrl;
            }
            // Default to Railway URL, but also check if we're in development
            const isLocalhost = window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1';
            return isLocalhost ? 'http://localhost:8000' : 'https://superb-joy-production-b689.up.railway.app';
        })(),
        maxMessageLength: 2000,
        maxSelectedTextLength: 5000
    };

    // State management
    let state = {
        isOpen: false,
        messages: [],
        selectedText: null,
        selectedTextCache: null  // Persistent cache for selected text
    };

    // DOM elements
    let elements = {};

    // Initialize the widget
    function init() {
        createWidget();
        setupEventListeners();
        loadExistingSelection();
    }

    // Create the chat widget HTML structure
    function createWidget() {
        // Create the floating button
        const floatingButton = document.createElement('div');
        floatingButton.id = 'chatbot-float-button';
        floatingButton.innerHTML = '💬';
        floatingButton.style.cssText = `
            position: fixed;
            bottom: 20px;
            right: 20px;
            width: 60px;
            height: 60px;
            border-radius: 50%;
            background: #4f46e5;
            color: white;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 24px;
            cursor: pointer;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
            z-index: 10000;
            transition: all 0.3s ease;
        `;

        // Create the chat modal
        const chatModal = document.createElement('div');
        chatModal.id = 'chatbot-modal';
        chatModal.style.cssText = `
            position: fixed;
            bottom: 90px;
            right: 20px;
            width: 400px;
            height: 500px;
            background: white;
            border-radius: 12px;
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
            display: none;
            flex-direction: column;
            z-index: 10000;
            overflow: hidden;
        `;

        chatModal.innerHTML = `
            <div id="chatbot-header" style="
                background: #4f46e5;
                color: white;
                padding: 16px;
                display: flex;
                justify-content: space-between;
                align-items: center;
            ">
                <h3 style="margin: 0; font-size: 16px;">Book Tutor</h3>
                <button id="chatbot-close" style="
                    background: none;
                    border: none;
                    color: white;
                    font-size: 20px;
                    cursor: pointer;
                    padding: 0;
                    width: 24px;
                    height: 24px;
                ">&times;</button>
            </div>
            <div id="chatbot-messages" style="
                flex: 1;
                padding: 16px;
                overflow-y: auto;
                background: #f9fafb;
            "></div>
            <div id="chatbot-input-area" style="
                padding: 16px;
                border-top: 1px solid #e5e7eb;
                background: white;
            ">
                <div id="selected-text-indicator" style="
                    margin-bottom: 8px;
                    padding: 8px;
                    background: #dbeafe;
                    border-radius: 6px;
                    font-size: 12px;
                    display: none;
                ">
                    <strong>Selected text:</strong> <span id="selected-text-content"></span>
                </div>
                <div style="display: flex; gap: 8px;">
                    <input type="text" id="chatbot-input" placeholder="Ask about the book content..." style="
                        flex: 1;
                        padding: 12px;
                        border: 1px solid #d1d5db;
                        border-radius: 8px;
                        font-size: 14px;
                    " />
                    <button id="chatbot-send" style="
                        background: #4f46e5;
                        color: white;
                        border: none;
                        border-radius: 8px;
                        padding: 12px 16px;
                        cursor: pointer;
                    ">Send</button>
                </div>
            </div>
        `;

        document.body.appendChild(floatingButton);
        document.body.appendChild(chatModal);

        // Store references to elements
        elements = {
            floatingButton: document.getElementById('chatbot-float-button'),
            modal: document.getElementById('chatbot-modal'),
            closeBtn: document.getElementById('chatbot-close'),
            messages: document.getElementById('chatbot-messages'),
            input: document.getElementById('chatbot-input'),
            sendBtn: document.getElementById('chatbot-send'),
            selectedTextIndicator: document.getElementById('selected-text-indicator'),
            selectedTextContent: document.getElementById('selected-text-content')
        };
    }

    // Set up event listeners
    function setupEventListeners() {
        // Toggle chat modal
        elements.floatingButton.addEventListener('click', function() {
            // Capture current text selection when chat button is clicked
            handleTextSelection();
            toggleChat();
        });
        elements.closeBtn.addEventListener('click', toggleChat);

        // Send message on button click
        elements.sendBtn.addEventListener('click', sendMessage);

        // Send message on Enter key (but allow Shift+Enter for new lines)
        elements.input.addEventListener('keydown', function(e) {
            if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                sendMessage();
            }
        });

        // Detect text selection
        document.addEventListener('mouseup', handleTextSelection);
        document.addEventListener('selectionchange', handleTextSelection);
    }

    // Toggle chat visibility
    function toggleChat() {
        state.isOpen = !state.isOpen;
        elements.modal.style.display = state.isOpen ? 'flex' : 'none';

        if (state.isOpen) {
            elements.input.focus();
        }
    }

    // Handle text selection
    function handleTextSelection() {
        const selection = window.getSelection();
        const selectedText = selection.toString().trim();

        if (selectedText && selectedText.length <= CONFIG.maxSelectedTextLength) {
            state.selectedText = selectedText;
            state.selectedTextCache = selectedText;  // Store in persistent cache
            showSelectedTextIndicator(selectedText);
        } else if (!selectedText && state.selectedTextCache) {
            // Don't clear selectedText if we have cached text (user might be typing)
            // Only clear when explicitly sending a message
            state.selectedText = null;
        }
    }

    // Show selected text indicator
    function showSelectedTextIndicator(text) {
        elements.selectedTextContent.textContent = text.length > 100 ? text.substring(0, 100) + '...' : text;
        elements.selectedTextIndicator.style.display = 'block';
    }

    // Hide selected text indicator
    function hideSelectedTextIndicator() {
        elements.selectedTextIndicator.style.display = 'none';
    }

    // Load existing selection when page loads
    function loadExistingSelection() {
        const selection = window.getSelection();
        const selectedText = selection.toString().trim();

        if (selectedText && selectedText.length <= CONFIG.maxSelectedTextLength) {
            state.selectedText = selectedText;
            state.selectedTextCache = selectedText;  // Store in persistent cache
            showSelectedTextIndicator(selectedText);
        }
    }

    // Send message to backend
    async function sendMessage() {
        const message = elements.input.value.trim();

        if (!message) return;
        if (message.length > CONFIG.maxMessageLength) {
            addMessage('Your message is too long. Please keep it under 2000 characters.', 'error');
            return;
        }

        // Add user message to UI
        addMessage(message, 'user');
        elements.input.value = '';

        // Show loading state with typing indicator
        const loadingMsg = addMessage('🤖 Typing...', 'bot', true);

        try {
            // Use cached selected text if available, otherwise use current state
            const selectedTextToUse = state.selectedTextCache || state.selectedText || null;

            // Prepare the request payload
            const payload = {
                question: message,
                selected_text: selectedTextToUse
            };

            // Send request to backend
            const response = await fetch(`${CONFIG.backendUrl}/chat`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(payload)
            });

            if (!response.ok) {
                if (response.status === 404 || response.status === 502 || response.status === 503) {
                    // Backend service is not available
                    throw new Error(`Backend service temporarily unavailable. Please check if the backend is deployed and accessible.`);
                } else {
                    throw new Error(`Server error: ${response.status} - ${response.statusText}`);
                }
            }

            const data = await response.json();

            // Remove loading message
            removeMessage(loadingMsg);

            // Add bot response to UI
            addMessage(data.answer, 'bot');

            // Add "based on selected text" badge if the response used selected text
            if (state.selectedTextCache || state.selectedText) {
                addContextBadge('Based on selected text');
            }

            // Handle sources if available
            if (data.sources && data.sources.length > 0) {
                addSources(data.sources);
            }

            // Clear the selected text cache after successfully sending the message
            state.selectedTextCache = null;
            hideSelectedTextIndicator();
        } catch (error) {
            // Remove loading message
            removeMessage(loadingMsg);

            // Show improved error message based on error type
            let errorMessage = 'Sorry, I encountered an error processing your request. Please try again.';

            if (error.message.includes('Backend service temporarily unavailable')) {
                errorMessage = 'Backend service is currently unavailable. The RAG chatbot may not be deployed yet or may be experiencing issues. Please check the deployment status.';
            } else if (error.message.includes('Failed to fetch')) {
                errorMessage = 'Unable to connect to the backend service. Please check your internet connection and backend deployment status.';
            } else if (error.message.includes('NetworkError')) {
                errorMessage = 'Network error occurred. Please check your connection and try again.';
            }

            addMessage(errorMessage, 'error');
            console.error('Chat error:', error);
        }
    }

    // Add message to chat UI
    function addMessage(text, sender, isTemporary = false) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `chatbot-message chatbot-message-${sender}`;
        messageDiv.style.cssText = `
            margin-bottom: 12px;
            padding: 12px;
            border-radius: 8px;
            max-width: 85%;
            word-wrap: break-word;
        `;

        if (sender === 'user') {
            messageDiv.style.cssText += `
                background: #4f46e5;
                color: white;
                margin-left: auto;
                text-align: right;
            `;
        } else if (sender === 'bot') {
            messageDiv.style.cssText += `
                background: #f3f4f6;
                color: #374151;
                margin-right: auto;
                text-align: left;
            `;
        } else if (sender === 'error') {
            messageDiv.style.cssText += `
                background: #fee2e2;
                color: #dc2626;
                margin-right: auto;
                text-align: left;
            `;
        }

        messageDiv.innerHTML = text;

        elements.messages.appendChild(messageDiv);
        elements.messages.scrollTop = elements.messages.scrollHeight;

        if (isTemporary) {
            return messageDiv;
        }
    }

    // Remove a message from UI
    function removeMessage(messageElement) {
        if (messageElement && messageElement.parentNode) {
            messageElement.parentNode.removeChild(messageElement);
        }
    }

    // Add sources to chat UI
    function addSources(sources) {
        if (!sources || sources.length === 0) return;

        const sourcesDiv = document.createElement('div');
        sourcesDiv.className = 'chatbot-sources';
        sourcesDiv.style.cssText = `
            margin-top: 8px;
            padding: 8px;
            background: #f0f9ff;
            border-radius: 6px;
            border-left: 3px solid #3b82f6;
            font-size: 12px;
        `;

        // Build source list with clickable links
        let sourcesList = '<strong>Sources:</strong><ul style="margin: 4px 0; padding-left: 16px;">';
        sources.forEach(source => {
            if (source.url) {
                sourcesList += `<li><a href="${source.url}" target="_blank" style="color: #3b82f6; text-decoration: underline;">${source.title || 'Source'}</a></li>`;
            } else if (source.title) {
                sourcesList += `<li>${source.title}</li>`;
            } else {
                sourcesList += `<li>Reference material</li>`;
            }
        });
        sourcesList += '</ul>';

        sourcesDiv.innerHTML = sourcesList;

        elements.messages.appendChild(sourcesDiv);
        elements.messages.scrollTop = elements.messages.scrollHeight;
    }

    // Add context badge to chat UI
    function addContextBadge(text) {
        const badgeDiv = document.createElement('div');
        badgeDiv.className = 'chatbot-context-badge';
        badgeDiv.style.cssText = `
            margin-top: 8px;
            padding: 4px 8px;
            background: #d1fae5;
            color: #065f46;
            border-radius: 12px;
            font-size: 11px;
            display: inline-block;
            margin-bottom: 8px;
        `;

        badgeDiv.textContent = text;

        elements.messages.appendChild(badgeDiv);
        elements.messages.scrollTop = elements.messages.scrollHeight;
    }

    // Initialize the widget when DOM is loaded
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }

})();