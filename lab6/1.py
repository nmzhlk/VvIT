class UserAccount:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password

    def set_password(self, new_password):
        self.__password = new_password
        return 'Пароль изменён :)'

    def check_password(self, password):
        if password == self.__password:
            return True
        return False


user = UserAccount('nmzhlk', 'nmzhlk@gmail.com', 'nmzhlk123')
print(f'Пользователь `{user.username}` с почтой `{user.email}`')

print(user.check_password('nmzhlk123'))

print(user.set_password('nmzhlk456'))
print(user.check_password('nmzhlk123'))
print(user.check_password('nmzhlk456'))
