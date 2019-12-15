import re

word = '''My phone number is 234-8131-6153-93 while my account number is 0423103459'''

phone_acct = re.findall(r'[a-z]* number', word)
#print(phone_acct)

ph_ac_dig = re.findall(r'\d{3}{2,4}* \d[9-10]', word)