from Credit_card import get_cc, validate
import re

#digit = "5399839100199610"
unc_digit = "53998301****1473"

def generate():
	global digit, unc_digit
	
	for num in range(10000):
		if len(str(num)) == 4:
			digit = unc_digit.replace("****", str(num))
			if validate(get_cc(digit)):
				print(f"The missing digits are {num}")
				print(digit)
			
generate()