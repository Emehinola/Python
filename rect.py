class Rectangle:
	"Class to calculate the area of a rectangle"
	
	def __init__(self, length, breadth):
		self.length = length
		self.breadth = breadth
		
	def area(self):
		return self.length * self.breadth
		
rect = Rectangle(3,4)
print(f"The area is {rect.area()}")