#Write a Python function to check if two given strings ("listen", "silent") are anagrams of each other (i.e., they contain the same characters but may be in a different order


s1= "listen"
s2= "silent"
if(sorted(s1)==sorted(s2)):
      print("The strings are anagrams.")
else:
      print("The strings aren't anagrams.")