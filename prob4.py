#Write a Python function to count the number of vowels and consonants in a given string "Hello World"

x = ("Hello World")
vowels = 0
consonants = 0
x.lower()

for i in x:
    if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
        vowels = vowels + 1
    else:
        consonants = consonants + 1
 
print("Total Number of Vowels in this String = ", vowels)
print("Total Number of Consonants in this String = ", consonants)
