# В вашем репозитории уже есть файл data_test/application.log.
#
# Напишите функцию, которая принимает тип записи ("ERROR", "WARNING", "INFO"),
# открывает файл через with open(...),
# построчно читает его и выводит только строки с переданным типом.
# Для проверки вызовите find_log_entries("ERROR").

def find_log_entries(key_word):
    with open('../data_test/application.log', 'r') as message:
        for i in message:
            if key_word in i:
                print(i)


find_log_entries("ERROR")
