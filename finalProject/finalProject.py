import random, string, datetime
from random import shuffle

#function to scramble the passwords that are generated to randomize the order
def scramble(word):
	word = list(word)
	shuffle(word)
	return ''.join(word)

print('\nHello User, this program is here to allow you to easily generate a secure and customizable password'
	+'\nYour passwords will be saved to a "passwords" file in the same directory you run this program\n'+
	'-----------------------------------------------------------------------------------\n')
print('Tell me which service this is for so I can add it next to your time stamp for organizational purposes'+
'\n\nTell me the characteristics of your new password, your choices are\nlowercase, uppercase, numbers and special characters\n')

service = input('What service is this password being used for?: \n')

#variables to save the instances of each password characteristic chosen by the user

lowercase = eval(input('Enter how many LOWERCASE letters you want. If you don\'t then enter 0 \n'))
uppercase = eval(input('Enter how many UPPERCASE letters you want. If you don\'t then enter 0 \n'))
numbers = eval(input('Enter how many NUMBERS you want. If you don\'t then enter 0 \n'))
specialch = eval(input('Enter how many SPECIAL CHARACTERS you want. If you don\'t then enter 0 \n'))

 #save all lowercase letters and uppercase letters to variables from string library
lowercValues = string.ascii_lowercase
uppercValues = string.ascii_uppercase
specialchValues = ['!','@','#','$','%','^','&','*','(',')']

lowercaseKeys = ''
uppercaseKeys = ''
numberKeys = ''
specialKeys = ''

#adding values to each variable according the the amount the user chooses
for i in range (lowercase):
	lowercaseKeys = lowercaseKeys + random.choice(lowercValues)

for i in range (uppercase):
	uppercaseKeys = uppercaseKeys + random.choice(uppercValues)

for i in range (numbers):
	numberKeys = numberKeys + str(random.randrange(10))

for i in range (specialch):
	specialKeys = specialKeys + random.choice(specialchValues)

#concatinating the variables into a single variable then scrambling them with the custom function
password = lowercaseKeys + uppercaseKeys + numberKeys + specialKeys
password = scramble(password)

#creating a file for the passwords generated with a timestamp for when the program is run and the service the password is for
output = open("passwords.txt","a")
output.write('New password: '+password+' Generated on {:%b-%d-%Y %H:%M:%S} '.format(datetime.datetime.now())+service+'\n')
output.close()

print('\nHere is your new password: '+password)
print()