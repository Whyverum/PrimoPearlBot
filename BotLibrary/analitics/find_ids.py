# BotLibrary/analitics/find_ids.py
# Проверка пользователя на нахождение в списках бота

from ..configs.list_ids import DataID

# Настройка экспорта модулей и логирования
__all__ = ("find_imp_id", "find_adm_id", "find_ban_id")
log_type = "ID"


# Функция поиска человека в списке администраторов
def find_adm_id(admin_id):
    admin_id = str(admin_id)
    if admin_id in DataID.admins:
        return True
    else:
        return f"Пользователь {admin_id} не является администратором!"


# Функция поиска человека в списке забаненных пользователей
def find_ban_id(ban_id):
    ban_id = str(ban_id)
    if ban_id in DataID.ban_list:
        return True
    else:
        return f"Пользователь {ban_id} не забанен!"


# Функция поиска человека в списке "важных" чатов
def find_imp_id(user_id):
    user_id = str(user_id)
    if user_id in DataID.important:
        return DataID.important[user_id]  # Возвращаем имя пользователя
    else:
        return user_id
