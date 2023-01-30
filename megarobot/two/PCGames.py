from games import *
class PCGames(Games):
    def __init__(self, name, genre):
        super().__init__(name)
        self.genre = genre
    def getName(self):
        print("Название игры: ")
        return super().getName()

