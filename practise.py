# Coding Question (Attempt seriously)
# Problem

# You are given an integer N and a list of N integers.

# Your task is to find the second largest distinct element in the list.

# Input Format

# First line: integer N

# Second line: N space-separated integers

# Output Format

# Print the second largest distinct number

# If it does not exist, print -1

# Constraints

# 2 ≤ N ≤ 10⁵

# -10⁹ ≤ elements ≤ 10⁹

# Example 1

# Input

# 5
# 10 20 20 8 15


# Output

# 15

# Example 2

# Input

# 3
# 5 5 5


# Output

# -1

arr = [10, 20, 20, 8, 15]
largest = -1
second_largest = -1

for i in range(len(arr)):
    if arr[i] > largest:
        second_largest = largest
        largest = arr[i]
    else:
        print(-1)
