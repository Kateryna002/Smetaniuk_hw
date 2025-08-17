lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
lst2 = []
for char in lst1:
    if type(char) == str:
        lst2.append(char)

print(lst2)

#Або такий варіант:
#lst2 = [char for char in lst1 if type(char) == str]
#print(lst2)