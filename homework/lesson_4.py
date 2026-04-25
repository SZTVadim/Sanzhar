print("Task 1: Работа с типами данных")
task_1_string = "Привет"
task_1_int = 42
task_1_float = 3.14
task_1_list = [1, 2, 3]
print(type(task_1_string))
print(type(task_1_int))
print(type(task_1_float))
print(type(task_1_list))

print("\nTask 2: Преобразование регистра строк")
task_2_python = "python PROGRAMMING"
print(task_2_python.lower())
print(task_2_python.upper())
print(task_2_python.title())
print(task_2_python.capitalize())

print("\nTask 3: Удаление пробелов")
task_3_spaces = "  Hello World  "
print(task_3_spaces.strip())
print(task_3_spaces.lstrip())
print(task_3_spaces.rstrip())

print("\nTask 4: Разделение и объединение строк")
task_4_string = "яблоко,банан,апельсин,груша"
task_4_list = task_4_string.split(",")
print(task_4_string.split(','))
print(" | ".join(task_4_list))

print("\nTask 5: Замена подстрок")
task_5_replace = "Я изучаю Python. Python - это круто!"
print(task_5_replace.replace("Python", "Java"))

print("\nTask 6: Поиск и подсчет")
task_6_count = "Python программирование на Python"
print(task_6_count.find("Python"))
print(task_6_count.count("Python"))
print(task_6_count.find("Java"))

print("\nTask 7: Проверка типа символов")
print("Hello123".isalnum())
print("12345".isdigit())
print("Hello".isalpha())
print("   ".isspace())

print("\nTask 8: Срезы строк")
task_8 = "Python very good"
print(task_8[:3])
print(task_8[-3:])
print(task_8[::2])
print(task_8[::-1])

print("\nTask 9: Экранирование символов")
print("Он сказал: \"Привет\"")
print("Первая строка\nВторая строка")
