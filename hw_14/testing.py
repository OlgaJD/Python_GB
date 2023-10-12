"""📌На семинаре 13 был создан проект по работе с пользователями (имя, id, уровень).
📌Напишите 3-7 тестов unittest для данного проекта.
📌Используйте setUp"""
import io
import json
import unittest
from unittest.mock import patch
from exceptions import NameAccessError, LevelError, IDAccessError
from classes import Terminal, User


class TestUsersProject(unittest.TestCase):

    def setUp(self):
        self.name = 'Marty'
        self.u_id = 1
        self.u_lvl = 3
        self.user_data = {self.u_lvl: [(self.name, self.u_id)]}
        with open('users.json', 'w', encoding='utf-8') as file:
            json.dump(self.user_data, file, indent=6, ensure_ascii=False)

    def test_success_login(self):
        """Проверка успешной регистрации существующего пользователя"""
        test_base = Terminal()
        result = test_base.login('Marty', 1)
        expected_result = User('Marty', '000001', 3)
        self.assertEqual(result, expected_result)

    def test_bad_name_access_error(self):
        """Проверка вызова исключения и его содержания при попытке регистрации пользователя с несуществующем именем"""
        with self.assertRaisesRegex(NameAccessError, 'Пользователя с именем "BadName" нет в базе данных'):
            test_base = Terminal()
            test_base.login('BadName', 1)

    def test_bad_id_access_error(self):
        """Проверка вызова исключения и его содержания при попытке регистрации пользователя с неверным ID"""
        with self.assertRaisesRegex(IDAccessError, 'Имя "Marty" не совпадает с ID 333'):
            test_base = Terminal()
            test_base.login('Marty', 333)

    def test_success_create_new_user(self):
        """Проверка успешного создания нового пользователя и добавление его в базу при достаточном уровне доступа
        зарегистрированного пользователя. """
        test_base = Terminal()
        login_user = test_base.login(self.name, self.u_id)
        new_test_user = User('Oscar', '777', 5)
        test_base.create_new_user(login_user, new_test_user)
        self.assertIn(new_test_user, test_base.users_db())

    def test_bad_level_error(self):
        """Проверка вызова исключения уровня доступа при попытке создания нового пользователя с уровнем выше,
        чем уровень зарегистрированного пользователя"""
        with self.assertRaises(LevelError):
            test_base = Terminal()
            login_user = test_base.login(self.name, self.u_id)
            new_test_user = User('Oscar', '777', 1)
            test_base.create_new_user(login_user, new_test_user)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_user_print(self, mock):
        """Проверка вывода информации о пользователе из базы данных"""
        test_base = Terminal()
        test_base.users()
        self.assertEqual('Имя: Marty (000001) | Уровень доступа 3\n', mock.getvalue())

    def tearDown(self) -> None:
        from pathlib import Path
        Path('users.json').unlink()


if __name__ == '__main__':
    unittest.main()
