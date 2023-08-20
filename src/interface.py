import re

from .directory import TelephoneDirectory


class Interface:
    """Консольный интерфейс для телефонного справочника"""
    DASHES: str = "-" * 100
    print(DASHES)
    print("Добро пожаловать в телефонный справочник!")
    print(DASHES)

    def __init__(self) -> None:
        self.telephone_directory: TelephoneDirectory = TelephoneDirectory()

    def start_program(self) -> str:
        """Начало программы"""
        print("Что-бы продолжить выберите цифру из ниже предоставленного списка, если желаете выйти(введите:"
              "'выход')")
        answer = input("1. Добавить запись в справочник\n"
                       "2. Вывести записи по характеристикам\n"
                       "3. Найти определённые записи по любым из параметров\n"
                       "4. Отредактировать запись\n"
                       "Введите цифру из выше перечисленного списка: ").strip()
        print(self.DASHES)
        return answer

    def main_program(self) -> None:
        """Основная работа программы"""
        dict_call_func: dict = {
            "1": self.add_data,
            "2": self.print_data,
            "3": self.search_data,
            "4": self.edit_data
        }
        while True:
            result: str = self.start_program()
            if result.lower() == "выход":
                break
            elif result in dict_call_func:
                res = dict_call_func[result]
                print(res())
                print(self.DASHES)
            else:
                print(self.DASHES)
                print("Вы ввели некорректный формат данных, нужна ввести цифру от 1 до 4 или написать 'выход'")

    def add_data(self) -> str:
        """Добавление данных"""
        new_data: dict[str, str] = self.preparation_data()
        return self.telephone_directory.add_entry(new_data)

    def print_data(self) -> str:
        """Вывод данных"""
        while True:
            page_number: str = input("Введите какую страницу справочника вывести: ")
            page_size: str = input("Введите количество записей которые нужно вывести: ")
            if int(page_number) > 0 and int(page_size) > 0:
                return self.telephone_directory.output_part_entry(int(page_number), int(page_size))
            print(self.DASHES)
            print("Неверный формат данных: Введите число от 1 до ...")

    def search_data(self) -> str:
        """Поиск данных"""
        specification: dict[str, str] = {
            "1": "Имя",
            "2": "Фамилия",
            "3": "Отчество",
            "4": "Название организации",
            "5": "Телефон рабочий",
            "6": "Телефон сотовый",
        }
        while True:
            key_specification: str = input("По каким параметрам искать запись в справочнике?\n"
                                           "1. Имя, "
                                           "2. Фамилия, "
                                           "3. Отчество, "
                                           "4. Название организации, "
                                           "5. Телефон рабочий, "
                                           "6. Телефон сотовый\n"
                                           "Введите одну или несколько цифр из списка для поиска записей "
                                           "(Пример: 1 или 1 4): ")

            keys: list[str] = key_specification.split()
            if all(key in specification for key in keys):
                key_value_pairs: dict[str, str] = {}
                for key in keys:
                    value_specification: str = input(f"Введите {specification[key]} по которому искать: ")
                    key_value_pairs[specification[key]] = value_specification
                return self.telephone_directory.search_entry_on_param(key_value_pairs)

            print(self.DASHES)
            print("Неверный формат данных: Введите цифры от 1 до 6!")

    def edit_data(self) -> str:
        """Редактирование данных"""
        while True:
            index_entry: str = input("Введите номер записи, которую хотите отредактировать: ")
            index_entry: int = int(index_entry) - 1
            if 0 <= index_entry <= self.telephone_directory.lenght:
                new_data: dict = self.preparation_data()
                return self.telephone_directory.edit_entry(index_entry, new_data)
            print(self.DASHES)
            print(f"Неверный формат данных: Введите число от 1 до {self.telephone_directory.lenght}")

    def preparation_data(self) -> dict[str, str]:
        """Подготовка данных"""
        entry_directory: tuple = ("Имя", "Фамилия", "Отчество", "Название организации", "Телефон рабочий",
                                  "Телефон сотовый")
        new_data: dict[str, str] = {}
        for entry in entry_directory:
            while True:
                try:
                    value: str = input(f"Введите {entry}: ")
                    if self.validate_data(entry, value):
                        new_data[entry] = value
                        break
                except ValueError as e:
                    print(f"***Неверный формат данных***: {e}\n***Введите повторно!***")

        return new_data

    def validate_data(self, entry: str, value: str) -> bool:
        """Проверка на валидность данных"""
        value_directory: tuple = ("Имя", "Фамилия", "Отчество", "Название организации")
        if entry in value_directory:
            if not re.match(r'^[A-ZА-Я][a-zа-я]+$', value):
                raise ValueError(f"Поле '{entry}' должно содержать только буквы, первый символ заглавный, а остальные "
                                 f"строчные и длина слова больше 1.")
        elif entry == "Телефон рабочий":
            if not re.match(r'^\d{5,}$', value):
                raise ValueError(f"Поле '{entry}' должно содержать только цифры и иметь длину больше 4 символов.")
        elif entry == "Телефон сотовый":
            if not re.match(r'^[78]\d{10}$', value):
                raise ValueError(f"Поле '{entry}' должно содержать только цифры, начинающихся с 7(8) и иметь длину 11 "
                                 f"символов.")
        return True
