# This file helps Railway detect this as a Python project
# The main application is in chatbot/backend/main.py

import os
import sys

# Change to the project root directory to ensure relative imports work
project_root = os.path.dirname(__file__)
os.chdir(project_root)

# Add the project root and backend directory to the Python path
backend_path = os.path.join(project_root, 'chatbot', 'backend')
sys.path.insert(0, project_root)
sys.path.insert(0, backend_path)

# Import and expose the main application
from main import app

if __name__ == "__main__":
    import uvicorn

    if 'PORT' in os.environ:
        port = int(os.environ['PORT'])
    else:
        port = 8000

    uvicorn.run(app, host="0.0.0.0", port=port)