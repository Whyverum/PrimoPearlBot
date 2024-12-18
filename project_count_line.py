import os

# Настройка экспорта модулей
__all__ = ("count_lines_in_python_files",)
type_messages = "count_lines_project"

def count_lines_in_python_files(directory):
    total_lines = 0
    total_files = 0

    # Проходим по всем директориям и файлам в заданной директории
    for root, dirs, files in os.walk(directory):
        # Исключаем определенные директории
        if any(excluded in root for excluded in ['.venv', '.git', '.idea', '__pycache__']):
            continue

        for file in files:
            if file.endswith('.py'):  # Проверяем, что файл имеет расширение .py
                total_files += 1
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        lines = f.readlines()
                        total_lines += len(lines)
                except UnicodeDecodeError:
                    # Если файл не может быть прочитан в utf-8, логируем предупреждение и продолжаем
                    print(f"Предупреждение: невозможно прочитать файл {file_path} из-за ошибки кодировки.")
                except Exception as e:
                    # Логируем любую другую ошибку и продолжаем
                    print(f"Ошибка при обработке файла {file_path}: {e}")

    return total_lines, total_files

# Задайте путь к вашей директории
directory_path = r'/'
lines_count, files_count = count_lines_in_python_files(directory_path)

print(f'Общее количество строк в файлах .py: {lines_count}')
print(f'Общее количество файлов .py: {files_count}')
