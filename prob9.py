#Write a Python function to remove the duplicates in-place from a sorted array and return the length of the new array/list without duplicates.List = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]


list1 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

print ("The original list is : " , list1)


new_list = list(set(list1))


print ("The list after removing duplicates : " , new_list)
