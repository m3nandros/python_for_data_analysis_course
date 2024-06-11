# Вихляев Егор, ММТ-2

# Exercise 1:
input_numbers = input("Введите список чисел (каждое число через пробел): ")
numbers = input_numbers.split()
numbers = [int(num) for num in numbers]
print("Numbers: ", numbers)
even_numbers = []


def even(numbers):
    for num in numbers:
        if num % 2 == 0 and num > 10:
            even_numbers.append(num)
    return even_numbers


print("Even numbers: ", even(numbers))

# Exercise 2:
input_string = input("Введите строку: ")


def space_number(string):
    count = 0
    for ch in string:
        if ch == " ":
            count += 1

    if count % 2 == 0:
        print("Четное число.")
    else:
        print("Нечетное число.")


print(space_number(input_string))

# Exercise 3:
input_numbers_ex3 = input("Введите список чисел (каждое число через пробел): ")
numbers = input_numbers_ex3.split()
numbers = [int(num) for num in numbers]
print("Numbers: ", numbers)


def mean(numbers):
    if numbers == []:
        return 0
    else:
        count = 0
        summ = 0
        for num in numbers:
            count += 1
            summ += num
        return summ / count


print("Среднее значения элементов списка: ", mean(numbers))

# Exercise 4:
input_numbers_ex4 = input("Введите список чисел (каждое число через пробел): ")
numbers = input_numbers_ex4.split()
numbers = [int(num) for num in numbers]
print("Numbers: ", numbers)


def summ_and_product(numbers):
    if numbers == []:
        return 0
    else:
        summ = 0
        product = 1
        for num in numbers:
            summ += num
            product *= num
        return summ, product


print(
    "Сумма и произведение элементов списка соответственно: ", summ_and_product(numbers)
)

# Exercise 5:
input_sides = input("Введите список длин отрезков: ")
sides = input_sides.split()
sides = [int(num) for num in sides]
print("Длины сторон: ", sides)


def triangle_exam(sides):
    if len(sides) != 3:
        print("Длин отрезков должно быть 3!")
        exit()
    elif len(sides) == 3:
        if (
            sides[0] + sides[1] > sides[2]
            and sides[0] + sides[2] > sides[1]
            and sides[1] + sides[2] > sides[0]
        ):
            return "Это треугольник."
        else:
            return "Это не треугольник."


print(triangle_exam(sides))

# Exercise 6:
phrases = ["Cogito ergo sum", "Per aspera ad astra", "Alea iacta est"]


def print_or_add(phrase):
    if phrase in phrases:
        print(phrase)
    else:
        phrases.append(phrase)
        print("Фраза добавлена в список!")


while True:
    phrase = input("Введите фразу: ")
    print_or_add(phrase)

# Exercise 7:
string_input_ex7 = input("Введите строку: ")


def register(string):
    count_upper = 0
    count_lower = 0
    for ch in string:
        if ch.isupper() == True:
            count_upper += 1
        elif ch.islower() == True:
            count_lower += 1
    return count_upper, count_lower


print(
    "Количество букв верхнего и нижнего регистров соответственно: ",
    register(string_input_ex7),
)

# Exercise 8:
day_data = input("Введите номер дня недели и язык через пробел: ").split()
day_num = int(day_data[0])
lang = day_data[1]


def day_of_the_week(day_data):
    day_num, lang = day_data
    days_ru = [
        "Понедельник",
        "Вторник",
        "Среда",
        "Четверг",
        "Пятница",
        "Суббота",
        "Воскресенье",
    ]
    days_en = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]

    if lang == "русский":
        return days_ru[day_num - 1]
    elif lang == "английский":
        return days_en[day_num - 1]
    else:
        return "Неизвестный язык"


print(day_of_the_week([day_num, lang]))
