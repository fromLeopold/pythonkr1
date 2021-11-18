str1 = 'An apple a day keeps the doctor away'
tuple1 = tuple(str1)
dict1 = {}
for i in tuple1:
    dict1[i] = tuple1.count(i)
print(dict1)