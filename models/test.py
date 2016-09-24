from DBClient import DBClient

#test insert and retrieval
test = DBClient('localhost', 27017)
post = {'author': 'Tom',
        'text': 'test server'}
test.insertData(post)

print(test.getAllResults())
