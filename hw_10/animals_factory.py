"""
📌Создайте три (или более) отдельных классов животных. Например рыбы, птицы и т.п.
📌У каждого класса должны быть как общие свойства, например имя, так и специфичные для класса.
📌Для каждого класса создайте метод, выводящий информацию специфичную для данного класса.
"""


class Animal:
    def __init__(self, name: str, age, kind='неизвестный', **kwargs):
        self.name = name
        self.age = age
        self.kind = kind
        self.kwargs = kwargs

    def get_info(self):
        return f'Имя: {self.name}. Возраст: {self.age}. Вид: {self.kind}.'

    def get_special(self):  # Только дополнительные параметры (**kwargs)
        special = ' '.join((f'Имя: {self.name}.', *(k.title() + ": " + v + "." for k, v in self.kwargs.items())))
        return special

    def get_name(self):
        return 'Имя: ' + self.name

    def get_age(self):
        return 'Возраст: ' + str(self.age)

    def get_kind(self):
        return 'Вид: ' + str(self.kind)


class Dog(Animal):
    def __init__(self, name, age, breed='Дворняжка', **kwargs):
        super().__init__(name, age)
        self.kind = 'Собака'
        self.breed = breed
        self.kwargs = kwargs

    def get_info(self):
        return super().get_info() + ' Порода ' + self.breed

    def voice(self):
        print(self.name + ': VOOFFF')


class Cat(Animal):
    def __init__(self, name, age, color='разноцветный', **kwargs):
        super().__init__(name, age)
        self.kind = 'Кот'
        self.color = color
        self.kwargs = kwargs

    def get_info(self):
        return super().get_info() + ' Цвет ' + self.color

    def feed(self, food=1):
        print(self.name + ': ' + 'ням ' * food)


class Mouse(Animal):
    def __init__(self, name, age, habitat='нора', **kwargs):
        super().__init__(name, age)
        self.kind = 'Мышь'
        self.habitat = habitat
        self.kwargs = kwargs

    def get_info(self):
        return super().get_info() + ' Место обитания ' + self.habitat


class Factory:

    @classmethod
    def new_animal(cls, kind: str = 'неизвестный', name: str = 'неизвестно', age: str = 'неизвестен', **kwargs):
        if kind.lower() == 'dog':
            return Dog(name, age, **kwargs)
        elif kind.lower() == 'cat':
            return Cat(name, age, **kwargs)
        elif kind.lower() == 'mouse':
            return Mouse(name, age, **kwargs)
        else:
            return Animal(name, age, **kwargs)


if __name__ == '__main__':
    factory = Factory()

    spike = factory.new_animal('dog', name='Spike', age='10', breed='Бульдог', specialty='любит покушать')
    tom = factory.new_animal('cat', name='Tom', age='2', color='черный')
    jerry = factory.new_animal('mouse', 'Jerry', crimes='украл 3 головки сыра', friend='Spike', hobbies='дразнить кота')
    puppy = factory.new_animal('dog', age='1', name='Puppy')
    casper = factory.new_animal(name='Casper', color='прозрачный', habitat='дом', sociality='дружелюбный',
                                skills='ходит сквозь стены')

    for animal in [puppy, tom, jerry, casper]:
        print(animal.get_info())
    print()
    for animal in [spike, jerry, casper]:
        print(animal.get_special())
    print()
    spike.voice()
    tom.feed(3)
