# program to switch input

alphas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

keys = "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26" #reversed(alphas)

value = ""

while value != "stop":
	value = input("Enter a value: ")
	
	for alpha, key in zip(alphas, keys):
		if alpha == value:
			print("The key is", key)
			break
			
else:
	print("Stopped")
		