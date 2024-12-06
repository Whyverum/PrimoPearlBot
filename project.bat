@echo off
REM project.bat
REM Этот файл нужно запускать перед стартом проекта
REM Он создает локальное окружение, скачивает все зависимости
REM Чтобы запустить файл используйте: start project или ./project


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


REM Обновление проекта из репозитория
echo Обновление проекта из GitHub...
git fetch origin || (
    color C
    echo Не удалось подключиться к удалённому репозиторию. Проверьте настройки Git и подключение к интернету.
    pause
    exit /b
)


git reset --hard origin/master || (
    color C
    echo Не удалось обновить проект. Проверьте наличие подключения к интернету или правильность настроек Git.
    pause
    exit /b
)
echo Проект успешно обновлён.
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


REM Очистка консоли перед запуском main.py
cls
echo Запуск main.py...
python main.py


pause
