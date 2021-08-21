# Create a New Python File and Import the Flask Dependency
from flask import Flask

# Create a New Flask App Instance
app = Flask(__name__)

# Create Flask Routes
@app.route('/')
def hello_world():
    return 'Hello world'

# Think of some simple code from which you could create a route. 
# Then try to create a new route implementing that logic.
# comment out code above to run app2
app2 = Flask(__name__)
@app2.route('/')
def name():
    return 'My name is Jordan'


# Run a Flask App
# Run this in command line in terminal
#   export FLASK_APP=app.py
#   flask run
# Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
# Copy and paste the localhost address into the web browser. 