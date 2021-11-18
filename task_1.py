my_list = [1, 'piu', 'cat', 'amene', 1, 54, 54, 1, 'amene']
my_list2 = []
for i in my_list:
    if my_list.count(i) == 1:
        my_list2.append(i)
print(my_list2)
