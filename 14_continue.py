count = 0
i = 1

while count < 100:
    if i % 7 == 0:
        i += 1
        continue
    
    print(i, end=" ")
    count += 1
    i += 1