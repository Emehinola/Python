import re

stat = '''
10, 14, 25, 29, 36, 40, 20, 18, 32
'''

x, y = 1, 10
for interval in re.findall(r'\d[x][0-9]', stat):
	print(interval)