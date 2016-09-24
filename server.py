#standard imports

import os
import json
from project import app
from flask import request, jsonify
from models.DBClient import DBClient

#Mongodb client
client = DBClient('localhost', 27017)

#base route
@app.route('/')
def start():
    return 'hello'

#data submission route
@app.route('/api/data', methods=['GET', 'POST'])
def data():
    #retrieve data
    if request.method == 'GET':
        return client.getAllResults()

    #submit data
    elif request.method == 'POST':
        p = {'author': request.form['author'], 'text': request.form['text']}
        client.insertData(p)
        return 'It worked!'

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run('0.0.0.0', port=port)
