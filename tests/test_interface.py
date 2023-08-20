import pytest

from src.directory import TelephoneDirectory




class TestTelephoneDirectory:
    TEST_ENTRY = {
        "Имя": "Иван",
        "Фамилия": "Петров",
        "Отчество": "Иванович",
        "Название организации": "ООО Тест",
        "Телефон рабочий": "123456",
        "Телефон сотовый": "987654"
    }

    def test_add_entry(self, telephone_directory: TelephoneDirectory):
        new_entry = self.TEST_ENTRY

        result = telephone_directory.add_entry(new_entry)

        assert result == "***Новая запись успешно добавлена***"
        assert new_entry in telephone_directory.list_entries

    def test_edit_entry(self, telephone_directory):
        new_entry = {
            "Имя": "Никита",
            "Фамилия": "Иванов",
            "Отчество": "Иванович",
            "Название организации": "ООО Тест1",
            "Телефон рабочий": "12345621",
            "Телефон сотовый": "98765423"
        }
        result = telephone_directory.edit_entry(index_entry=0, new_entry=new_entry)
        assert result == "***Запись успешно отредактирована***"
        assert telephone_directory.list_entries[0] == new_entry
        assert telephone_directory.load_entries()[0] == new_entry

    def test_load_entries(self, telephone_directory: TelephoneDirectory):
        entries = telephone_directory.load_entries()
        assert isinstance(entries, list)
        assert len(entries) == 1
    #
    # def test_save_entries(self, telephone_directory):
    #     new_entry = self.TEST_ENTRY
    #     telephone_directory.add_entry(new_entry)
    #
    #     telephone_directory.save_entries(telephone_directory.list_entries)
    #
    #     entries = telephone_directory.load_entries()
    #     assert new_entry in entries


    # def test_search_entry_on_param(self, telephone_directory):
    #     search_entry = {"Имя": "Никита", "Отчество": "Иванович"}
    #     result = telephone_directory.search_entry_on_param(key_value_pairs=search_entry)
    #     assert result == "***Поиск завершён***"
    #
    # def test_output_part_entry(self, telephone_directory):
    #     result = telephone_directory.output_part_entry(page_number=1, page_size=1)
    #     assert result == "***Записи получены***"
