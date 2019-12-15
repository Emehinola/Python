#working on my_operator
a = int(input("Enter a number:"))

b = int(input("Enter another number:"))

print(" ")

print("Loading your data...")

print(" ")

print(" ")
if (a == 3) or (b == 3):
	print("One of the number you just \nentered is 3")

elif a == b:
	print("The two numbers you just \nentered are the same")

else:
	print("Alright you choose:", a, "and", b)
print("The sum of the two numbers is:", a+b)	
if a == b:
	print("It is possible for", a, "to be your favourite number")
else:
	print(" ")
		
	print("I guess; your favorite numbers should either be:", a, "or", b, "Even possibly be both:", a, "and", b)	
print('.')	
print('.')
print('.')
print('Thanks for your feedbacks, your data will be processed in \ndue time')
    #program to sum the first n numbers:
	
def sum_me(num):
	
	if num==1:
		
		return 1

	else:
		
		return (num+sum_me(num-1))
num=int(input("Enter your number:"))

print("The sum of the first n natural ", num, "numbers gives", sum_me(num ))