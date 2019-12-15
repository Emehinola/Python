result = []

def prime_num(numbers):
	for numb in numbers:
		if numb == 1:
			numbers.remove(1)
		for num in range(2,numb):
			if numb % num == 0:
				result.append(numb)
			
	def get_result(result):
		prime = []
		for items in numbers:
			if items not in result:
				prime.append(items)
		
		return prime
		
	print(get_result(result))
numbers = [1,2,3,5,17,21]		
prime_num(numbers)