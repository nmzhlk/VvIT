class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def set_radius(self, new_radius):
        self.radius = new_radius


kroog = Circle(2)  # Создаем объект с радиусом 2
print(kroog.get_radius())  # Выведем текущий радиус

kroog.set_radius(1000)  # Изменим радиус на 1000
print(kroog.get_radius())  # Выведем измененный радиус
