import math
import random
import datetime
import os
import time
import calendar
import turtle
import re
import string
import platform

# ===== 1. Використання math =====
try:
    num = 144
    result = math.sqrt(num)  # Обчислення квадратного кореня
    print(f"1. Квадратний корінь з {num} = {result}")
except Exception as e:
    print("Помилка в math:", e)

# ===== 2. Використання random =====
try:
    fruits = ["яблуко", "банан", "груша", "персик"]
    choice = random.choice(fruits)  # Випадковий вибір елемента
    print("2. Випадковий фрукт:", choice)
except Exception as e:
    print("Помилка в random:", e)

# ===== 3. Використання datetime =====
try:
    now = datetime.datetime.now()  # Поточна дата та час
    print("3. Поточна дата і час:", now.strftime("%d.%m.%Y %H:%M:%S"))
except Exception as e:
    print("Помилка в datetime:", e)

# ===== 4. Використання os =====
try:
    current = os.getcwd()  # Повертає шлях до поточної папки
    print("4. Поточна директорія:", current)
except Exception as e:
    print("Помилка в os:", e)

# ===== 5. Використання string =====
try:
    letters = string.ascii_lowercase  # Усі маленькі літери англійського алфавіту
    print("5. Усі малі літери англійського алфавіту:", letters)
except Exception as e:
    print("Помилка в string:", e)
