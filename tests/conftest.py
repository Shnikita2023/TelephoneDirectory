import os
import pytest

from src.directory import TelephoneDirectory
from src.interface import Interface


@pytest.fixture(scope="session")
def telephone_directory() -> TelephoneDirectory:
    """Функция создаёт экземпляр класса TelephoneDirectory"""
    return TelephoneDirectory()


@pytest.fixture(scope="session")
def interface() -> Interface:
    """Функция создаёт экземпляр класса Interface"""
    return Interface()


@pytest.fixture(scope="session")
def remove_json_file() -> None:
    """Функция удаляет файл telephone_book.json после завершение всех тестов"""
    json_file_path = os.path.join(os.getcwd(), "telephone_book.json")
    try:
        yield
        os.remove(json_file_path)
    except Exception as e:
        print(f"Ошибка удаления файла {json_file_path}: {e}")
