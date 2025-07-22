#Problem Statement: Count the number of uppercase, 
# lowercase, digital and special characters in a given string.
#link ="https://www.geeksforgeeks.org/problems/count-type-of-characters3635/0"

s = "#GeeKs01fO@gEEks07"
count_upper = ""
count_lower = ""
count_digital =""
count_special_char =""

for char in s:
    if char.isupper():
        count_upper += char

    elif char.islower():
        count_lower += char 

    elif char.isdigit():
        count_digital += char
    
    else:
        count_special_char += char


print("Uppercase characters:", len(count_upper))
print("Lowercase characters:", len(count_lower))
print("Digital characters:", len(count_digital))
print("special characters:", len(count_special_char))

