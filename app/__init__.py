# Flask
from flask import Flask

# Create the Flask app
app = Flask(__name__)

# These imports are Python files in the directory (the /app package)
# Global app.config settings
from app import config
