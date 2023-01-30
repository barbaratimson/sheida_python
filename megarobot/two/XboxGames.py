from games import *
class XboxGames(Games):
    def __init__(self, name, genre, generation):
        super().__init__(name)
        self.generation = generation
        self.genre = genre
    def getName(self):
        print("Название игры: ")
        return super().getName()

