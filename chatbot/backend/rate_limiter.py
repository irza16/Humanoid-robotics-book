import time
from collections import defaultdict, deque
from typing import Dict
import threading
from fastapi import Request, HTTPException
from config import settings


class RateLimiter:
    def __init__(self):
        self.requests = defaultdict(deque)
        self.lock = threading.Lock()

    def is_allowed(self, identifier: str) -> bool:
        """
        Check if a request from the given identifier is allowed based on rate limits
        """
        with self.lock:
            now = time.time()
            # Remove requests older than the time window
            while (self.requests[identifier] and
                   now - self.requests[identifier][0] > settings.rate_limit_window):
                self.requests[identifier].popleft()

            # Check if we've exceeded the rate limit
            if len(self.requests[identifier]) >= settings.rate_limit_requests:
                return False

            # Add the current request
            self.requests[identifier].append(now)
            return True


# Global rate limiter instance
rate_limiter = RateLimiter()


def check_rate_limit(request: Request) -> None:
    """
    Check rate limit for a request, raises HTTPException if limit exceeded
    """
    # Use client IP as identifier (with port to distinguish different connections from same IP)
    client_ip = request.client.host
    if not rate_limiter.is_allowed(client_ip):
        raise HTTPException(
            status_code=429,
            detail="Rate limit exceeded. Please try again later."
        )