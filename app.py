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

# For Hugging Face Spaces and other deployment platforms,
# map DATABASE_URL to NEON_DATABASE_URL if needed
if 'DATABASE_URL' in os.environ and 'NEON_DATABASE_URL' not in os.environ:
    os.environ['NEON_DATABASE_URL'] = os.environ['DATABASE_URL']

# Import and expose the main application
from main import app

if __name__ == "__main__":
    import uvicorn

    # Support both PORT and PORT_8000 environment variables
    port = 8000
    if 'PORT' in os.environ:
        try:
            port = int(os.environ['PORT'])
        except ValueError:
            port = 8000
    # HF Spaces uses port 7860 by default
    elif 'SPACE_ID' in os.environ:  # Hugging Face Spaces specific variable
        port = 7860

    uvicorn.run(app, host="0.0.0.0", port=port)