import os

import pytest

from src.directory import TelephoneDirectory
from tests.conftest import remove_json_file


@pytest.mark.usefixtures("remove_json_file")
class TestTelephoneDirectory:
    """Тестирование класса Telephone"""

    TEST_DATA_ENTRY: dict[str, str] = {
        "Имя": "Никита",
        "Фамилия": "Петров",
        "Отчество": "Иванович",
        "Название организации": "ООО Тест",
        "Телефон рабочий": "123456",
        "Телефон сотовый": "987654"
    }

    NEW_TEST_DATA_ENTRY: dict[str, str] = {
        "Имя": "Никита",
        "Фамилия": "Иванов",
        "Отчество": "Иванович",
        "Название организации": "ООО Тест1",
        "Телефон рабочий": "12345621",
        "Телефон сотовый": "98765423"
    }

    def test_add_entry(self, telephone_directory: TelephoneDirectory) -> None:
        """Тест функции на добавление записи"""
        new_entry = self.TEST_DATA_ENTRY
        result = telephone_directory.add_entry(new_entry)
        assert result == "***Новая запись успешно добавлена***"
        assert new_entry in telephone_directory.list_entries

    def test_edit_entry(self, telephone_directory: TelephoneDirectory) -> None:
        """Тест функции на редактирование записи"""
        new_entry = self.NEW_TEST_DATA_ENTRY
        result = telephone_directory.edit_entry(index_entry=0, new_entry=new_entry)
        assert result == "***Запись успешно отредактирована***"
        assert telephone_directory.list_entries[0] == new_entry
        assert telephone_directory.load_entries()[0] == new_entry

    def test_load_entries(self, telephone_directory: TelephoneDirectory) -> None:
        """Тест функции на чтение данных из файла"""
        entries = telephone_directory.load_entries()
        assert isinstance(entries, list)
        assert len(entries) == 1

    def test_save_entries(self, telephone_directory: TelephoneDirectory) -> None:
        """Тест функции на запись данных в файл"""
        new_entry = self.TEST_DATA_ENTRY
        telephone_directory.add_entry(new_entry)
        telephone_directory.save_entries(telephone_directory.list_entries)
        entries = telephone_directory.load_entries()
        json_file_path = os.path.join(os.getcwd(), "telephone_book.json")
        assert new_entry in entries
        assert os.path.exists(path=json_file_path), "Файл не существует"

    def test_search_entry_on_param(self, telephone_directory: TelephoneDirectory) -> None:
        """Тест функции на поиск записей"""
        search_entry = {"Имя": "Никита", "Отчество": "Иванович"}
        result = telephone_directory.search_entry_on_param(key_value_pairs=search_entry)
        entries = telephone_directory.load_entries()
        assert result == "***Поиск завершён. Найдено 2 записи(запись)***"
        assert len(entries) == 2

    def test_output_part_entry(self, telephone_directory: TelephoneDirectory) -> None:
        """Тест функции на вывод записей"""
        result = telephone_directory.output_part_entry(page_number=1, page_size=2)
        assert result == "***Записи получены***"
        assert self.NEW_TEST_DATA_ENTRY == telephone_directory.list_entries[0]
        assert self.TEST_DATA_ENTRY == telephone_directory.list_entries[1]
        assert len(telephone_directory.list_entries) == 2
