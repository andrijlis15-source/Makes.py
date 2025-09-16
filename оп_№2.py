a = [45, 25, 3, 453, 66, 7, 52, 99, 36, 26, "кінь", "коло", "сік", "ніж", "сніг", "телефон", "ручка", "стіл", "штора", "меч"]
int_list = [i for i in a if isinstance(i, int)]
str_list = [i for i in a if isinstance(i, str)]

int_list.sort()
str_list.sort()

b = int_list + str_list

c = [i for i in int_list if i % 2 == 0]

cups = [i.upper() for i in str_list]



print("Основний список:", a)
print("Відсортований список (int по зростанню, str а-я):", b)
print("Числа кратні 2:", c)
