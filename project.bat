@echo off
REM Включение кодировки для Windows
chcp 65001 > nul
cls


REM Изменяем заголовок окна консоли
title Запуск Бота-aiogram


REM Убедитесь, что Python установлен и доступен
echo Проверка наличия Python...
python --version || (
    color C
    echo Python не установлен. Установите Python и повторите попытку.
    echo Установите его по ссылке: https://www.python.org/downloads/
    title Проект - Python не установлен!
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


REM Создание виртуального окружения, если его еще нет
if not exist .venv (
    echo Создание виртуального окружения...
    python -m venv .venv
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
echo.


REM Создание Git репозитория
echo Проверка наличия Git репозитория...
if not exist .git (
    echo Создание Git репозитория...
    git init
    echo Репозиторий создан.
)
echo.


REM Очистка консоли перед запуском main.py
cls
echo Запуск main.py...
echo.
python main.py


pause
