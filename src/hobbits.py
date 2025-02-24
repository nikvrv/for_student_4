class HobbitsPriorityStatus:
    def __init__(self):
        self.hobbits_miles = {"Frodo": 505, "Sam": 499, "Merry": 350, "Pippin": 350}

    def add_new_hobbit(self, hobbit_name):
        if not isinstance(hobbit_name, str):
            raise ValueError
        if hobbit_name not in self.hobbits_miles.keys():
            self.hobbits_miles[hobbit_name] = 0

    def remove_hobbit(self, hobbit_name):
        if hobbit_name in self.hobbits_miles.keys():
            del self.hobbits_miles[hobbit_name]
        else:
            raise ValueError("There are not hobbits")

    def add_miles_to_hobbit(self, hobbit_name, miles):
        if self.hobbits_miles.get(hobbit_name) is not None:
            self.hobbits_miles[hobbit_name] = miles

    def get_status(self, hobbit_name):
        if not self.hobbits_miles.get(hobbit_name):
            return ""

        if self.hobbits_miles[hobbit_name] < 300:
            return "Classic"

        if 300 <= self.hobbits_miles[hobbit_name] < 400:
            return "Silver"

        if 400 <= self.hobbits_miles[hobbit_name] < 500:
            return "Gold"

        if self.hobbits_miles[hobbit_name] >= 500:
            return "Platinum"
