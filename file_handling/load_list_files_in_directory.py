import os


def load_list_files_in_directory(directory_path):
    """Загружает все файлы из указанной директории и возвращает их пути без корневой папки."""
    files = []
    for root, _, filenames in os.walk(directory_path):
        for filename in filenames:
            full_path = os.path.join(root, filename)
            relative_path = os.path.relpath(full_path, directory_path)
            files.append(relative_path)
    return files
