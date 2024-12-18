@echo off
REM start.bat
REM Этот файл нужно запускать перед стартом проекта
REM Он создает локальное окружение, скачивает все зависимости
REM Чтобы запустить файл используйте: start start или ./start

REM Включение кодировки для Windows
chcp 65001 > nul
cls

REM Изменяем заголовок окна консоли
title Запуск Бота-aiogram

REM Убедитесь, что PyPy установлен и доступен
echo Проверка наличия PyPy...
pypy --version || (
    color C
    echo PyPy не установлен. Установите PyPy и повторите попытку.
    echo Установите его по ссылке: https://www.pypy.org/download.html
    title Проект - PyPy не установлен!
    pause
    exit /b
)
echo.

REM Проверка наличия Git
echo Проверка наличия Git...
git --version > nul 2>&1 || (
    color C
    echo Git не установлен. Установите Git и повторите попытку.
    echo Установите его по ссылке: https://git-scm.com/downloads
    title Проект - Git не установлен!
    pause
    exit /b
)
echo.

REM Проверка наличия Git репозитория
if not exist .git (
    echo Создание Git репозитория...
    git init
    echo Добавление удалённого репозитория...
    git remote add origin https://github.com/Whyverum/PrimoPearlBot
) else (
    echo Удалённый репозиторий уже настроен.
)
echo.

REM Создание .env для хранения токенов
echo Создаётся файл .env...
(
    echo main_bot_token=Вставьте Токен бота с @BotFather
    echo APIKey=Иной ключ-api
    echo WebAPIKey=Иной ключ web-api
    echo important_id=Иной важный айди
    echo secret=Некий секрет
) > .env
echo.
echo Файл .env - успешно создан!
echo Пожалуйста, перейдите в файл и вставьте свои ключи.
pause > Вы готовы продолжить? Нажмите ENTER, чтобы продолжить!
echo.
pause > Вы уверены???Нажмите ENTER, чтобы продолжить!

REM Создание виртуального окружения, если его еще нет
if not exist .venv (
    echo Создание виртуального окружения...
    pypy -m venv .venv
    echo.
)

REM Активируем виртуальное окружение
echo Активация виртуального окружения...
call .venv\Scripts\activate
echo.

REM Установка Poetry, если не установлен
echo Проверка наличия Poetry...
poetry --version || (
    echo Установка Poetry...
    pip install poetry
)
echo.

REM Установка зависимостей из poetry.lock и pyproject.toml
echo Установка зависимостей...
poetry install
poetry update
echo.

REM Очистка консоли перед запуском main.py
cls
pause > Настройте конфигуратор или запустите main.py!
