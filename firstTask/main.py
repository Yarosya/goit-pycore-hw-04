# def total_salary(path):
#     total = 0
#     count = 0
#
#     try:
#         with open(path, 'r', encoding='utf-8') as file:
#             for line in file:
#                 name, salary = line.strip().split(',')
#                 total += int(salary)
#                 count += 1
#
#         average = total / count if count > 0 else 0
#         return total, average
#
#     except FileNotFoundError:
#         print(f"Файл за шляхом {path} не знайдено.")
#         return 0, 0
#     except ValueError:
#         print("Помилка формату даних у файлі. Переконайтеся, що зарплати є числами.")
#         return total, average
#     except Exception as e:
#         print(f"Сталася помилка: {e}")
#         return total, average
#
# total, average = total_salary("/first task/salary.txt")
# print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

import os

# Отримати абсолютний шлях до файлу
file_path = os.path.abspath("./first task/salary.txt")
print(f"Абсолютний шлях до файлу: {file_path}")

# Отримати абсолютний шлях до поточного файлу (скрипту)
current_file_path = os.path.abspath(__file__)
print(f"Абсолютний шлях до поточного файлу: {current_file_path}")