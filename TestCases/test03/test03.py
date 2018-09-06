import requests as re

print 'Check that user 1 has todo recordings. Use Accert and count recordings'
try:


    responseTodos = re.get('http://jsonplaceholder.typicode.com/todos', timeout=(1000, 1))
    todosTable = responseTodos.json()
    q = 0
    for itemTodos in todosTable:
        if itemTodos['userId'] == 1:
            q += 1
    print "shtyk", q
    assert (q > 0), 'Not passed'




except re.exceptions.ReadTimeout:
    print('Oops. Read timeout occured')
except re.exceptions.ConnectTimeout:
    print('Oops. Connection timeout occured!')