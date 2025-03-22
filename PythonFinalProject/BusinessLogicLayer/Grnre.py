class Genre:
    generlist = {1: "specialized", 2: "romance", 3: "Fantasy", 4: "Classic", 5: "Art", 6: "Scary", 7: "crime",
                  8: "comedy", 9: "historical", 10: "literary"}

    def __init__(self, genre):
        self._genre = genre

    def __is_fill(self):
        if self._genre:
            return True
        else:
            return False

    def __is_in_List(self):
        key_list=self.generlist.keys()
        if not self._genre.isdecimal() :
            return  False
        if int(self._genre) in key_list :
                return  True
        return False

    def is_valid_genre(self):
        if self.__is_fill() and self.__is_in_List() :
            return  True
        return  False

    def get_genre_name(self):
            return self.generlist[int(self._genre)]
