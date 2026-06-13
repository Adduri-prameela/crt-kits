pin=input('Enter the password :')
try:
    if(pin=='1234'):
        print('Logic is successful')
    else:
        raise TypeError('Incorrect Password')
except TypeError as e:
    print(e)