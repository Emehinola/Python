import sys

"""
Python program to validate 
credit card using Luhn's Algorithm
"""
rev = ""
def get_cc(card_num):
    global rev

    if len(card_num) < 9:
        print("Invalid digit")
        sys.exit(1)
		
    else:
        # reversed form of the number
        reversed_num = list(card_num[::-1])
        reversed_num = list(map(lambda x:int(x), reversed_num))
        rev = reversed_num[1:] # the first number is the check digit
    return rev

def validate(reversed_num):
    sorted_num = [] # empty list to multiply every sec digit of the card by two
    for index,nums in enumerate(reversed_num):
        if index % 2 != 0:
            sorted_num.append(nums)
        else:
            sorted_num.append(nums*2) # append every sec digit by 2 times of their values
  
# get the sum of all the numbers
    every_dig = []
    for i in sorted_num:
        if i > 9:
            every_dig.append(i-9)
        else:
            every_dig.append(i)
    sum_num = 0
    for num in tuple(every_dig):
            sum_num += num
    sum_num = sum_num*9
   
    if card_num[-1] == str(sum_num)[-1]:
        return True

    else:
        return False

card_num = "5399830161821473" #"37562198673"
if __name__=="__main__":
	print(validate(get_cc(card_num)))