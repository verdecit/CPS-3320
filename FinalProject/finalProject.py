import random, string, datetime
from random import shuffle

def scramble(word):
	word = list(word)
	shuffle(word)
	return ''.join(word)

print('\nHello User, this program is here to allow you to easily generate a secure and customizable password'
	+'\nYour passwords will be saved to a "passwords" file in the same directory you run this program\n'+
	'-----------------------------------------------------------------------------------\n')


print('Tell me the characteristics of your new password, your choices are\nlowercase, uppercase, numbers and special characters\n')


lowercase = eval(input('Enter how many LOWERCASE letters you want. If you don\'t then enter 0 \n'))
uppercase = eval(input('Enter how many UPPERCASE letters you want. If you don\'t then enter 0 \n'))
numbers = eval(input('Enter how many NUMBERS you want. If you don\'t then enter 0 \n'))
specialch = eval(input('Enter how many SPECIAL CHARACTERS you want. If you don\'t then enter 0 \n'))

 
lowercValues = string.ascii_lowercase
uppercValues = string.ascii_uppercase
specialchValues = ['!','@','#','$','%','^','&','*','(',')']

lowercaseKeys = ''
uppercaseKeys = ''
numberKeys = ''
specialKeys = ''

for i in range (lowercase):
	lowercaseKeys = lowercaseKeys + random.choice(lowercValues)

for i in range (uppercase):
	uppercaseKeys = uppercaseKeys + random.choice(uppercValues)

for i in range (numbers):
	numberKeys = numberKeys + str(random.randrange(10))

for i in range (specialch):
	specialKeys = specialKeys + random.choice(specialchValues)

password = lowercaseKeys + uppercaseKeys + numberKeys + specialKeys
password = scramble(password)

output = open("passwords.txt","a")
output.write('New password: '+password+' Generated on {:%b-%d-%Y %H:%M:%S} \n'.format(datetime.datetime.now()))
output.close()

print('\nHere is your new password: '+password)
print()
