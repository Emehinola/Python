# adding "!" at the end of each string in array
def add_excitement(array):
	array = [f"{word}!" for word in array]
	print(array)
	
add_excitement(["sam", "is", "good"])

# sum all digits in num
def sum_digit(num):
	total = 0
	for i in str(num):
		total += int(i)
		
	return total
	
print(sum_digit(555))