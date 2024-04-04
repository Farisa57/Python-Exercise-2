#Write a Python function to count the occurrences of each element in a list and return a dictionary with the counts.List = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

def occurence(x):
    counts = {}

    for item in x:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1

        return counts
    
    occurence([1,2,2,3,3,3,4,4,4,4])
    print(occurence)

