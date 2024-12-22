import datetime
import math

print(math.sqrt(int(input('Введите число, а я посчитаю его квадратный корень: '))))

now = datetime.datetime.now()
print(f'Текущее время: {now.hour}:{now.minute}')
print(f'Дата: {now.day}.{now.month}.{now.year}')
