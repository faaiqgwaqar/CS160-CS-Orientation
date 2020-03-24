def smallest (arr):
#function definition is created using an array as part
	min = arr[i]
	#sets storage of vars in array in 'min'
	for i in range(len(arr)):
	#a for loop is created that takes i (info in array), and spreads its range out to be seen
		if min > arr[i]:
		#creates a conditional that defines if min is less than the array value
			min = arr[i]
			#then it is equal to the value min
	return min
#the value is returned
