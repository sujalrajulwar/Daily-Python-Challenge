# Given a list of characters, merge all of them into a string.

# Example 1:

# Input:
# N = 13
# Char array = g e e k s f o r g e e k s
# Output: geeksforgeeks
# Explanation: combined all the characters
# to form a single string.

# Example 2:

# Input:
# N = 4
# Char array = e e b a
# Output: eeba
# Explanation: combined all the characters
# to form a single string.


# Your Task:
# You dont need to read input or print anything. Complete the function chartostr() which accepts a char array arr and its size  N  as parameter and returns a string.
# Link : "https://www.geeksforgeeks.org/problems/convert-a-list-of-characters-into-a-string5142/0"

array = "g e e k s f o r g e e k s"
new_arr = array.split(" ")
new_arr_1 = "".join(new_arr)
print(new_arr_1)
