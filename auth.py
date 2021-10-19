def get_credentital():
    username = input ("type username")
    password = input("type password")
    return username, password

username,password = get_credentital()
print (username, password)