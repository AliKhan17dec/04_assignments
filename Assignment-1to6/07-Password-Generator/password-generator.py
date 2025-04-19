import random

print('Welcome to you password Generator')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'

number = input('Amount of Passwords to generate: ')
number = int(number)

length = input('Input your password lenght: ')
length = int(length)

print('\nhere are you password:')

for pwd in range(number):
    passwords = ''
    for c in range(length):
      passwords += random.choice(chars)
    print(passwords)
