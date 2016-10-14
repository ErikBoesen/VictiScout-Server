import os
import json
from project import app
from flask import request, jsonify


# Main page
@app.route('/')
def start():
    """Show a working notification on the root page."""
    return '<h1>It works!</h1>\nThis is the main page for the scouting server. This page itself is useless. If you want to upload some data, submit it with a POST request to /api/data. If you want to fetch ALLL the data, submit a GET request. All this stuff is done automatically through the VictiScout application. Check it out sometime.'


# Open data submission route
@app.route('/api/data', methods=['GET', 'POST'])
def data():
    # If user is POSTing data,
    if request.method == 'POST':
        json_file = open('data.json', 'a')
        json_file.write(str(json.dumps(request.form)) + '\n')
        return 'It worked!'

    # If user gives a GET request, return all the data that has been gathered.
    elif request.method == 'GET':
        json_file = open('data.json', 'r')
        return json_file.read()


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run('0.0.0.0', port=port)
