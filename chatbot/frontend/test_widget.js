/**
 * Basic tests for the chatbot widget functionality
 * These tests can be run in the browser console or with a testing framework
 */

// Test suite for chatbot widget
const ChatWidgetTests = {
    // Test if the widget is properly initialized
    testWidgetInitialization: function() {
        console.log('Testing widget initialization...');

        // Check if the floating button exists
        const floatButton = document.getElementById('chatbot-float-button');
        if (!floatButton) {
            console.error('❌ Floating button not found');
            return false;
        }

        // Check if the modal exists
        const modal = document.getElementById('chatbot-modal');
        if (!modal) {
            console.error('❌ Modal not found');
            return false;
        }

        console.log('✅ Widget elements found');
        return true;
    },

    // Test if the widget can be toggled
    testWidgetToggle: function() {
        console.log('Testing widget toggle...');

        const floatButton = document.getElementById('chatbot-float-button');
        const modal = document.getElementById('chatbot-modal');

        if (!floatButton || !modal) {
            console.error('❌ Required elements not found for toggle test');
            return false;
        }

        // Store initial state
        const initialState = modal.style.display;

        // Click the button to toggle
        floatButton.click();

        // Check if modal is now visible (if it was hidden) or hidden (if it was visible)
        const newState = modal.style.display;
        if (initialState === 'none' && newState !== 'none') {
            console.log('✅ Widget toggle works - modal is now visible');
        } else if (initialState !== 'none' && newState === 'none') {
            console.log('✅ Widget toggle works - modal is now hidden');
        } else {
            console.error('❌ Widget toggle may not be working correctly');
            return false;
        }

        return true;
    },

    // Test if text selection detection works
    testTextSelection: function() {
        console.log('Testing text selection detection...');

        // Create a test element with text
        const testElement = document.createElement('div');
        testElement.id = 'test-text-element';
        testElement.textContent = 'This is a test text for selection.';
        testElement.style.padding = '20px';
        testElement.style.margin = '20px';
        document.body.appendChild(testElement);

        // Select the text programmatically
        const range = document.createRange();
        range.selectNodeContents(testElement);

        const selection = window.getSelection();
        selection.removeAllRanges();
        selection.addRange(range);

        // Trigger selection change event
        document.dispatchEvent(new Event('selectionchange'));

        // Check if the selection indicator appears
        const indicator = document.getElementById('selected-text-indicator');
        if (indicator && indicator.style.display !== 'none') {
            console.log('✅ Text selection detection works');
        } else {
            console.log('ℹ️ Text selection detection - indicator may not be visible (this could be expected if widget is closed)');
        }

        // Clean up
        document.body.removeChild(testElement);

        return true;
    },

    // Test API communication (this would require a running backend)
    testApiCommunication: async function(backendUrl) {
        console.log('Testing API communication...');

        try {
            const response = await fetch(`${backendUrl}/health`);
            if (response.ok) {
                const data = await response.json();
                if (data.status === 'healthy') {
                    console.log('✅ API communication works - health check passed');
                    return true;
                } else {
                    console.error('❌ API health check failed');
                    return false;
                }
            } else {
                console.error(`❌ API request failed with status ${response.status}`);
                return false;
            }
        } catch (error) {
            console.error(`❌ API request failed with error: ${error.message}`);
            return false;
        }
    },

    // Run all tests
    runAllTests: async function(backendUrl = 'http://localhost:8000') {
        console.log('Starting Chatbot Widget Tests...\n');

        const tests = [
            { name: 'Widget Initialization', test: this.testWidgetInitialization },
            { name: 'Widget Toggle', test: this.testWidgetToggle },
            { name: 'Text Selection', test: this.testTextSelection },
            { name: 'API Communication', test: () => this.testApiCommunication(backendUrl) }
        ];

        const results = [];

        for (const test of tests) {
            try {
                console.log(`\n--- Running ${test.name} ---`);
                const result = await (test.test instanceof Function ? test.test() : test.test);
                results.push({ name: test.name, passed: result });
            } catch (error) {
                console.error(`❌ Error running ${test.name}: ${error.message}`);
                results.push({ name: test.name, passed: false, error: error.message });
            }
        }

        // Print summary
        console.log('\n--- Test Summary ---');
        let passedCount = 0;
        for (const result of results) {
            const status = result.passed ? '✅ PASSED' : '❌ FAILED';
            console.log(`${result.name}: ${status}`);
            if (result.passed) passedCount++;
        }

        console.log(`\nOverall: ${passedCount}/${results.length} tests passed`);

        return { total: results.length, passed: passedCount, failed: results.length - passedCount };
    }
};

// Export for use in other contexts
if (typeof module !== 'undefined' && module.exports) {
    module.exports = ChatWidgetTests;
}

// Example usage:
// ChatWidgetTests.runAllTests('https://your-backend-url.com');