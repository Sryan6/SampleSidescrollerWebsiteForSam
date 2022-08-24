# Main. See /app package and its __init__.py, which ultimately runs this
# This page is the target of FLASK_APP, that is FLASK_APP=main.py
from flask import Flask
from dotenv import load_dotenv

# Below, again, see /app package and its files for organizing the site
from app import app, config
import json
import os
import re
import sys
import time

from datetime import datetime

# from dotenv import load_dotenv
from flask import (
    render_template,
    flash,
    request,
    redirect,
    send_from_directory,
    session)

from pathlib import Path

# Configure variables in .env file in root directory
load_dotenv()

# Get path from app
path = app.config['PATH']

@app.route("/")
def home():
    return "Hello, World!"
    
if __name__ == "__main__":
    app.run(debug=True)