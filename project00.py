import pandas as ps

df = ps.read_csv('~/Desktop/PythonProject0/vgsales.csv')

n=0

while n == 0:
	userin =input("Enter a Genre and recieve the top games under that genre "+
	"your options include Shooter, Platform, Racing, Adventure, Action, Sports ")

	if userin not in {'Shooter','Platform','Racing','Adventure','Action','Sports'}:
		print("Invalid input Try again with exact spelling")
		n = 0
	else:
		n = 1
		
print(df.loc[df['Genre'] == userin].head(20))