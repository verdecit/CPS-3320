# Hangman game!
# Assume the answer is "hangman"
import random

r =random.randint(0,2)

words = [['s','n','o','w'],['s','p','e','e','d'],['p','y','t','h','o','n']]
A = words[r]
L = ['_','_','_','_','_','_','_']
play = True
incorrect = 0
while play == True: 
	letter = str(input("Guess a letter: "))
	i = 0  # Check to see if that letter is in the Answer
	for currentletter in A:
		if letter == currentletter: # If the letter the user guessed is found in the answer
			L[i] = letter 	
		i=i+1		# set the underscore in the user's answer to that letter
	print(' '.join(str(n) for n in L))	# Display what the player has thus far (L) with a space
			
	if A == L:
		play = False #Test to see if the word has been successfully completed, and if so, end the loop
		print("GREAT JOB!")
else:
	print(' '.join(str(n) for n in L))
	print("BAD GUESS!")
	incorrect=incorrect+1
	if incorrect == 6:
		play = False
		print("Game Over")

