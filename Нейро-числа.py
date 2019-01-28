# Распознование цифр в поле 3х3

# Задаём стандартное написание цифр от 0 до 9
import random

num0 = list('111101101101111')
num1 = list('001001001001001')
num2 = list('111001111100111')
num3 = list('111001111001111')
num4 = list('101101111001001')
num5 = list('111100111001111')
num6 = list('111100111101111')
num7 = list('111001001001001')
num8 = list('111101111101111')
num9 = list('111101111001111')

# И объединим их в массив
nums = [num0, num1, num2, num3, num4, num5, num6, num7, num8, num9]

# Добавим искажённое написание цифры 5 для примера распознавания
num51 = list('111100111000111')
num52 = list('111100010001111')
num53 = list('111100011001111')
num54 = list('110100111001111')
num55 = list('110100111001011')
num56 = list('111100101001111')

# Добавим начальные веса в сеть
weights = [0 for i in range(15)]

# Установим порог при котором активируется функция
bias = 7


# Простейшая функция, которая считает взвешенную сумму и сравнивает с порогом (Или единичный шаг работы сети)
def proceed(number):
    net = 0
    for i in range(15):
        net += int(number[i]) * weights[i]

    return net >= bias  # Если превышен порог, то сеть будет думать что искажённая цифра - 5, если нет - другая.


# Вспомогательная функция, которая уменьшит значине весов, если сеть ошиблась
def decrease(number):
    for i in range(15):
        if int(number[i]) == 1:
            weights[i] -= 1


# Ещё одна вспомогательная функция, для случаев если сеть не смогла распознать цифру 5
def increase(number):
    for i in range(15):
        if int(number[i]) == 1:
            weights[i] += 1


# Настало время тренировать нашу сеть, целых 10 тысяч раз
for i in range(10000):
    option = random.randint(0, 9)  # Берём случайное число от 0 до 9

    if option != 5:  # Если выпадает не цифра 5
        if proceed(nums[option]):  # Если сеть нашла пятёрку, которой нет
            decrease(nums[option])  # То наказываем её

    else:
        if not proceed(num5):  # Если сеть не увидела пятерку, хотя она есть
            increase(num5)  # То говорим, что "Вот она пятёрка же"

# Но как понять что сеть научилась? Надо вывести результаты
# Сначала выведем значения весов
print(weights)

# Затем прогоним по обучающей выборке
print("0 это 5? ", proceed(num0))
print("1 это 5? ", proceed(num1))
print("2 это 5? ", proceed(num2))
print("3 это 5? ", proceed(num3))
print("4 это 5? ", proceed(num4))
print("6 это 5? ", proceed(num6))
print("7 это 5? ", proceed(num7))
print("8 это 5? ", proceed(num8))
print("9 это 5? ", proceed(num9), '\n')

# И прогон по тестоваой выборке
print("Узнал 5? ", proceed(num5))
print("Узнал 5 - 1? ", proceed(num51))
print("Узнал 5 - 2? ", proceed(num52))
print("Узнал 5 - 3? ", proceed(num53))
print("Узнал 5 - 4? ", proceed(num54))
print("Узнал 5 - 5? ", proceed(num55))
print("Узнал 5 - 6? ", proceed(num56))