import pytest


class TestHobbits:
    @pytest.mark.parametrize("name", ("Alex", "Nik", 321, ""))
    def test_add_new_hobbit(self, hobbits, name):
        hobbits.add_new_hobbit(name)

        assert hobbits.hobbits_miles[name] == 0

    def test_delete_hobbit(self, hobbits):
        # name = add_new_hobbit
        name = "Alex"
        hobbits.remove_hobbit(name)
        assert name not in hobbits.hobbits_miles.keys()
