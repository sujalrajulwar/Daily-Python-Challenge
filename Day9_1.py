# Given an array arr, the task is to find whether the arr is palindrome or not. If the arr is palindrome then return true else return false.

# An array is said to be palindrome if its reverse array matches the original array.

# Examples:

# Input: arr = [1, 2, 3, 2, 1]
# Output: true
# Explanation: Here we can see we have [1, 2, 3, 2, 1] if we reverse it we can find [1, 2, 3, 2, 1] which is the same as before. So, the answer is true.
# Input: arr = [1, 2, 3, 4, 5]
# Output: false
# Explanation: Here we can see we have [1, 2, 3, 4, 5] if we reverse it we find [5, 4, 3, 2, 1] which is the not same as before. So, the answer false.
# Link = https://www.geeksforgeeks.org/problems/perfect-arrays4645/0
arr = [1, 2, 3, 2, 1, 5, 5, 6, 6, 7, 8, 10]

i = 0
j = len(arr) - 1
arr1 = arr.copy()
while i < j:
    arr1[i], arr1[j] = arr1[j], arr1[i]
    i += 1
    j -= 1
if arr1 == arr:
    print("Palindrome")
else:
    print("Not Palindrome")
