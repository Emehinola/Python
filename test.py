import re

def div(x,y):
	assert (y!=0), "Zero division error"
	return x/y
	
#print(div(2,8))

def div(a,b):
	try:
		return a/b
	except Exception as Argument:
		return f"{Argument}"
		
#print(div(1,0))

def get(age):
	if age < 9:
		raise Exception(age)
		
	return age
	
#try:
#	re = get(6)
	#print(re)
	
#except Exception as e:
	#print("error in handling age", e.args[0])
	
def lol(li):
	return [
		list(row) for row in zip(*li)
	]

l = [['a','b','d'],['d','e','f'],['g','h','i']]
#print(lol(l))

fun = {
'a':23,
'b':43
}

#result = f"{a}*{b}".format(**fun)
#print(result)

w = "Samie is good"
if re.search(r"\n", w):
	print("It exists")
else:
	print("Does not exist")
	