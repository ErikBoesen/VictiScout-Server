import requests
import json

#sends data to server 
r = requests.post('http://0.0.0.0:8080/api/data', data={'author': 'Erik', 'text':'test server'})

#retrieve and print data
results = requests.get('http://0.0.0.0:8080/api/data')

print(results.text.encode('utf-8'));
