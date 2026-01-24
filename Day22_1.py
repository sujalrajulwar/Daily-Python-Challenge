# Given a string s, check if it is a "Panagram" or not.
# Return true if the string is a Panagram, else return false.
# A "Panagram" is a sentence containing every letter in the English Alphabet
# either in lowercase or Uppercase.

# Examples:

# Input: s = "Bawds jog, flick quartz, vex nymph"
# Output: true
# Explanation: In the given string,
# there are all the letters of the English alphabet. Hence,
# the output is true.
# Input: s = "sdfs"
# Output: false
# Explanation: In the given string, there aren't all the letters
# present in the English alphabet. Hence, the output is false.

s = "Bawds jog, flick quartz, vex nymph"
arr = [0] * 26
s = s.lower()

for char in s:
    if char.isalpha():
        arr[ord(char) - 97] += 1

is_pangram = True
for count in arr:
    if count == 0:
        is_pangram = False
        break

print(is_pangram)
