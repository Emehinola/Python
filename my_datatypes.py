#working on integers
v = 30
m=5
h=m*v
print(h)
#and hence determine its type
print(" ")
d=type(h)
print("Datatype of d is:")
print(d)
		#working on float-point numbers
print(" ")
k=2e0
print(k)
print(type(k))
print(736e727)
print("evaluating 5e-324")			
print(5e-324)
        #working on bases
print(" ")
print("now working on bases, i.e converting from one base to\nanother:")   
     
print('converting 10 from base_10 to 2 gives:',\
0b10)
	       #Now working on string
print(" ")
print(" ")
print("it's time to work on string")   
"""working on sting
  ...continuation"""
print("i am blessed" + " by the most high")
v="see you later"
b="when i'm back"
c=v+" "+b
print(c)

print(' ')	

"""From this place, i will be working
on arithmetical operation"""
    #To calculate the sum of the first n integers...

print("Program to sum the first n natural numbers;")

def sum_up(n):
	
	if n==1:
		return 1
	else:
		return (n+sum_up(n-1))
n = int(input("Enter a number:"))
print("The sum of the first", n, "number is", (n+sum_up(n-1)))