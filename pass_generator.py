import random
chars='abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ#$%&()*+-/@^<>'

def password(num, length):
    for i in range(num):
        password=''
        for i in range(length):
            password +=random.choice(chars)
        print(password)
    return None


length=int(input('password length?'))
num=int(input('how many passwords?'))
print('Generated passwords are:')
password(num,length)