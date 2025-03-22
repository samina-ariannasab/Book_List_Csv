class Name:
    def __init__(self, name):
        self._name = name

    def __is_fill(self):
        if self._name:
            return True
        else:
            return False

    def __check_name(self, charlist):
        for char in self._name:
            if not('a' <= char.lower() <= 'z' )  :
                if not(char in charlist) :
                    return False
        return True

    def is_valid_name_mandatory(self,charlist):
        if self.__is_fill() and self.__check_name(charlist):
            return True
        return False

    def is_valid_name_non_mandatory(self,charlist):
        if  self.__check_name(charlist):
            return True
        return False

    def get_data(self):
        return self._name
