# Вихляев Егор, ММТ-2
import random
import re

# Exercise 1: Хотя бы два способа

# Способ 1
user_string = input("Введите строку: ")
print(user_string[0], user_string[-1])

# Способ 2
char_list = list(user_string)
print(char_list[0], char_list[-1])

# Exercise 2:
num_1 = float(input("Number 1: "))
num_2 = float(input("Number 2: "))

print(f"{num_1} * {num_2} = ", num_1 * num_2)


# Exercise 3:
# Способ 1
user_string_ex3 = input("Введите строку: ")
print(user_string_ex3[:2] + user_string_ex3[-2:])

# Способ 2
# Exercise 4:
# Способ 1
years_list = [2003, 2004, 2005, 2006, 2007, 2008]

# Способ 2
year_list_2 = []

for i in range(6):
    year_list_2.append(2003 + i)

print(year_list_2)

# Exercise 5:
print(year_list_2[3])

# Exercise 6:
things = ["mozzarella", "cinderella", "salmonella"]
print(things[1].upper(), things)  # В таком случае список не изменяется
things[1] = things[
    1
].upper()  # В случае присваивания элементу индекса этот же элемент в верхнем регистре -- список изменится
print(things)

# Exercise 7:

things.remove("salmonella")
print("Список без salmonella: ", things)

# Exercise 8:
values = [x for x in range(15)]
print(values)

# Exercise 9:
list_ex9 = [random.randint(0, 140) for i in range(10)]
print(list_ex9)
list_ex9_evens = list(filter(lambda x: x % 2 == 0, list_ex9))
print(list_ex9_evens)

# Exercise 10:
nums = [random.randint(0, 100) for i in range(10)]
print("Nums: ", nums)
new_nums = []

for i in range(1, len(nums)):
    if nums[i] > nums[i - 1]:
        new_nums.append(nums[i])

print("New nums: ", new_nums)

# Exercise 11:
num1 = int(input("Число 1: "))
num2 = int(input("Число 2: "))


def multiplication(a, b):
    if a % 2 == 0 and b % 2 == 0:
        return a * b
    else:
        print("Либо каждое из чисел, либо оба не являются четными!")


print(multiplication(num1, num2))

# Exercise 12:

string_ex12 = "Data Analysis"
print(string_ex12)
words = string_ex12.split()
words = [words[1], words[0]]
string_ex12 = " ".join(words)
print(string_ex12)

"""
# Exercise 13: Решение №1
nums_ex13 = input("Введите список чисел (через пробел): ").split()
unique_numbers = set(nums_ex13)  # Множество содержит только уникальные элементы
count = len(unique_numbers)
print(f"В списке встречается {count} различных чисел.")
"""

# Exercise 13: Решение №2
nums_ex13 = input("Введите список чисел (через пробел): ").split()
nums_ex13 = [int(x) for x in nums_ex13]  # Переводим «строковые» числа в «нормальные»

unique_numbers = []
for number in nums_ex13:
    if number not in unique_numbers:
        unique_numbers.append(number)

print(f"В списке {len(unique_numbers)} различных чисел.")

# Exercise 14:
word = input("Введите слово: ")
count_word = len(word)
reversed_word = word[::-1]

if reversed_word == word:
    print("Введеное слово является палиндромом!")
else:
    print("Введенное слово не является палиндромом!")

# Exercise 15:
nums_ex15 = []

while True:
    value = input("Введите число или 'stop': ")
    if value == "stop":
        break

    nums_ex15.append(float(value))

total = 0
for num in nums_ex15:
    total += num

print("Введенный список чисел: ", nums_ex15)
print("Сумма чисел в списке: ", total)

# Exercise 16:
string_ex16 = input("Введите строку: ")
words_ex16 = string_ex16.split()


new_words_ex16 = []
for word in words_ex16:
    new_words_ex16.append(word[0].upper() + word[1:])

new_string_ex16 = " ".join(new_words_ex16)
print(new_string_ex16)

# Exercise 17:
packed = input("Введите сжатую строку: ")

# Используем регулярное выражение для разбивки строки на буквы и числа
parts = re.findall(r"(\d+)([A-Z])|([A-Z])", packed)

# Собираем распакованную строку
unpacked = ""
for count, letter, single in parts:
    if single:
        unpacked += single
    else:
        unpacked += int(count) * letter

print(unpacked)

# Exercise 18:
char_amount = int(input("Количество символов: "))


def gen_pass(length):
    characters = (
        "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*_-."
    )
    password = ""
    for i in range(length):
        password += random.choice(characters)
    return password


print(f"Сгенерированный пароль из {char_amount} символов:", gen_pass(char_amount))

# Exercise 19:

user_pass = input("Введите пароль: ")
digits = "1234567890"
lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special = "!@#$%^&*()-+"

length_valid = len(user_pass) >= 12
digit_valid = False
lower_valid = False
upper_valid = False
special_valid = False

for ch in user_pass:
    if ch in digits:
        digit_valid = True
    elif ch in lowercase:
        lower_valid = True
    elif ch in uppercase:
        upper_valid = True
    elif ch in special:
        special_valid = True

valid = length_valid and digit_valid and lower_valid and upper_valid and special_valid

if valid == True:
    print("Пароль надежный!")
else:
    print("Пароль ненадежный!")
    if length_valid == False:
        print("Длина пароля должна быть не менее 12 символов!")
    if digit_valid == False:
        print("Пароль должен содержать хотя бы одну цифру!")
    if lower_valid == False:
        print("Пароль должен содержать хотя бы один символ нижнего регистра!")
    if upper_valid == False:
        print("Пароль должег содержать хотя бы один символ верхнего регистра!")
    if special_valid == False:
        print("Пароль должен содержать хотя бы один специальный символ!")
