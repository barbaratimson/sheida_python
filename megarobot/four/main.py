from mySecondClass import *

def main ():
    a = MySecondClass("FSFSDFS",6456456)
    print(a.field)
    print(a.number)
    a.setField()
    print(a.field)
    a.setField("dd")
    print(a.field)
if __name__ == "__main__":
    main()