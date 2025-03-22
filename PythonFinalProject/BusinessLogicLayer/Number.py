class Number :
    def __init__(self, number):
        self._number = number


    def __check_number(self):
        if self._number.isdecimal()  :
            return True
        else:
            return False

    def __check_len_number(self,minlen=0,maxlen=0):
       if minlen >0 :
           if len(self._number) >= minlen :
              return False

       if maxlen >=0 :
           if len(self._number)<maxlen :
               return  False
       return  True

    def is_valid_number(self,minlen=0,maxlen=0):
        if self.__check_number() and self.__check_len_number(minlen,maxlen) :
            return  True
        return  False


    def get_data(self):
        return self._number
