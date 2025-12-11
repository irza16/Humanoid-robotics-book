import React, { useEffect } from 'react';

// Docusaurus Root component to integrate the chatbot widget
export default function Root({ children }) {
  useEffect(() => {
    // Check if script is already loaded to prevent duplicates
    const existingScript = document.querySelector('script[src="/Humanoid-robotics-book/chatbot-widget.js"]');
    if (!existingScript) {
      // Load the chatbot widget script dynamically
      const script = document.createElement('script');
      // When Docusaurus serves with baseUrl, static files are available at baseUrl path
      script.src = '/Humanoid-robotics-book/chatbot-widget.js'; // Served from static directory relative to base URL
      script.async = true;
      script.onload = () => {
        console.log('Chatbot widget script loaded successfully');
        // The chatbot widget should now use the configured backend URL
      };
      // Set the backend URL as a data attribute on the script for the widget to use
      script.setAttribute('data-backend-url', 'http://localhost:8000');
      script.onerror = () => {
        console.error('Failed to load chatbot widget script');
      };
      // Add console log to verify script is being added
      console.log('Adding chatbot widget script to page from:', script.src);
      document.body.appendChild(script);
    } else {
      console.log('Chatbot widget script already exists');
    }

    // Clean up the script when component unmounts
    return () => {
      const scripts = document.getElementsByTagName('script');
      for (let i = 0; i < scripts.length; i++) {
        if (scripts[i].src && scripts[i].src.includes('chatbot-widget.js')) {
          document.body.removeChild(scripts[i]);
          console.log('Removed chatbot widget script');
          break;
        }
      }
    };
  }, []);

  return <>{children}</>;
}