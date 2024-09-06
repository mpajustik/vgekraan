import sys
import logging
from pathlib import Path

# Add the project directory to the sys.path
project_home = str(Path(__file__).resolve().parent)
if project_home not in sys.path:
    sys.path.insert(0, project_home)

from app import app as application  # Import Flask app from app.py

# Configure logging
logging.basicConfig(stream=sys.stderr)