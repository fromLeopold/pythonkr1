list1 = [1, 3, 67, 24, 42, 23, 76, 78, 78, 23, 67, 23]
counter = 0
for i in list1:
    c = list1.count(i)
    if c >= 2:
        counter += c % 2
print(counter)