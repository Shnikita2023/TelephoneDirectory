import os
import pytest

from src.directory import TelephoneDirectory


@pytest.fixture()
def telephone_directory() -> TelephoneDirectory:
    return TelephoneDirectory()


@pytest.fixture(scope="session")
def remove_json_file(request):
    directory = TelephoneDirectory()
    json_file_path = "/tests/telephone_book.json"

    def cleanup():
        if os.path.exists(json_file_path):
            os.remove(json_file_path)

        # Зарегистрировать функцию cleanup() как финализатор
    request.addfinalizer(cleanup)

    return directory
