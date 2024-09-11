from pathlib import Path


def load_files_content(file_paths):
    contents = []
    for file_path in file_paths:
        try:
            # Используем pathlib для работы с путями
            path = Path(file_path)
            # Получаем путь без первых двух папок
            relative_path = Path(*path.parts[2:])
            
            # Чтение содержимого файла
            with path.open('r', encoding='utf-8') as file:
                file_content = file.read()
            
            # Формируем строку для каждого файла
            contents.append(f"#{relative_path}\n\n{file_content}\n\n")
        except Exception as e:
            print(f"Ошибка при загрузке файла {file_path}: {e}")
    
    # Соединяем все строки в один текст
    return ''.join(contents)
