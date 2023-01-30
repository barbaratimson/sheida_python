from canada import *
from germany import *
from russia import *

def main ():
    a = Canada()
    a.setPopulation(100000)
    print(a.getPopulation())

    b = Russia()
    b.setPopulation(2000000)
    print(b.getPopulation())

    c = Germany()
    c.setPopulation(10000)
    print(c.getPopulation())
if __name__ == "__main__":
    main()