list1 = [45, 46, 346, 36, 645, 456, 36, 879, 7, 849, 98, 90]
list2 = [15, 46, 5, 7, 67, 15, 456, 46, 78, 90, 7, 45]
set1 = set(list1)
set2 = set(list2)
list3 = list(set2.intersection(set1))
lenset = len(list3)
print(f'{lenset} общих элементов: {list3}')