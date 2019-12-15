import re, time, sys

turns = 5
attempts = []
enter = "" # input from user
word = ""

def wrong():
	global turns
	global attempts, enter
	
	turns -= 1
	attempts.append(enter)
	return f"Not in word... Guess again"
	
def won():
	return "Congratuations, You won!..."

def gameOver():
	global word
	print("Game over...")
	print(f"The correct full word is: {word}")
	
	try_again = input("Do you want to try again?: ")
	
	if try_again.lower() == "yes":
		print("\n")
		play()
		
	else:
		sys.exit(1)

def play():
	global turns
	global attempts, enter, word
	
	k = []
	print("..............Welcome to hangman game..............")
	print("")
	word = "polymorphism"
	print("word: ", word.replace(word, "*"*len(word)))
			
	while enter != "quit":
		print(" ")
		print("")

		enter = input("Guess a letter:  ")
		word = "polymorphism"
		
		if enter in word:
			for i in word:
				if i != enter and i not in k:
					r = word.replace(i, "*", 1)
					word = r
				else:
					r = word.replace(enter, enter, 1)
					word = r
			if "*" not in word:
				won()
				#print("You won!..")
				#return word
			k.append(enter)		
			print("word: ", r)
			
		else:
			wrong()
			
		if turns == 0:
			gameOver()
			
		print(f"{turns} turn(s) remainig")
		print("Incorrect attempts: ",  end="")
		for i in attempts:
				print(i, " ", end="")
		time.sleep(1)
		
		#return word
		
if __name__ == "__main__":
	play()