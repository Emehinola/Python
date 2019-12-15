#Codes to convert numbers from millimetre and metres to centimetre

def conversion(cent):
	
	metres = int(cent*100)
	
	milli_metre = int(cent/10)
	
	print(cent, "cm gives", metres, "m")
	print(cent, "cm gives", milli_metre, "mm")

cent = int(input("Enter the no:"))

conversion(cent)
	