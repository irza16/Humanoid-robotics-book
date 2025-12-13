# This file helps Railway detect this as a Python project
# The main application is in chatbot/backend/main.py

import os
import sys

# Change to the backend directory and run the main application
if __name__ == "__main__":
    backend_path = os.path.join(os.path.dirname(__file__), 'chatbot', 'backend')
    sys.path.insert(0, backend_path)
    os.chdir(backend_path)

    # Import and run the main application
    from main import app
    import uvicorn

    if 'PORT' in os.environ:
        port = int(os.environ['PORT'])
    else:
        port = 8000

    uvicorn.run(app, host="0.0.0.0", port=port)