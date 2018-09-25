import requests as re
import pytest

print 'Check that user 1 has todo recordings. Use Accert and count recordings'
try:


    responseTodos = re.get('http://jsonplaceholder.typicode.com/todos', timeout=(1000, 1))
    todosTable = responseTodos.json()
    toDoCounter = 0
    for itemTodos in todosTable:
        if itemTodos['userId'] == 1:
            toDoCounter += 1
    print "User 1 has ", toDoCounter, "to do items"
    # assert (toDoCounter > 0), 'Not passed'
    def test_3():
        toDoCounter > 0



except re.exceptions.ReadTimeout:
    print('Oops. Read timeout occured')
except re.exceptions.ConnectTimeout:
    print('Oops. Connection timeout occured!')