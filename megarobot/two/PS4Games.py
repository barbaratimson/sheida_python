from games import *
class PS4Games(Games):
    def __init__(self, name, genre, consoleModel):
        super().__init__(name)
        self.consoleModel = consoleModel
        self.genre = genre
    def getName(self):
        print("Название игры: ")
        return super().getName()

