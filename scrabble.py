#scrabble game program
#program takes input from user and outputs the value of the input provided
l=input("Hello please enter a letter ")
l=l.lower()
def letterScore(l):
	if l in 'anoerstuil':
		return 1
	elif l in 'dg':
		return 2
	elif l in 'bcpm':
		return 3
	elif l in 'fhvwy':
		return 4
	elif l in 'k':
		return 5
	elif l in 'jx':
		return 8
	elif l in 'qz':
		return 10
	else:
		return 0
print(letterScore(l))

w=input("Hello please enter a word ")
w=w.lower()
def wordScore(w):
	score=0
	for i in range(len(w)):
		score = score + letterScore(w[i])
	return score
print(wordScore(w))
