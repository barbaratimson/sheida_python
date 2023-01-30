class Person:
    def __init__(self, n, s, qual = 1):
        self.name = n
        self.surname = s
        self.qual = qual
    def getInf (self):
        return f"{self.name} {self.surname} {self.qual}"
    def __del__(self):
        return f"До свидания мистер {self.name} {self.surname}"

def main ():
    a = Person("Андрей","Климов",1)
    b = Person("Никита","Буянов",2)
    c = Person("Боба","Абоба",3)
    print(f"{a.getInf()}\n{b.getInf()}\n{c.getInf()}")
    print(a.__del__())
    input()

if __name__ == "__main__":
    main()
