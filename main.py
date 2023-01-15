"""Данный модуль описывает поведение персонажа игры."""


from random import randint

DEFAULT_ATTACK: int = 5
"""Константа по умолчанию числового выражения атаки персонажа."""

DEFAULT_DEFENCE: int = 10
"""Константа по умолчанию числового выражения защиты персонажа."""

DEFAULT_STAMINA: int = 80
"""Константа по умолчанию числового выражения выносливости персонажа."""


class Character:
    """Родительский класс, описывающий свойства и методы персонажей."""

    BRIEF_DESC_CHAR_CLASS: str = 'отважный любитель приключений'
    """Константа описания персонажа."""

    RANGE_VALUE_ATTACK: tuple = (1, 3)
    """Константа диапазона значений атаки."""

    RANGE_VALUE_DEFENCE: tuple = (1, 5)
    """Константа диапазона значений защиты."""

    SPECIAL_SKILL: str = 'Удача'
    """Константа описания специального умения персонажа."""

    SPECIAL_BUFF: int = 15
    """Константа числового выражения специального умения персонажа."""

    def __init__(self, name: str) -> None:
        """Конструктор родительского класса."""

        self.name = name

    def attack(self) -> str:
        """Метод атаки персонажа."""

        value_attack: int = DEFAULT_ATTACK + randint(*self.RANGE_VALUE_ATTACK)
        return f'{self.name} нанес урон противнику равный {value_attack}'

    def special(self) -> str:
        """Метод специального умения персонажа."""

        return (f'{self.name} применил специальное умение '
                f'"{self.SPECIAL_SKILL} {self.SPECIAL_BUFF}".')

    def defence(self) -> str:
        """Метод защиты персонажа."""

        value_defence: int = (DEFAULT_DEFENCE +
                              randint(*self.RANGE_VALUE_DEFENCE))
        return f'{self.name} блокировал {value_defence} ед. урона.'

    def __str__(self) -> str:
        """Метод вывода на печать собственного класса персонажа."""

        return f'{self.__class__.__name__} - {self.BRIEF_DESC_CHAR_CLASS}.'


class Warrior(Character):
    """Класс-наследник для персонажа Воитель."""

    BRIEF_DESC_CHAR_CLASS = ('дерзкий воин ближнего боя. '
                             'Сильный, выносливый и отважный.')
    RANGE_VALUE_ATTACK = (3, 5)
    RANGE_VALUE_DEFENCE = (5, 10)
    SPECIAL_SKILL = 'Выносливость'
    SPECIAL_BUFF = DEFAULT_STAMINA + 25


class Mage(Character):
    """Класс-наследник для персонажа Маг."""

    BRIEF_DESC_CHAR_CLASS = ('находчивый воин дальнего боя. '
                             'Обладает высоким интеллектом')
    RANGE_VALUE_ATTACK = (5, 10)
    RANGE_VALUE_DEFENCE = (-2, 2)
    SPECIAL_SKILL = 'Находчивость'
    SPECIAL_BUFF = DEFAULT_ATTACK + 40


class Healer(Character):
    """Класс-наследник для персонажа Лекарь."""

    BRIEF_DESC_CHAR_CLASS = ('могущественный заклинатель. '
                             'Черпает силы из природы, веры и духов')
    RANGE_VALUE_ATTACK = (-3, -1)
    RANGE_VALUE_DEFENCE = (2, 5)
    SPECIAL_SKILL = 'Защита'
    SPECIAL_BUFF = DEFAULT_DEFENCE + 30


def start_training(char_class: Character) -> str:
    """Функция тренеровки способностей выбранного персонажа."""

    game_commands: dict = {'attack': char_class.attack,
                           'defence': char_class.defence,
                           'special': char_class.special}
    print('Потренируйся управлять своими навыками.')
    print('Введи одну из команд: attack — чтобы атаковать противника, '
          'defence — чтобы блокировать атаку противника или '
          'special — чтобы использовать свою суперсилу.')
    print('Если не хочешь тренироваться, введи команду skip.')
    command: str = ''
    while command != 'skip':
        command = input('Введи команду: ')
        if command in game_commands:
            print(game_commands[command]())
        elif command != 'skip':
            print('Введена неверная команда. Попробуйте ещё раз.')
    return 'Тренировка окончена.'


def choice_char_class(char_name: str) -> Character:
    """Функция выбора персонажа."""

    game_classes: dict = {'warrior': Warrior, 'mage': Mage, 'healer': Healer}
    approve_choice: str = ''
    while approve_choice != 'y':
        selected_class: str = input('Введи название персонажа, '
                                    'за которого хочешь играть: '
                                    'Воитель — warrior, '
                                    'Маг — mage, Лекарь — healer: ')
        char_class: Character = game_classes[selected_class](char_name)
        print(char_class)
        approve_choice = input('Нажми (Y), чтобы подтвердить выбор, '
                               'или любую другую кнопку, '
                               'чтобы выбрать другого персонажа ').lower()
    return char_class


if __name__ == '__main__':
    """Основная функция.
    Здесь происходит выбор персонажа и демонстрация его умений.
    """

    print('Приветствую тебя, искатель приключений! '
          'Прежде чем начать игру...')
    char_name: str = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10. '
          'Ты можешь выбрать один из трёх путей силы: '
          'Воитель, Маг, Лекарь')
    char_class: Character = choice_char_class(char_name)
    print(start_training(char_class))
