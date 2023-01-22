"""import random
#
msg = "Бросаем кости... "
cube1 = random.randint(1,6)
cube2 = random.randint(1,6)
#
#
name = type(msg)
print(name)
print(msg, cube1, cube2)"""


import random


print("\nПривет, укажите диапазон цифр, а я выберу случайное число.")
start = int(input("Начальное число: "))
finish = int(input('Финальное число: '))

number = random.randint(start,finish)

# Высчитываем сколько попыток необходимо
lenth = finish - start
count = 0
while True:
    count = count + 1
    lenth = int(lenth / 2)
    if lenth <= 1:
        print(f"Ты станешь чемпионом, если угадаешь с {count} попытки!\n")
        break

attempt = 0
number_list = []
print('Ваше число: ', end=' ')
user_num = int(input())

while True:
    attempt = attempt + 1
    if user_num == number:
        number_list.append(number)
        number_list.sort()
        if attempt <= count:
            print(f"\n\tПобедитель! Цель: {number}")
            print(f"\tУгадал с {attempt} попытки!")
            print('\tВаши удары: ', *number_list)
        else:
            print(f"\n\tСправился, но с {attempt} попытки и мой пёс справится :)")
        break
    else:
        number_list.append(number)
        number_list.append(user_num)
        number_list.sort()

        target_index = number_list.index(number)
        number_list[target_index] = "???"

        print('Попадите в цель:',*number_list, '\n')
        number_list.remove("???")
        print('Ваше число: ', end=' ')
        user_num = int(input())
