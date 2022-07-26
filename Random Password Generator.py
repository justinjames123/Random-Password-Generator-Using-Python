import random

print(" *** Welcome To My Random Password Generator ***")

print()

chars = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789`~!@#$%^&*()-_=+\|]}[{;:""/?.>,< "

num = int(input("How Many Passwords Do You Want? "))

len = int(input("What Should Be The Length Of The Passwords? "))

print("Here Are Your Passwords: ")

print()
for pwd in range(num):
    passwords = ''
    for i in range (len):
        passwords += random.choice(chars)
    print(passwords)


