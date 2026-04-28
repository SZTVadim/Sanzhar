# ЗАДАНИЕ 1: Добавление элементов в список
# 1. Добавьте "банан" в конец списка
fruits = ["яблоко"]
fruits.append("банан")
print(fruits)
# 2. Добавьте элементы ["апельсин", "груша"]
some_fruits = ["апельсин", "груша"]
fruits.extend(some_fruits)
print(fruits)
# 3. Вставьте "виноград" на позицию с индексом 1
fruits.insert(1, "виноград")
print(fruits)

# ЗАДАНИЕ 2: Удаление элементов из списка
task_2_fruits = ["яблоко", "банан", "апельсин", "банан"]
# 1. Удалите первое вхождение "банан" (remove)
task_2_fruits.remove("банан")
print(task_2_fruits)
# 2. Удалите последний элемент и сохраните его в переменную
last_fruit = task_2_fruits.pop()
print(last_fruit)

# ЗАДАНИЕ 3: Поиск элементов в списке
task_3_fruits = ["яблоко", "банан", "апельсин", "банан"]
# 1. Найдите индекс первого вхождения "банан"
index_of_banana = task_3_fruits.index("банан")
print(index_of_banana)
# 2. Посчитайте, сколько раз встречается "банан"
count_bananas = task_3_fruits.count("банан")
print(count_bananas)

# ЗАДАНИЕ 4: Сортировка и реверс списка
numbers = [3, 1, 4, 1, 5, 9, 2]
# 1. Отсортируйте список по возрастанию (sort)
numbers.sort()
print(numbers)
# 2. Переверните список (reverse)
numbers.reverse()
# 3. Выведите результат
print(numbers)

# ЗАДАНИЕ 5:
# Создайте список кубов чисел от 1 до 8 с помощью генератора списков.
numbers_in_cube = [n**3 for n in range(1, 9)]
print(numbers_in_cube)
# Затем найдите минимальное и максимальное значение в этом списке.
minimum = min(numbers_in_cube)
maximum = max(numbers_in_cube)
# Выведите оба результата.
print(minimum)
print(maximum)

# ЗАДАНИЕ 6:
task_6_numbers = [5, 12, 8, 15, 3, 20, 7, 18, 9, 11]
# С помощью генератора списков создайте новый список, содержащий только числа больше 10.
ten_list = [n for n in task_6_numbers if n > 10]
print(ten_list)
# Затем найдите сумму всех этих чисел с помощью функции sum().
summary = sum(ten_list)
# Выведите результат.
print(summary)

# ЗАДАНИЕ 7:
cities = ["москва", "санкт-петербург", "казань"]
# С помощью генератора списков создайте новый список, где каждое название начинается с заглавной буквы.
titled_cities = [n.title() for n in cities]
# Выведите результат.
print(titled_cities)
