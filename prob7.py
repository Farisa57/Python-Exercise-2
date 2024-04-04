#Write a Python function to merge two sorted lists into a single sorted list.List1 = [1, 3, 5] List2 = [2, 4, 6]

List1= [1,3,5]
List2= [2,4,6]

new_list = sorted(List1+List2)

print("The merged list is = " , new_list)