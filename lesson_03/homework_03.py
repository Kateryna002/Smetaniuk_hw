alice_in_wonderland = ('''"Would you tell me, please, which way I ought to go from here?"\n
"That depends a good deal on where you want to get to," said the Cat.\n
"I don\'t much care where ——" said Alice.\n
"Then it doesn\'t matter which way you go," said the Cat.\n
"—— so long as I get somewhere," Alice added as an explanation.\n
"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."''')
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк

print (alice_in_wonderland)

"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
area_black_sea = 436402
area_azov_sea = 37800
area_amount = area_black_sea + area_azov_sea

print(f"Чорне та Азовське моря разом займають:{area_amount} км2")

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
warehouses_total = 375291
warehouse1_warehouse2_summ = 250449
warehouse2_warehouse3_summ = 222950
warehouse3 = warehouses_total - warehouse1_warehouse2_summ
warehouse2 = warehouse2_warehouse3_summ - warehouse3
warehouse1 = warehouse1_warehouse2_summ - warehouse2

print(f"На першому складі перебуває:{warehouse1} товарів")
print(f"На другому складі перебуває:{warehouse2} товарів")
print(f"На третьому складі перебуває:{warehouse3} товарів")

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
monthly_payment = 1179
payment_period = 18
nout_price = monthly_payment * payment_period

print(f"Вартість комп'ютера: {nout_price} грн")

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
a = 8019 % 8
b = 9907 % 9
c = 2789 % 5
d = 7248 % 6
e = 7128 % 5
f = 19224 % 9

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
pizza_l = 274 * 4
pizza_m = 218 * 2
juice = 35 * 4
cake = 350 * 1
water = 21 * 3
money_ammount = pizza_l + pizza_m + juice + cake + water

print(f"Знадобиться: {money_ammount} грн")

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
photos_amount = 232
page1 = 8
album_pages_total = photos_amount / page1

print(f"Потрібно: {album_pages_total} сторінок, щоб вклеїти всі фото")

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""

xarkiv_budapesht = 1600
consumption_per_100km = 9
tank_capacity = 48
liters_needed = (xarkiv_budapesht / 100) * consumption_per_100km
full_tank = liters_needed / tank_capacity
refuel_stops = (liters_needed / tank_capacity) - 1
#за умови, що спочатку поїздки бак повний

print(f"Потрібно бензину: {liters_needed} літрів")
print(f"За умови, що спочатку поїздки бак був повний, кількість заїздів на заправку: {refuel_stops}")