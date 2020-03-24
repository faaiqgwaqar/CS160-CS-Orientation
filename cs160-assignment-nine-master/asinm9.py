def bubblesort(nums):
	if (len(nums)<2):
		return nums 
	else:
		for i in range (0,len(nums)-1):
			for j in range(0,len(nums)-i-1):
				if nums[j]>nums[j+1]:
					temp = nums [j]
					nums[j] = nums[j+1]
					nums[j+1] = temp
		return nums
