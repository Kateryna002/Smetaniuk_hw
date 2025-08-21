my_list = list(range(100))
total = 0
for i in my_list:
    if i % 2 == 0:
        total += i

print(total)

#Або: total = sum(i for i in my_list if i % 2 == 0)
