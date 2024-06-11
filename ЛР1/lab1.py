# Вихляев Егор, ММТ-2

from random import randint
import math
import cmath

# Exercise 1

random_number = randint(1, 100)

while True:
    user_number = int(input("Введите загаданное число: "))

    if user_number == random_number:
        print("Вы угадали!")
        break
    elif user_number > random_number:
        print("Введенное число больше загаданного.")
    else:
        print("Введенное число меньше загаданного.")

# Exercise 2: Решение квадратного однородного (!) уравнения

a = int(input("Введите коэффициент при второй степени: "))
b = int(input("Введите коэффициент при первой степеени: "))
c = int(input("Введите коэффициент при нулевой степени: "))
discrim = math.pow(b, 2) - 4 * a * c
x_1 = (-b + cmath.sqrt(discrim)) / (
    2 * a
)  # Учитываем комплексные корни благодаря модулю cmath
x_2 = (-b - cmath.sqrt(discrim)) / (2 * a)
print("Корень x_1 = ", x_1, ", корень x_2 = ", x_2)

# Exercise 3: Иными словами, нужно найти НОД количеств игроков в обеих командах

N = int(input("Введите количество человек в команде A: "))
M = int(input("Введите количество человек в команде B: "))


def nod(a, b):  # Пишем функция, находящую НОД от двух чисел посредством рекурсии
    if b == 0:
        return a
    else:
        return nod(b, a % b)


d = nod(N, M)  # Требуемое значение d

print("Минимальное подходящее число d = ", d)


# Exercise 4: «Жадный» алгоритм

amount = int(
    input("Введите сумму, которую необходимо  снять в банкомате: ")
)  # Запращиваем сумму, которую нужно снять
exam = amount

denominations = [5000, 1000, 500, 200, 100]  # Список доступных купюр
counts = []  # Список количеств каждой купюры

for d in denominations:
    count = amount // d  # Количество каждой из купюр
    counts.append(count)  # Добавляем количество выдачи каждой купюры в отдельный список
    amount -= (
        count * d
    )  # Сумма по итогам итерации уменьшается на номинал купюры, умноженный на ее количество

if (exam - amount) != exam:
    print("Невозможно выдать требуемую сумму.")
else:
    with open("result_ex4.txt", "w") as f:
        for i, d in enumerate(denominations):
            f.write(f"{d} rubles: {counts[i]}\n")

print("Результат записан в файл result_ex4.txt.")

# Exercise 5:

N = int(input("Введите ширину помещения: "))
M = int(input("Введите длину помещения: "))

if N > 10 or M > 10:
    print("Ширина и длина помещения не должны превышать 10!")
    N = int(input("Введите ширину помещения: "))
    M = int(input("Введите длину помещения: "))

starting_x = int(input("Введите начальное положение робота по x: "))
starting_y = int(input("Введите начальное положение робота по y: "))
space = N * M

while True:
    command = input("Введите команду (N, S, W, E, X): ")

    if command == "N":
        starting_y += 1
    elif command == "S":
        starting_y -= 1
    elif command == "W":
        starting_x -= 1
    elif command == "E":
        starting_x += 1
    elif command == "X":
        break

    if starting_x < 0:
        starting_x += 1
    elif starting_x > N:
        starting_x -= 1
    elif starting_y < 0:
        starting_y += 1
    elif starting_y > M:
        starting_y -= 1

    print("Марсоход находится на позиции: ", starting_x, starting_y)

# Exercise 6:

places = {
    "спальня": {"выходы": ["ванная", "коридор"]},
    "ванная": {"выходы": ["спальня", "коридор"]},
    "кухня": {"выходы": ["коридор", "окно"]},
    "коридор": {"выходы": ["спальня", "ванная", "кухня", "наружу"]},
}

current_place = "спальня"
victory = False

while not victory:
    print(f"Вы в {current_place}")

    exits = places[current_place]["выходы"]
    command = input(f"Куда идем? \n {exits}\n")

    if command in exits:
        current_place = command
        if current_place == "наружу":
            print("Вы покинули квартиру!")
            victory = True
        elif current_place == "окно":
            print("Wasted!")
            victory = True
    else:
        print("Туда нельзя пойти!")

# Exercise 7:


def add_fractions(frac1, frac2):
    num = frac1[0] * frac2[1] + frac2[0] * frac1[1]
    den = frac1[1] * frac2[1]
    return [num, den]


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def simplify_fraction(frac):
    gcd_val = gcd(frac[0], frac[1])
    num = frac[0] // gcd_val
    den = frac[1] // gcd_val
    return [num, den]


n = int(input("Количество дробей: "))

fractions = []
for i in range(n):
    num = int(input(f"Числитель {i+1}: "))
    den = int(input(f"Знаменатель {i+1}: "))
    fractions.append([num, den])

result = fractions[0]
for i in range(1, len(fractions)):
    result = add_fractions(result, fractions[i])

result = simplify_fraction(result)

print(f"\nОтвет: {result[0]}/{result[1]}")
