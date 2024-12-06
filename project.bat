@echo off
cls
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
echo Проверка наличия Git репозитория...
if not exist .git (
    echo Создание Git репозитория...
    git init
    echo Репозиторий создан.
)
echo.


REM Запрос на восстановление всех файлов проекта из репозитория
echo Внимание! Если вы хотите восстановить все файлы проекта из GitHub, введите Y.
echo Для отмены процесса введите любой другой символ.
set /p user_input=Вы хотите восстановить все файлы? (Y/N):⠀

if /I "%user_input%"=="Y" (
    echo Восстановление всех файлов из репозитория...
    git reset --hard HEAD || (
        color C
        echo Не удалось восстановить файлы из Git. Проверьте наличие подключения к интернету или правильность настроек Git.
        pause
        exit /b
    )
    echo Все файлы восстановлены.
) else (
    echo Восстановление файлов отменено.
)



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
echo.
python main.py


pause
