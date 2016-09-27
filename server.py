import os
import json
from project import app
from flask import request, jsonify
from models.DBClient import DBClient

# MongoDB client
client = DBClient('localhost', 27017)

# Main page
@app.route('/')
def start():
    return '<h1>It works!</h1>\nThis is the main page for the scouting server. This page itself is useless. If you want to upload some data, submit it with a POST request to /api/data.'

# Open data submission route
@app.route('/api/data', methods = ['GET', 'POST'])
def data():
    # If user is POSTing data,
    if request.method == 'POST':
        p = {'data': request.form['data']}
        client.insertData(p)
        return 'It worked!'

    # If user gives a GET request, return all the data that has been gathered.
    elif request.method == 'GET':
        return client.getData()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run('0.0.0.0', port = port)
