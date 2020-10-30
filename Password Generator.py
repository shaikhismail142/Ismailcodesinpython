import random
import string

def fun():

    length = int(input("Enter no. of characters for your password: \n"))

    character = input("Do you want letters included in your password? press 'Y' for Yes and 'N' for no..")

    if character == 'Y':

        password_characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(password_characters) for i in range(length))
        print("Random string password is:", password)

    elif character == 'N':
        password_characters = string.digits + string.punctuation
        password = ''.join(random.choice(password_characters) for i in range(length))
        print("Random string password is:", password)
fun()