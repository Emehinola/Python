# import triangular stars
from stars import f
from halfStar import half
 # width of rectangle
 
def rect(n=12, left=11):
	# loop to draw out shape
	for i in range(1, n+1):
		if (i>=3)&(i<n):
			result = f"1 2 3 {' '*int(2*n-13)} 3 2 1"
			print(' '*left, result)
		elif (i>=2)&(i<n):
			result = f"1 2 {'3'*int(2*n-9)} 2 1"
			print(' '*left, result)
			
		elif (i>=1)&(i<n): # creating space inside the rectangle
			result = f"1{' '*int(2*n-3)}1"
			print(' '*left, result)
		else:
			result = n * '* '
			print(' '*left, result)
f(12)
rect()
half(20, 12)
rect(20, 3)