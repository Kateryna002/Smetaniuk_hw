my_list = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]

def char_summ(lst):
    result = []
    for item in lst:
        try:
            parts = item.split(",")
            digits = [int(element) for element in parts]
            result.append(sum(digits))
        except ValueError:
            print(f"Не можу обробити '{item}'!")
    return result

print(char_summ(my_list))
