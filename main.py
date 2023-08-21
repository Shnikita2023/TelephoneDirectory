from src.interface import Interface


def main() -> None:
    """
    Запуск программы
    :return: None
    """
    interface: Interface = Interface()
    interface.main_program()


if __name__ == '__main__':
    main()
