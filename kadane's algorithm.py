
def max_subarray(array):

	max_so_far = array[0]
	current_max = array[0]

	for integer in range(1,len(array)) :


		current_max = max(array[integer]+current_max , array[integer])
		max_so_far = max(max_so_far,current_max)
		

	return max_so_far


print(max_subarray([-2,-1,-3,-4,-1,-2,-1,9,1,-5,4,5,6]))
