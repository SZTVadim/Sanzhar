# Домашнее задание: Декораторы, @property и @classmethod
#
# ЗАДАНИЕ 1: Декоратор
# 1) Создайте декоратор log_execution:
#    - Декоратор должен выводить "Функция запущена" перед выполнением функции
#    - Выполнять саму функцию
#    - Выводить "Функция завершена" после выполнения функции
def log_execution(func):
    def wrapper(*args, **kwargs):
        print("Функция запущена")

        f = func(*args, **kwargs)
        print(f)

        print("Функция завершена")
        return f
    return wrapper

# 2) Примените декоратор к функции calculate_sum(a, b):
#    - Функция должна возвращать сумму двух чисел
#    - Используйте синтаксис @log_execution


@log_execution
def calculate_sum(a, b):
    return a + b


# 3) Вызовите функцию calculate_sum(5, 3) и посмотрите результат
calculate_sum(5, 3)


# ЗАДАНИЕ 2: @property и @classmethod
#
# Cоздайте класс Book (Книга):
# 1) В __init__ принимайте: title (название), author (автор)
#    - Создайте приватный атрибут __price (цена), инициализируйте значением 0
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.__price = 0

# 2) Создайте @property для price:
#    - Геттер должен возвращать __price
#    - Сеттер должен проверять: если цена < 0,
    #    выводить "Ошибка: цена не может быть отрицательной!"
#    - Сеттер должен проверять: если цена > 10000,
    #    выводить "Ошибка: максимальная цена 10000 рублей!"
#    - Иначе устанавливать значение
    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            print("Ошибка: цена не может быть отрицательной!")
        elif value > 10000:
            print("Ошибка: максимальная цена 10000 рублей!")
        else:
            self.__price = value

# 3) Создайте @classmethod create_from_string:
#    - Принимает строку в формате "Название|Автор"
    #    (например, "Война и мир|Толстой")
#    - Разделяет строку и создает объект Book
#    - Возвращает созданный объект
    @classmethod
    def create_from_string(cls, string):
        title, author = string.split('|')
        return cls(title, author)

# 4) Создайте обычный метод get_info:
#    - Возвращает строку: "Книга '{title}' автор {author}, цена {price} руб."
    def get_info(self):
        return f'Книга {self.title} автор {self.author}, цена {self.price} руб'


# 5) Использование:
#    - Создайте книгу обычным способом:
    #    book1 = Book("1984", "Оруэлл")
#    - Создайте книгу через @classmethod:
    #    book2 = Book.create_from_string("Мастер и Маргарита|Булгаков")
#    - Установите цены: book1.price = 500, book2.price = 750
#    - Попробуйте установить неверную цену:
    #    book1.price = -100, book1.price = 15000
#    - Выведите информацию о книгах через get_info() через print
book1 = Book("1984", "Оруелл")
book2 = Book.create_from_string("Мастер и Маргарита|Булгаков")
book1.price = 500
book2.price = 750
book1.price = -100
book1.price = 15000
print(book1.get_info())
print(book2.get_info())
