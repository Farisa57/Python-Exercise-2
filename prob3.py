#Given a list of n-1 integers from 1 to n, find the missing number in the list.List = [1, 2, 4, 6, 3, 7, 8] 





		
def find_missing(list):
	start = list[0]
	end = list[-1]
	return sorted(set(range(start, end + 1)).difference(list))


list = [1, 2, 4, 6, 3, 7, 8]
print(find_missing(list))
