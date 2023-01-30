from MobileGames import *
from PCGames import *
from PS4Games import *
from XboxGames import *
def main ():

    a = PCGames("Booba","Action")
    a.setYear(2004)
    print(a.getName() + " " + a.genre)
    print(a.year)

    b = MobileGames("Aboba","Android")
    b.setYear(2011)
    print(b.getName() + " " + b.osType)
    print(b.year)

    c = PS4Games("Bebes","Roguelike","PS4 Slim")
    c.setYear(2016)
    print(c.getName() + " " + c.genre + " " + c.consoleModel)
    print(c.year)

    d = XboxGames("YesYeS","FPS","NextGen")
    d.setYear(2015)
    print(d.getName() + " " + d.genre + " " + d.generation)
    print(d.year)
if __name__ == "__main__":
    main()
