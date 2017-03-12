class PhoneBook:
    def __init__(self):
        self.entries = {}  # Empty dict

    def add(self, name, number):
        self.entries[name] = number

    def lookup(self, name):
        return self.entries[name]

    def is_consistent(self):
        values = [values for key, values in self.entries.items()]
        for i in values:
            if values.count(i) > 1:
                return False
        return True
