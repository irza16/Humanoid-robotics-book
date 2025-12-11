from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from typing import Callable
import logging
import time
import traceback

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class LoggingMiddleware:
    """Middleware for logging requests and responses"""

    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        if scope["type"] != "http":
            return await self.app(scope, receive, send)

        request = Request(scope)
        start_time = time.time()

        # Log the incoming request
        logger.info(f"Request: {request.method} {request.url}")

        # Capture response
        response_body = b""

        async def send_with_capture(message):
            if message["type"] == "http.response.body":
                response_body = message.get("body", b"")
            await send(message)

        # Process the request
        await self.app(scope, receive, send_with_capture)

        # Log the response
        process_time = time.time() - start_time
        logger.info(f"Response: {request.method} {request.url} - Process time: {process_time:.2f}s")


async def validation_exception_handler(request: Request, exc: HTTPException):
    """Handle validation exceptions"""
    logger.error(f"Validation error: {exc.detail}")
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": "VALIDATION_ERROR", "message": str(exc.detail)}
    )


async def general_exception_handler(request: Request, exc: Exception):
    """Handle general exceptions"""
    logger.error(f"General error: {str(exc)}")
    logger.error(traceback.format_exc())
    return JSONResponse(
        status_code=500,
        content={"error": "INTERNAL_ERROR", "message": "An internal error occurred"}
    )


def add_error_handlers(app):
    """Add error handlers to the FastAPI app"""
    app.add_exception_handler(HTTPException, validation_exception_handler)
    app.add_exception_handler(Exception, general_exception_handler)