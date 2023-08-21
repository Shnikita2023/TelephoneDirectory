import json


class TelephoneDirectory:
    """Телефонный справочник"""

    def __init__(self) -> None:
        """Инициализация объекта load_entries"""
        self.list_entries: list = self.load_entries()

    def add_entry(self, new_entry: dict[str, str]) -> str:
        """Добавление записи в справочник"""
        self.list_entries.append(new_entry)
        self.save_entries(entries=self.list_entries)
        return "***Новая запись успешно добавлена***"

    def edit_entry(self, index_entry: int, new_entry: dict[str, str]) -> str:
        """Редактирование записей в справочнике"""
        print(f"Редактирование записи {index_entry + 1}:")
        self.list_entries[index_entry] = new_entry
        self.save_entries(entries=self.list_entries)
        return "***Запись успешно отредактирована***"

    def search_entry_on_param(self, key_value_pairs: dict[str, str]) -> str:
        """Поиск записей в справочнике по нескольким параметрам"""
        count: int = 0
        for index, dict_directory in enumerate(self.list_entries):
            if all(dict_directory[key] == value for key, value in key_value_pairs.items()):
                count += 1
                print(self.format_entry(index, dict_directory))
        if count:
            return f"***Поиск завершён. Найдено {count} записи(запись)***"
        return "***Записи с данными параметрами не найдены***"

    def output_part_entry(self, page_number: int, page_size: int) -> str:
        """Вывод определённых записей из справочника"""
        start_index: int = (page_number - 1) * page_size
        end_index: int = page_number * page_size
        page_data: list = self.list_entries[start_index:end_index]
        if page_data:
            for index, item in enumerate(page_data):
                print(self.format_entry(index, item))
            return "***Записи получены***"
        return "***Записи не найдены***"

    def format_entry(self, index: int, item: dict[str, str]) -> str:
        """Форматирование записи в указанном формате"""
        return (f"***Запись {index + 1}***"
                f" Имя: {item['Имя']},"
                f" Фамилия: {item['Фамилия']},"
                f" Отчество: {item['Отчество']},"
                f" Название организации: {item['Название организации']},"
                f" Телефон рабочий: {item['Телефон рабочий']},"
                f" Телефон сотовый: {item['Телефон сотовый']}")

    def save_entries(self, entries: list) -> None:
        """Сохранение записей в файл"""
        try:
            with open("telephone_book.json", 'w', encoding="utf-8") as file:
                json.dump(entries, file, ensure_ascii=False, indent=4)
        except Exception as ex:
            print(f"Ошибка при записи в файл {ex}")

    def load_entries(self) -> list:
        """Чтение записей из файла"""
        try:
            with open("telephone_book.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []
        except Exception as ex:
            print(f"Ошибка при чтение файла {ex}")
