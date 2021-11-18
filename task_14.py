str1 = input('Enter: ')
list1 = str1.split()
for i in list1:
    if i.isdigit():
        print(i)
