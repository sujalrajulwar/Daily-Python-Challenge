# One odd Occuring
# Difficulty: BasicAccuracy: 50.53%Submissions: 88K+Points: 1

# Given an array of arr[] positive integers
# where all numbers occur even number of times except
# one number which occurs odd number of times.
# Return that number.

# Examples:

# Input:arr[] = [1, 2, 3, 2, 3, 1, 3]
# Output: 3
# Explaination: 3 occurs three times.
# Input:arr[] = [5, 7, 2, 7, 5, 2, 5]
# Output: 5
# Explaination: 5 occurs three times.

# Constraints:
# 1 ≤ arr.size() ≤ 105
# 1 ≤ arr[i] ≤ 106
# Link : "https://www.geeksforgeeks.org/problems/find-the-odd-occurence4820/1?page=1&category=Arrays&difficulty=Basic&status=unsolved&sortBy=submissions"

arr = [1, 2, 3, 2, 3, 1, 3]
occur = {}

for i in range(len(arr)):
    if arr[i] in occur:
        occur[arr[i]] += 1
    else:
        occur[arr[i]] = 1

for key, val in occur.items():
    if val % 2 != 0:
        print(key)
    else:
        continue
