# ЗАДАНИЕ 1: Работа с множествами
# Дано множество фруктов:
fruits = {"яблоко", "банан"}

# 1. Добавьте "апельсин" в множество
fruits.add("апельсин")

# 2. Добавьте несколько элементов ["груша", "виноград"] используя update()
fruits_list = ["груша", "виноград"]
fruits.update(fruits_list)

# 3. Удалите "банан" используя discard()
fruits.discard("банан")

# 4. Попробуйте удалить "киви" используя discard() (элемента нет в множестве)
fruits.discard("киви")
print(fruits)

# 5. Попробуйте удалить "киви" используя remove() (элемента нет в множестве) - закомментируйте эту строку
# fruits.remove("киви")

# 6. Удалите и сохраните произвольный элемент используя pop()
random_fruit = fruits.pop()
# 7. Выведите результат
print(random_fruit)


# ЗАДАНИЕ 2: Работа с кортежами
# Дано:
coordinates = (10, 20, 30, 20, 10, 20, 40)

# 1. Выведите первый элемент кортежа
first = coordinates[0]
print(first)

# 2. Выведите последний элемент кортежа
last = coordinates[-1]
print(last)

# 3. Выведите срез с 2-го по 4-й элемент (включительно)
two_2_four = coordinates[1:4]
print(two_2_four)

# 4. Проверьте, есть ли число 30 в кортеже (используйте оператор in)
thirty = 30 in coordinates
print(thirty)

# 5. Найдите индекс первого вхождения числа 20
index_20 = coordinates.index(20)
print(index_20)

# 6. Подсчитайте, сколько раз встречается число 20
count_20 = coordinates.count(20)
print(count_20)

# 7. Подсчитайте, сколько раз встречается число 50 (его нет в кортеже)
count_50 = coordinates.count(50)
print(count_50)

# 8. Выведите длину кортежа
length = len(coordinates)
print(length)


# ЗАДАНИЕ 3: Операции с кортежами

# Дано:
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
numbers = [10, 20, 30, 40, 50]

# 1. Объедините tuple1 и tuple2 в один кортеж
tuples = tuple1 + tuple2
print(tuples)

# 2. Создайте кортеж, где элементы tuple1 повторяются 3 раза
triple_tuple = tuple1 * 3
print(triple_tuple)

# 3. Распакуйте tuple1 в три переменные a, b, c
a, b, c = tuple1
print(a)
print(b)
print(c)

# 4. Распакуйте numbers (преобразовав в кортеж) так, чтобы:
#    - первый элемент был в переменной first
#    - последний элемент был в переменной last
#    - все средние элементы были в списке middle
first, *middle, last = numbers
print(first)
print(middle)
print(last)

# 5. Преобразуйте список numbers в кортеж
tuple_numbers = tuple(numbers)
print(type(tuple_numbers))

# 6. Создайте кортеж из четных чисел от 0 до 10 (используйте генератор)
countable_tuple = tuple(n for n in range(0, 11) if n % 2 == 0)
print(countable_tuple)

# 7. Создайте кортеж квадратов чисел от 1 до 5 (используйте генератор)
square_tuple = tuple(n ** 2 for n in range(1, 6))
print(square_tuple)

# 8. Создайте кортеж из одного элемента со значением 42
tuple_one = (42,)
print(tuple_one)
