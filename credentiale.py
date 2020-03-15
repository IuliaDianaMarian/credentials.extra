#this program asks you to choose an alph username and num password then asks you to log in with those credentials
#if you try to log in with an unknown username, it will ask you if you want to create a new account

database={}

print('welcome. please choose a username. it can only contain letters.')

username=input()

while True:
    if username.isalpha():
        break
    print('please write a username composed of only letters')
    username=input()


while username in database.keys():
    print('this username is taken. please choose another username')
    username=input()


print('now please choose a password composed of only numbers')

password=input()

while True:
    if password.isdecimal():
        break
    print('please choose a password composed of numbers')
    password=input()

database[username]=password

print('Thank you. Now please log in with the chosen username and password')

while True:
    print('please type your username')
    user=input()
    if user not in database.keys():
        print('there is no user registered with this username. do you wish to create a new account with this username? type yes or no')
        input=input()
        if input=='no':
            print('no problem')
        else:
            print('choose a password for the above introduced username')
            passw=input()
            database[user]=passw
            print('Now please log in with the chosen username and password')
            break
    else:
        break

print('username in database. now please type the password linked to this account.')

passwordAsked=input()

while True:
    if passwordAsked==database.get(user,0):
        print('log in successful')
        break
    else:
        print('try again')
        passwordAsked=input()

    