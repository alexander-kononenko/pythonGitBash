import requests as re

print "list with POST from body for used with id=3"
try:
    responsePost = re.get('http://jsonplaceholder.typicode.com/posts', timeout=(1000, 1))
    postTable = responsePost.json()
    listPost = []
    for itemPst in postTable:
        if itemPst['userId'] == 3:
            listPost.append([itemPst['body']])
    print listPost


except re.exceptions.ReadTimeout:
    print('Oops. Read timeout occured')
except re.exceptions.ConnectTimeout:
    print('Oops. Connection timeout occured!')