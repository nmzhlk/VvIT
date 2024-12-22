class Employee:
    def __init__(self, name, id, **kwargs):
        self.name = name
        self.id = id
        super().__init__(**kwargs)

    def get_info(self):
        return f'Сотрудник {self.name} с идентификатором {self.id}.'


class Manager(Employee):
    def __init__(self, name, id, department, **kwargs):
        super().__init__(name=name, id=id, **kwargs)
        self.department = department

    def manage_project(self):
        return f'Менеджер {self.name} работает над проектом в департаменте {self.department}.'

    def get_info(self):
        base_info = super().get_info()
        return f'{base_info} Он менеджер в департаменте {self.department}.'


class Technician(Employee):
    def __init__(self, name, id, specialization, **kwargs):
        super().__init__(name=name, id=id, **kwargs)
        self.specialization = specialization

    def perform_maintenance(self):
        return f'Техник {self.name} проводит техническое обслуживание по специализации {self.specialization}.'

    def get_info(self):
        base_info = super().get_info()
        return f'{base_info} Техническая специализация: {self.specialization}.'


class TechManager(Manager, Technician):
    def __init__(self, name, id, department, specialization, **kwargs):
        super().__init__(name=name, id=id, department=department, specialization=specialization, **kwargs)
        self.team = set()

    def add_employee(self, employee):
        self.team.add(employee)
        return f'Сотрудник {employee.name} добавлен в команду {self.name}.'

    def get_team_info(self):
        team = f'Команда сотрудника {self.name}:\n'
        for employee in self.team:
            team += f'- {employee.get_info()}\n'
        return team

    def get_info(self):
        base_info = super().get_info()
        return f'{base_info} Это технический менеджер.'



employee = Employee('Антон', 1)
manager = Manager('Андрей', 2, 'HR')
technician = Technician('Алексей', 3, 'Электрик')
tech_manager = TechManager('Александр', 4, 'ИТ', 'Системное администрирование')

print(employee.get_info())
print()

print(manager.get_info())
print(manager.manage_project())
print()

print(technician.get_info())
print(technician.perform_maintenance())
print()

print(tech_manager.get_info())
print(tech_manager.manage_project())
print(tech_manager.perform_maintenance())
print()

tech_manager.add_employee(employee)
tech_manager.add_employee(manager)
tech_manager.add_employee(technician)
print(tech_manager.get_team_info())
