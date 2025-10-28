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

try:
    num = 144
    result = math.sqrt(num)  
    print(f"1. Квадратний корінь з {num} = {result}")
except Exception as e:
    print("Помилка в math:", e)

try:
    fruits = ["яблуко", "банан", "груша", "персик"]
    choice = random.choice(fruits)  
    print("2. Випадковий фрукт:", choice)
except Exception as e:
    print("Помилка в random:", e)

try:
    now = datetime.datetime.now() 
    print("3. Поточна дата і час:", now.strftime("%d.%m.%Y %H:%M:%S"))
except Exception as e:
    print("Помилка в datetime:", e)

try:
    current = os.getcwd() 
    print("4. Поточна директорія:", current)
except Exception as e:
    print("Помилка в os:", e)

try:
    letters = string.ascii_lowercase
    print("5. Усі малі літери англійського алфавіту:", letters)
except Exception as e:
    print("Помилка в string:", e)
