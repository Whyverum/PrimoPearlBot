# BotLibrary/library/time.py
# Библиотека поиски времени

import pytz
from tzlocal import get_localzone
from datetime import datetime

# Настройка экспорта модулей и логирования
__all__ = ("TimeVariable", "host_time", "get_choice_time", "get_time_zone")
log_type = "Time"


"""Создание класса с временными параметрами"""
class TimeVariable:
    format = "%Y-%m-%d %H:%M:%S"
    another_format = "%S:%M:%H %d-%m-%Y"
    choice_main_utc = "Asia/Novosibirsk"
    choice_utc_msk = "Europe/Moscow"


"""Получение времени хоста и иного места"""
timezone = pytz.timezone(TimeVariable.choice_utc_msk)
host_time = datetime.now(timezone)


"""Функция получения локальной временной зоны"""
def get_time_zone():
    local_timezone = get_localzone()
    return local_timezone.key


"""Возвращает текущее время по выбранному часовому поясу в формате строки"""
def get_choice_time(choice_utc):
    # Текущее время в UTC
    utc_now = datetime.now(pytz.utc)

    # Московский часовой пояс
    choice_tz = pytz.timezone(choice_utc)

    # Перевод времени в московский часовой пояс
    choice_now = utc_now.astimezone(choice_tz)

    # Смещение UTC для Москвы
    utc_offset_choice = choice_now.utcoffset().total_seconds() / 3600  # Смещение в часах

    # Форматирование времени
    choice_time = choice_now.strftime(TimeVariable.format) + f" (UTC{int(utc_offset_choice):+})"

    return choice_time
