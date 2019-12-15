# creating a list of items from which a user can choose

m_list = ['rice', 'milk', 'butter', 'garri']

m_list.insert(1, 'salt')

print('enter your choice:')

print(m_list)

print(' ')

v=input('your choice:')

print('')

if v==m_list[3]:
	print('wow! you chose my favourite')

elif v==m_list[2]:
	print('not bad!')

else:
	print('you\'ve made the right choice')	

print(' ')

if v == m_list[0]:
	print('What would you like to prepare it with?; Stove or gas cooker:')
	k = input('Enter the method:')
else:
	print('You won\'t undergo much stress in preparing it.')	
if k == 'gas cooker':
	print(' ')
	print('....Please be very careful while using gas cooker')
else:
     print(' ')
     print('That\'s good because that method has low risk.')
print(r'Samuel is a good\great boy')
		
