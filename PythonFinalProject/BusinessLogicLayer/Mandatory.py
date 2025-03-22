class Mandatory:
    def __init__(self, name):
        self._name = name

    def __is_fill(self):
        if self._name:
            return True
        else:
            return False

    def is_valid_mandatory(self):
        if self.__is_fill():
            return True
        return False

    def get_data(self):
        return self._name



