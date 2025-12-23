import React, { useEffect } from 'react';

// Docusaurus Root component to integrate the chatbot widget
export default function Root({ children }) {
  useEffect(() => {
    // Determine the base URL based on the current hostname
    const isGitHubPages = window.location.hostname.includes('github.io');
    const baseUrl = isGitHubPages ? '/Humanoid-robotics-book' : '';

    // Check if script is already loaded to prevent duplicates
    const scriptPath = `${baseUrl}/chatbot-widget.js`;
    const existingScript = document.querySelector(`script[src="${scriptPath}"]`);

    if (!existingScript) {
      // Load the chatbot widget script dynamically
      const script = document.createElement('script');
      script.src = scriptPath; // Served from static directory relative to base URL
      script.async = true;
      script.onload = () => {
        console.log('Chatbot widget script loaded successfully');
        // The chatbot widget should now use the configured backend URL
      };
      // Set the backend URL as a data attribute on the script for the widget to use
      // Use production URL for GitHub Pages/Vercel, localhost for development
      const isLocalhost = window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1';
      const backendUrl = isLocalhost ? 'http://localhost:8000' : 'https://superb-joy-production-b689.up.railway.app';
      script.setAttribute('data-backend-url', backendUrl);
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
          if (scripts[i].parentNode) {
            scripts[i].parentNode.removeChild(scripts[i]);
          }
          console.log('Removed chatbot widget script');
          break;
        }
      }
    };
  }, []);

  return <>{children}</>;
}