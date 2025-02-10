@echo off
REM start.bat
REM Этот файл нужно запускать перед стартом проекта.
REM Он создает локальное окружение, скачивает все зависимости.
REM Чтобы запустить файл, используйте: start start или ./start.

REM Установить кодировку UTF-8 и заголовок для консоли.
chcp 65001 > nul
title Запуск Бота-aiogram
cls

REM Проверка установки PyPy.
echo Проверка наличия PyPy...
pypy --version > nul 2>&1 || (
    color C
    echo [ОШИБКА]: PyPy не установлен. Установите PyPy и повторите попытку.
    echo Ссылка для установки: https://www.pypy.org/download.html
    title Проект - PyPy не установлен!
    pause
    exit /b
)
echo [OK]: PyPy установлен.
echo.

REM Проверка установки Git.
echo Проверка наличия Git...
git --version > nul 2>&1 || (
    color C
    echo [ОШИБКА]: Git не установлен. Установите Git и повторите попытку.
    echo Ссылка для установки: https://git-scm.com/downloads
    title Проект - Git не установлен!
    pause
    exit /b
)
echo [OK]: Git установлен.
echo.

REM Проверка и инициализация Git репозитория.
if not exist .git (
    echo Создание Git репозитория...
    git init > nul
    git remote add origin https://github.com/Whyverum/PrimoPearlBot > nul
    echo [OK]: Git репозиторий создан и настроен.
) else (
    echo [OK]: Git репозиторий уже настроен.
)
echo.

REM Создание виртуального окружения, если его еще нет.
if not exist .venv (
    echo Создание виртуального окружения...
    pypy -m venv .venv > nul
    if %errorlevel% neq 0 (
        color C
        echo [ОШИБКА]: Не удалось создать виртуальное окружение.
        pause
        exit /b
    )
    echo [OK]: Виртуальное окружение создано.
) else (
    echo [OK]: Виртуальное окружение уже существует.
)
echo.

REM Создание файла .env с вводом данных из консоли в папке .venv.
if not exist .venv\.env (
    echo Создаётся файл .env в папке .venv...
    set /p main_bot_token=Введите токен бота (main_bot_token):
    set /p APIKey=Введите ключ API (APIKey):
    set /p WebAPIKey=Введите ключ Web API (WebAPIKey):
    set /p important_id=Введите важный ID (important_id):
    set /p secret=Введите секретный ключ (secret):

    REM Проверяем пустые значения.
    if "%main_bot_token%"=="" (
        echo [ОШИБКА]: Токен бота не может быть пустым.
        pause
        exit /b
    )
    if "%APIKey%"=="" (
        echo [ОШИБКА]: Ключ API не может быть пустым.
        pause
        exit /b
    )
    if "%WebAPIKey%"=="" (
        echo [ОШИБКА]: Ключ Web API не может быть пустым.
        pause
        exit /b
    )
    if "%important_id%"=="" (
        echo [ОШИБКА]: Важный ID не может быть пустым.
        pause
        exit /b
    )
    if "%secret%"=="" (
        echo [ОШИБКА]: Секретный ключ не может быть пустым.
        pause
        exit /b
    )

    REM Создание файла .env.
    (
        echo main_bot_token=%main_bot_token%
        echo APIKey=%APIKey%
        echo WebAPIKey=%WebAPIKey%
        echo important_id=%important_id%
        echo secret=%secret%
    ) > .venv\.env
    echo [OK]: Файл .env успешно создан в папке .venv!
) else (
    echo [OK]: Файл .env уже существует в папке .venv.
)
echo.

REM Активация виртуального окружения.
echo Активация виртуального окружения...
call .venv\Scripts\activate > nul
if %errorlevel% neq 0 (
    color C
    echo [ОШИБКА]: Не удалось активировать виртуальное окружение.
    pause
    exit /b
)
echo [OK]: Виртуальное окружение активировано.
echo.

REM Проверка и установка Poetry.
echo Проверка наличия Poetry...
poetry --version > nul 2>&1 || (
    echo Установка Poetry...
    pip install poetry > nul
    if %errorlevel% neq 0 (
        color C
        echo [ОШИБКА]: Не удалось установить Poetry.
        pause
        exit /b
    )
    echo [OK]: Poetry успешно установлен.
)
echo [OK]: Poetry установлен.
echo.

REM Установка зависимостей.
echo Установка зависимостей проекта...
poetry install > nul
if %errorlevel% neq 0 (
    color C
    echo [ОШИБКА]: Не удалось установить зависимости.
    pause
    exit /b
)
echo [OK]: Зависимости установлены.
echo.

REM Очистка консоли перед запуском.
cls
echo Все готово! Настройте конфигурацию или запустите main.py.
pause
