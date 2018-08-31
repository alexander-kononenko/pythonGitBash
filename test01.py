import requests as re

print 'Count users which contains 5 in zipcode'
try:
    response = re.get('http://jsonplaceholder.typicode.com/users', timeout=(1000, 1))
    userTable = response.json()
    yes = 0
    no = 0
    for itemUsr in userTable:
        if '5' in str([itemUsr['address']['zipcode']]):
            yes += 1

        else:
            no += 1

    print "Number 5 is found for", yes, "users"
    print "For", no, "number 5 is not found"



except re.exceptions.ReadTimeout:
    print('Oops. Read timeout occured')
except re.exceptions.ConnectTimeout:
    print('Oops. Connection timeout occured!')
