# BotLibrary/library/decorator.py
# Небольшая библиотека для декорирования текста

from art import *
from colorama import *
from termcolor import *
import cowsay

# Подключение ANSI в стандартное Windows_cmd
just_fix_windows_console()


# Некоторые возможности библиотеки art и termcolor  (не полный, проще использовать сам art)
class ArtObject:
    text_hw = colored("Привет, Мир!", "red", attrs=["reverse", "blink"])

    coffe_art = art("coffee", number=1, space=1)  # c[_]
    women_art = art("woman", number=1, space=1)  # ▓⚗_⚗▓ ▓⚗_⚗▓
    butterfly_art = art("butterfly", number=1, space=1)  # Ƹ̵̡Ӝ̵̨̄Ʒ
    happy_art = art("happy", number=1, space=1)  # ۜ\(סּںסּَ` )/ۜ
    random_art = art("random", number=1, space=1)  # Вывод случайного арта из библиотеки

    block_font = 'block'  # Делает большие квадраты вокруг рисунка
    white_buble = 'white_bubble'  # Делает вокруг букв белый кружок
    cybermedium = 'cybermedium'  # Делает текст более "киберпанковым"
    random_font = 'random'  # Делает случайный фон вокруг рисунка


# Коды для редактирования текста
class TextDecorator:
    RESET_DECORATOR = "\033[0m"  # Код для сброса форматирования
    BOLD = "\033[1m"  # Код для включения жирного текста
    FAINT = "\033[2m"  # Код для включения тонкого текста (редко поддерживается)
    KURTIV = "\033[3m"  # Код для включения курсива
    UNDERLINE = "\033[4m"  # Код для включения подчеркнутого текста
    BLINK = "\033[5m"  # Код для включения мигающего текста (редко поддерживается)
    INVERT = "\033[7m"  # Код для инверсированного цвета
    HIDDEN = "\033[8m"  # Код для скрытого текста
    STRIKETHROUGH = "\033[9m"  # Код для зачеркнутого текста

    # Коды для цвета текста
    BLACK = "\033[30m"  # Черный текст
    RED = "\033[31m"  # Красный текст
    GREEN = "\033[32m"  # Зеленый текст
    YELLOW = "\033[33m"  # Желтый текст
    BLUE = "\033[34m"  # Синий текст
    MAGENTA = "\033[35m"  # Пурпурный текст
    CYAN = "\033[36m"  # Бирюзовый текст
    WHITE = "\033[37m"  # Белый текст
    LIGHT_BLACK = "\033[90m"  # Светлый черный (серый) текст
    LIGHT_RED = "\033[91m"  # Светлый красный текст
    LIGHT_GREEN = "\033[92m"  # Светлый зеленый текст
    LIGHT_YELLOW = "\033[93m"  # Светлый желтый текст
    LIGHT_BLUE = "\033[94m"  # Светлый синий текст
    LIGHT_MAGENTA = "\033[95m"  # Светлый пурпурный текст
    LIGHT_CYAN = "\033[96m"  # Светлый бирюзовый текст
    LIGHT_WHITE = "\033[97m"  # Светлый белый текст

    # Коды для цвета фона
    BLACK_BACKGROUND = "\033[40m"  # Черный фон
    RED_BACKGROUND = "\033[41m"  # Красный фон
    GREEN_BACKGROUND = "\033[42m"  # Зеленый фон
    YELLOW_BACKGROUND = "\033[43m"  # Желтый фон
    BLUE_BACKGROUND = "\033[44m"  # Синий фон
    MAGENTA_BACKGROUND = "\033[45m"  # Пурпурный фон
    CYAN_BACKGROUND = "\033[46m"  # Бирюзовый фон
    WHITE_BACKGROUND = "\033[47m"  # Белый фон
    LIGHT_BLACK_BACKGROUND = "\033[100m"  # Светлый черный фон
    LIGHT_RED_BACKGROUND = "\033[101m"  # Светлый красный фон
    LIGHT_GREEN_BACKGROUND = "\033[102m"  # Светлый зеленый фон
    LIGHT_YELLOW_BACKGROUND = "\033[103m"  # Светлый желтый фон
    LIGHT_BLUE_BACKGROUND = "\033[104m"  # Светлый синий фон
    LIGHT_MAGENTA_BACKGROUND = "\033[105m"  # Светлый пурпурный фон
    LIGHT_CYAN_BACKGROUND = "\033[106m"  # Светлый бирюзовый фон
    LIGHT_WHITE_BACKGROUND = "\033[107m"  # Светлый белый фон
