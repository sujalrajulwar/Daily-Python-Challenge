n = 19
start = 2
end = n // 2


for x in range(start, end):
    if n % x == 0:
        print(False)
    else:
        continue
print(True)
