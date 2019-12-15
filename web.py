import re

word = '''My phone number is 234-8131-6153-93 while my account number is 0423103459'''

phone_acct = re.findall(r'[a-z]* number', word)
#print(phone_acct)

ph_dig = re.findall(r'\d{3}-\d{4}*', word)

acc_dig = re.findall(r'\d{9,10}', word)

ph_acct = ph_dig + acc_dig
print(ph_acct)

y = 0

number_type = {}

for names in phone_acct:
	number_type[names] = ph_acct[y]
	y += 1
	
print(number_type)
