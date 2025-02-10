# BotLibrary/timers/start_timer.py
# Функция получения времени старта

import pytz
from tzlocal import get_localzone
from datetime import datetime
from ..configs import TimeVariable

# Настройка экспорта модулей и логирования
__all__ = ("host_time", "get_choice_time", "get_time_zone")
log_type = "Time"


"""Получение времени хоста и иного места"""
timezone = pytz.timezone(TimeVariable.choice_utc_krsk)  # Используем Красноярск вместо Москвы
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

    # Перевод времени в выбранный часовой пояс
    choice_now = utc_now.astimezone(choice_tz)

    # Смещение UTC для выбранного региона
    utc_offset_choice = choice_now.utcoffset().total_seconds() / 3600  # Смещение в часах

    # Форматирование времени в стиле, как у Москвы (YYYY-MM-DD HH:MM:SS (UTC±X))
    choice_time = choice_now.strftime(TimeVariable.format) + f" (UTC{int(utc_offset_choice):+})"

    return choice_time
