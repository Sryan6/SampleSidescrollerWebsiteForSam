import os
from app import app

# The path to this file
app.config['PATH'] = os.path.dirname(os.path.realpath(__file__))

# Are we in development mode or production?
# Development
if os.getenv('FLASK_ENV') == "development":
    app.config['DEV_MODE'] = 1
else:
    # Production
    app.config['DEV_MODE'] = 0