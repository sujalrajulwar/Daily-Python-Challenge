# Given an array arr[]. The task is to find the largest element and return it.

# Examples:

# Input: arr[] = [1, 8, 7, 56, 90]
# Output: 90
# Explanation: The largest element of the given array is 90.
# Input: arr[] = [5, 5, 5, 5]
# Output: 5
# Explanation: The largest element of the given array is 5.
# Input: arr[] = [10]
# Output: 10
# Explanation: There is only one element which is the largest.

# Link: "https://www.geeksforgeeks.org/problems/largest-element-in-array4009/0"

arr = [1, 8, 7, 56, 90]
ans = float('-inf')  # Initialize to negative infinity

for i in range(len(arr)):

    if arr[i] > ans:
        ans = arr[i]
    else:
        continue
       
    
print(ans)