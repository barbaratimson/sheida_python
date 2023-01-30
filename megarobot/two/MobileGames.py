from games import *
class MobileGames(Games):
    def __init__(self, name, osType):
        super().__init__(name)
        self.osType = osType
    def getName(self):
        print("Название игры: ")
        return super().getName()

