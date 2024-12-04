# BotCode/settings/configs/bot_secrets.py


# Ключи и токены от API
NameBot_bot_token = 'Сюда нужно вставить токен-бота с @BotFather'
APIKey = 'other_api_key'
WebAPIKey = 'other_web_api_key'
bot_token = NameBot_bot_token


# Пароль от базы данных пользователей
passwords = [
    # Первый сервис
    {
        'service': "db",
        'id': "db_id",
        'username': "db_username",
        'password': "db_password",
    },

    # Второй сервис
    {
        'service': "site",
        'id': "site_id",
        'username': "site_username",
        'password': "site_password"
    },
]


# Айди забанненых пользователей
ban_list_ids = {
    6666666666: "Забаненный1",    # @username_ban1
    101010101: "Забаненный2",    # @username_ban2
}


# Айди администраторов бота
important_adm_ids = {
    1234567890: "Пользователь1",  # @username1
    9987654321: "Пользователь2",  # @username2
}


# Айди групп-администраторов
important_groups_ids = {
    1087968824: "GroupAnonymousBot",
    -1234567891011: "ИмяЧата1",
    -123456789100: "ИмяЧата2",
}


# Айди администраторов бота
important_users_list_ids = {
    9999999999: "Админ1",  # @username_admin1
    888888888: "Админ2",  # @username_admin2
}
