class Vehicle:
    def __init__(self):
        self.make = ''
        self.model = ''

    def get_info(self):
        return f'Это транспортное средство марки {self.make}, модель: {self.model}'


class Car(Vehicle):
    def __init__(self):
        super().__init__()
        self.fuel_type = ''

    def get_info(self):
        return (f'Это транспортное средство марки {self.make}, модель: {self.model}.\n'
                f'Работает на топливе: {self.fuel_type}.')


ts = Vehicle()
print(ts.make, ts.model, '← Тут пусто')
ts.make, ts.model = 'КамАЗ', '6282 / Это электробус.'
print(ts.get_info())

car = Car()
print(car.make, car.model, car.fuel_type, '← Тут пусто')
car.make, car.model, car.fuel_type = 'Лада', 'Гранта', 'Бензин'
print(car.get_info())

# Выше показана ОЧЕНЬ ПЛОХАЯ практика: изменять атрибуты объекта класса напрямую не стоит.