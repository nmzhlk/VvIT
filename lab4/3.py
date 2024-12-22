import pack.add, pack.subtract, pack.multiply, pack.divide, pack.combine

a = int(input('Введите число A: '))
b = int(input('Введите число B: '))

print(f'Сумма A и B = {pack.add.add(a, b)}')
print(f'Разность A и B = {pack.subtract.subtract(a, b)}')
print(f'Произведение A и B = {pack.multiply.multiply(a, b)}')
print(f'Частное деления A на B = {pack.divide.divide(a, b)}')

print()

line1 = input('Введите первую строчку: ')
line2 = input('Введите вторую строчку: ')
print(f'Соединил строки: {pack.combine.combine(line1, line2)}')
