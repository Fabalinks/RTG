import json

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

def write_pwdb(pwdb):

    with open('pwdb.json','wt') as pwdb_file:
        json.dump(pwdb,pwdb_file)
    print('Pwdb written!')

def read_pwdb():
    with open('pwdb.json', 'rt') as pwdb_file:
        pwdb = json.load(pwdb_file)
    return pwdb



pwdb = {'fabian':'sickpass',
        'sandra': 'greatpwd'}
username,password = get_credentital()
write_pwdb(pwdb)
pwdb = read_pwdb()
authenticate(username,password,pwdb)



