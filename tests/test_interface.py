from _pytest.monkeypatch import MonkeyPatch

from src.directory import TelephoneDirectory
from src.interface import Interface


class TestInterface:
    """Тестирование класса Interface"""

    def test_init(self, interface: Interface) -> None:
        """Функция для тестирования init объекта TelephoneDirectory"""
        assert interface.telephone_directory is not None
        assert isinstance(interface.telephone_directory, TelephoneDirectory)

    def test_start_program(self, monkeypatch: MonkeyPatch, interface: Interface) -> None:
        """Функция для тестирования начало программы"""
        choices: tuple = ('1', '2', '3', '4', "выход")
        for choice in choices:
            monkeypatch.setattr('builtins.input', lambda _: choice)
            result = interface.start_program()
            assert result == choice
