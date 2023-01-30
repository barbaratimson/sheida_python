from myClass import *

class MySecondClass(Myclass):
    def __init__(self,number,field):
        super().__init__(field)
        self.number = number
    