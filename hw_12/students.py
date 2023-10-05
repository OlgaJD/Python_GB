"""Создайте класс студента.
Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы.
Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых.
"""
import json


class FIOCheck:
    """Проверяет ФИО на первую заглавную букву и наличие только букв"""

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if not value.isalpha():
            raise ValueError('Для ФИО можно использовать только буквы')
        if not value.istitle():
            raise ValueError('Фамилия, имя и отчество должны начинаться с большой буквы')
        setattr(instance, self.name, value)


class CSVReader:
    """Функция читает файл csv и создает список предметов для студента в формате list.
    Количество предметов, которые добавляются в список, зависит от переданного параметра course (курса студента).
    Если курс студента не указан при создании класса, в список добавляются все предметы из файла csv.
    Функция вызывается автоматически при создании экземпляра класса Student.
    """

    @classmethod
    def lessons_from_csv(cls, course, file='lessons.csv'):
        with open(file, 'r', encoding='utf-8') as r:
            lessons = []
            data = r.readlines()
            if course is None:
                count = len(data)
            elif course == 1:
                count = 3
            elif course == 2:
                count = 5
            elif course == 3:
                count = 7
            else:
                raise ValueError('Неверно указан курс. Доступны значения от 1 до 3 или незаполненное значение.')
            for i in range(count):
                lessons.append(data[i].split())
            return lessons


class Student:
    surname = FIOCheck()
    name = FIOCheck()
    middlename = FIOCheck()

    def __init__(self, surname, name, middlename, course=None):
        self.surname = surname
        self.name = name
        self.middlename = middlename
        self.course = course if course else None
        self._dnevnik = self.dnevnik_create(course)

    def dnevnik_create(self, course):
        """ Создает дневник для студента на основании полученного списка в формате list.
        Оценка к предмету может быть только одна. Результаты тестов могут содержать несколько значений.
        Формат дневника - словарь вида:
        {
            'Предмет_1': {'Оценка': 'None', 'Результаты тестов': ['None']},
            'Предмет_2': {'Оценка': 'None', 'Результаты тестов': ['None']},
        }
        """
        lessons = CSVReader.lessons_from_csv(course)
        self._dnevnik = dict()
        for lesson in lessons:
            self._dnevnik[''.join(lesson)] = {'Оценка': None, 'Результаты тестов': [None]}
        return self._dnevnik

    def __str__(self):
        """Метод представления для пользователя."""
        return f'Студент {self.surname} {self.name} {self.middlename} изучает предметы: ' \
               f'{", ".join(list(map(str, self._dnevnik.keys())))} '

    def lessons(self):
        """Возвращает все предметы, которые изучает студент. Функция не возвращает оценки и результаты тестов."""
        return ", ".join(list(map(str, self._dnevnik.keys())))

    def get_grades(self):
        """Возвращает оценки по предметам, в виде списка: ['Предмет_1: оценка', 'Предмет_2: оценка']"""
        grades = []
        for k in self._dnevnik.keys():
            grades.append(''.join(f'{k}: {self._dnevnik[k]["Оценка"]}'))
        return grades

    def average_grade(self):
        """Возвращает средний балл по оценкам всех предметов вместе взятых.
        Если оценок нет, возвращается строка: 'У студента еще нет оценок',
        предмет не учитывается в расчетах среднего балла."""
        sum_grades = 0
        count_lessons = 0
        for i in self._dnevnik.keys():
            if self._dnevnik[i]["Оценка"] is not None:
                sum_grades += self._dnevnik[i]["Оценка"]
                count_lessons += 1
        if count_lessons == 0:
            return 'У студента еще нет оценок'
        return round((sum_grades / count_lessons), 2)

    def set_grade(self, lesson, grade):
        """Записывает оценку по указанному предмету в дневник.
        Оценка может быть только одна, поэтому каждый раз значение перезаписывается"""
        if lesson not in self._dnevnik.keys():
            raise ValueError('Студент не изучает указанный предмет')
        if not isinstance(grade, int):
            raise ValueError('Неверный формат. Оценка должна быть целым числом')
        if not 1 < grade < 6:
            raise ValueError('Неверное значение. Оценка должна быть в интервале от 2 до 5')
        test_results = self._dnevnik[lesson]['Результаты тестов']
        self._dnevnik[lesson] = {'Оценка': grade, 'Результаты тестов': test_results}

    def set_test_result(self, lesson: str, result: list):
        """Записывает результаты тестов по указанному предмету в дневник.
        Результатов тестов по предмету может быть несколько"""
        if lesson not in self._dnevnik.keys():
            raise ValueError('Студент не изучает указанный предмет')
        for i in result:
            if not isinstance(i, int):
                raise ValueError('Неверный формат. Результаты тестов должны быть целыми числами')
        if list(filter(lambda x: x <= 0 or x > 101, result)):
            raise ValueError('Неверное значение. Результаты теста должны быть в интервале от 0 до 100')
        grade = self._dnevnik[lesson]['Оценка']
        old_results = self._dnevnik[lesson]['Результаты тестов']
        if None in old_results:
            old_results = result
        else:
            old_results += result
        self._dnevnik[lesson] = {'Оценка': grade, 'Результаты тестов': old_results}

    def get_test_result(self):
        """Возвращает результаты тестов по предметам в виде списка:
        ['Предмет_1: результаты тестов', 'Предмет_2: результаты тестов']"""
        results = []
        for k in self._dnevnik.keys():
            results.append(''.join(f'{k}: {self._dnevnik[k]["Результаты тестов"]}'))
        return results

    def average_tests(self, lesson=None):
        """Возвращает средний балл по тестам для каждого предмета.
        Если предмет указан, возвращается средний балл.
        Если предмет не указан возвращается список со всеми предметами и средним баллом по каждому.
        Если результатов теста еще нет в значении среднего балла указывается 'Тесты не проводились'"""
        if lesson is None:
            results = []
            for k in self._dnevnik.keys():
                if None in self._dnevnik[k]["Результаты тестов"]:
                    results.append(''.join(f'{k}: Тесты не проводились'))
                else:
                    res_list = self._dnevnik[k]["Результаты тестов"]
                    summ = sum(res_list)
                    count = len(res_list)
                    av = round((summ / count), 2)
                    results.append(''.join(f'{k}: {av}'))
            return results

        results = self._dnevnik[lesson]['Результаты тестов']
        if lesson not in self._dnevnik.keys():
            raise ValueError('Студент не изучает указанный предмет')
        if results is None:
            raise ValueError('Еще нет результатов по этому предмету')
        average = round((sum(results) / len(results)), 2)
        return average

    def archive(self):
        """Записывает данные дневника в файл json"""
        path = f'{self.surname}_{self.name}.json'
        with open(path, 'w', encoding='utf-8') as w:
            w.write(json.dumps(self._dnevnik, indent=4, ensure_ascii=False))


marty = Student('Котиков', 'Марти', 'Оскарович', 2)
oscar = Student('Cat', 'Oscar', 'Potato', 1)

print(marty)
marty.set_grade('Chemistry', 3)
marty.set_grade('Informatics', 5)
marty.set_test_result('Chemistry', [5, 6, 10])
marty.set_test_result('Biology', [80, 1, 99])
marty.set_grade('Biology', 3)
marty.set_test_result('Literature', [10, 55, 80])
print(f'Оценки: {marty.get_grades()}')
print(f'Тесты: {marty.get_test_result()}')
print(f'Средний тест по Biology: {marty.average_tests("Biology")}')
print(f'Средняя оценка по всем предметам: {marty.average_grade()}')
print(f'Средний тест по всем предметам: {marty.average_tests()}')
marty.archive()
