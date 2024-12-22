import my_module

print(my_module.add(38, 14))  # 38 + 14 = 52
print(my_module.subtract(125, 177))  # 125 - 177 = -52

print()
a = int(input('Введите число A: '))
b = int(input('Введите число B: '))

print(f'Сумма A и B = {my_module.add(a, b)}')
print(f'Разность A и B = {my_module.subtract(a, b)}')
