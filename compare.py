def nearest(num, iterable):
	# checking if num id in iterable
	if num in iterable:
			return num
	else:
			num_sort = [num-i for i in iterable]
	return iterable[num_sort.index(max(num_sort))]
	
print(nearest(3, [5,1,4]))