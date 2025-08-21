my_string = input("give me a number \n")
char_in_set = len(set(my_string))
if char_in_set > 10:
    print("True")
else:
    print("False")

#Або такий варіант:
#print(len(set(input("give me a number \n"))) > 10)
