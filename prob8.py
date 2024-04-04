#Write a Python function to find all duplicate elements in a list and return them in a new list. List = [1, 2, 3, 2, 4, 5, 4, 6]


from collections import Counter


list1 = [1, 2, 3, 2, 4, 5, 4, 6]
d = Counter(list1)
 
new_list = list([item for item in d if d[item]>1])
print(new_list)