"""
Домашнее задание
Темы: слайды 30-36 - Словари (dictionaries)
"""

# ЗАДАНИЕ 1: Работа со словарями и перебор элементов

# Создайте словарь с информацией о студенте:
student_info = {
    "name": "Иван",
    "age": 20,
    "course": 2,
    "city": "Москва"
}
# 1. Выведите все ключи словаря
keys = student_info.keys()
print(keys)

# 2. Выведите все значения словаря
values = student_info.values()
print(values)

# 3. Используя цикл for, выведите все пары "ключ: значение"
for k, v in student_info.items():
    print(f"{k}: {v}")

# 4. Используя цикл for, выведите только значения словаря
for value in student_info.values():
    print(value)


# ЗАДАНИЕ 2: Удаление элементов и генератор словарей

# Дан словарь цен на фрукты:
prices = {"яблоко": 50, "банан": 30, "апельсин": 40, "груша": 35, "виноград": 60}

# 1. Удалите "груша" из словаря
del prices["груша"]
print(prices)

# 2. Удалите "виноград" и сохраните цену в переменную
grape = prices.pop("виноград")
print(grape)

# 3. Создайте новый словарь с теми же фруктами, но с ценами со скидкой 10%
prices_with_discount = {fruit: int(price*90/100) for fruit, price in prices.items()}

# 4. Выведите результат
print(prices_with_discount)


# ЗАДАНИЕ 3: Объединение словарей
# У вас есть два словаря:
student1 = {"имя": "Иван", "возраст": 20, "курс": 2}
student2 = {"имя": "Мария", "возраст": 21, "город": "Санкт-Петербург"}

# 1. Объедините student2 в student1
student1.update(student2)

# 2. Выведите результат
print(student1)

# 3. Создайте новый словарь student3, объединив оба словаря (не изменяя исходные)
student3 = student1.copy()
student3.update(student2)

# 4. Выведите все три словаря для сравнения
print(student1)
print(student2)
print(student3)
