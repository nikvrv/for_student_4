import pytest

from src.hobbits import HobbitsPriorityStatus


@pytest.fixture(scope="session")
def hobbits():
    return HobbitsPriorityStatus()


@pytest.fixture
def add_new_hobbit(hobbits):
    hobbit_name = "Alex"
    hobbits.add_new_hobbit(hobbit_name)
    return hobbit_name
