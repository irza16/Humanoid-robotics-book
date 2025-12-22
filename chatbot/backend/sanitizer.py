import html
import re
from typing import Optional


def sanitize_input(text: Optional[str]) -> Optional[str]:
    """
    Sanitize user input to prevent injection attacks
    """
    if text is None:
        return None

    # Remove potentially dangerous characters/sequences
    # First, HTML escape to prevent XSS
    text = html.escape(text)

    # Remove or escape other potentially dangerous patterns
    # This is a basic implementation - in production, you might want more sophisticated sanitization
    dangerous_patterns = [
        r'<script.*?>.*?</script>',  # Script tags
        r'javascript:',              # JavaScript URLs
        r'on\w+\s*=',               # Event handlers
        r'<iframe.*?>',              # Iframe tags
        r'<object.*?>',              # Object tags
        r'<embed.*?>',               # Embed tags
    ]

    for pattern in dangerous_patterns:
        text = re.sub(pattern, '', text, flags=re.IGNORECASE | re.DOTALL)

    return text.strip()


def sanitize_url(url: Optional[str]) -> Optional[str]:
    """
    Sanitize URL input to ensure it's a valid HTTP/HTTPS URL
    """
    if url is None:
        return None

    # Basic URL validation - ensure it starts with http:// or https://
    url = url.strip()
    if url.startswith(('http://', 'https://')):
        return url
    else:
        # If it doesn't have a protocol, return None or a safe default
        return None