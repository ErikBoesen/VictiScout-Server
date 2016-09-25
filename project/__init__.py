#sets up the Flask object
from flask import Flask
app = Flask('VictiScout-Server')
app.config['SECRET_KEY'] = 'random'
app.debug = True
