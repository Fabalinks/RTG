def get_credentital():
    username = input ("type username")
    password = input("type password")
    return username, password

def authenticate(username,password,pwdb):
    auth=False
    if username in pwdb:
        if password == pwdb[username]:
            print('Authentication succesful')
            auth = True
        else:
            print('wrong password ')
    else:
        print ('User not known! ')
    return auth

pwdb = {'fabian':'sickpass',
        'sandra': 'greatpwd'}
username,password = get_credentital()
authenticate(username,password,pwdb)



