class Book:
    def __init__(self,bookname,authorname,translatorname,isbn,genre,publisher,yearpublication):
        self._bookname=bookname
        self._authorname=authorname
        self._translatorname=translatorname
        self._isbn=isbn
        self._genre=genre
        self._publisher=publisher
        self._yearpublication=yearpublication

    def get_list(self):
        basket=[self._bookname,self._authorname,self._translatorname,self._isbn,self._genre,self._publisher,self._yearpublication]
        return basket