import time
import random
from functools import wraps
from typing import Callable, Type, Any
import logging

logger = logging.getLogger(__name__)

def retry_with_backoff(
    max_retries: int = 3,
    base_delay: float = 1.0,
    max_delay: float = 60.0,
    backoff_factor: float = 2.0,
    exceptions: tuple = (Exception,)
):
    """
    Decorator to retry a function with exponential backoff.

    Args:
        max_retries: Maximum number of retry attempts
        base_delay: Initial delay in seconds
        max_delay: Maximum delay in seconds
        backoff_factor: Factor by which delay increases after each retry
        exceptions: Tuple of exceptions to catch and retry on
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            last_exception = None

            for attempt in range(max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e

                    if attempt == max_retries:
                        # Last attempt, raise the exception
                        logger.error(f"Function {func.__name__} failed after {max_retries} retries: {str(e)}")
                        raise e

                    # Calculate delay with exponential backoff and jitter
                    delay = min(base_delay * (backoff_factor ** attempt), max_delay)
                    jitter = random.uniform(0, delay * 0.1)  # Add up to 10% jitter
                    total_delay = delay + jitter

                    logger.warning(
                        f"Attempt {attempt + 1} failed for {func.__name__}: {str(e)}. "
                        f"Retrying in {total_delay:.2f}s..."
                    )

                    time.sleep(total_delay)

            # This line should never be reached, but included for type checking
            raise last_exception

        return wrapper
    return decorator


class RetryableAPI:
    """
    A class to handle retryable API calls with exponential backoff.
    """

    def __init__(
        self,
        max_retries: int = 3,
        base_delay: float = 1.0,
        max_delay: float = 60.0,
        backoff_factor: float = 2.0,
        exceptions: tuple = (Exception,)
    ):
        self.max_retries = max_retries
        self.base_delay = base_delay
        self.max_delay = max_delay
        self.backoff_factor = backoff_factor
        self.exceptions = exceptions

    def call(self, func: Callable, *args, **kwargs) -> Any:
        """
        Call a function with retry logic.
        """
        last_exception = None

        for attempt in range(self.max_retries + 1):
            try:
                return func(*args, **kwargs)
            except self.exceptions as e:
                last_exception = e

                if attempt == self.max_retries:
                    # Last attempt, raise the exception
                    logger.error(f"API call failed after {self.max_retries} retries: {str(e)}")
                    raise e

                # Calculate delay with exponential backoff and jitter
                delay = min(self.base_delay * (self.backoff_factor ** attempt), self.max_delay)
                jitter = random.uniform(0, delay * 0.1)  # Add up to 10% jitter
                total_delay = delay + jitter

                logger.warning(
                    f"API call attempt {attempt + 1} failed: {str(e)}. "
                    f"Retrying in {total_delay:.2f}s..."
                )

                time.sleep(total_delay)

        # This line should never be reached, but included for type checking
        raise last_exception