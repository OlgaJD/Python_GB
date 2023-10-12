"""Создайте класс с базовым исключением и дочерние классы исключения:
ошибка уровня
ошибка доступа.
Доработайте классы исключения так, чтобы они выдали подробную информацию об ошибках.
Передавайте необходимые данные из основного кода проекта."""


class UserException(Exception):
    def __init__(self, msg: str):
        self.msg = msg

    def __str__(self):
        return self.msg


class LevelError(UserException):
    def __init__(self, log_level, new_level):
        super().__init__(
            f'Ошибка уровня доступа! Ваш уровень ({log_level}) меньше требуемого для создания пользователя уровня {new_level}')


class AccessError(UserException):
    def __init__(self, msg=''):
        self.msg = 'Ошибка доступа' + ' ' + msg
        super().__init__(self.msg)


class NameAccessError(AccessError):
    def __init__(self, name):
        self.msg = f'Пользователя с именем "{name}" нет в базе данных'
        super().__init__(self.msg)


class IDAccessError(AccessError):
    def __init__(self, name, u_id):
        self.msg = f'Имя "{name}" не совпадает с ID {u_id}'
        super().__init__(self.msg)
