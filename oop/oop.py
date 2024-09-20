class Oop:
    num=0
    def __init__(self,make,model,year,color):
        self.make=make
        self.model=model
        self.year=year
        self.color=color
        Oop.add_car

    def drive(self):
        print("drive")

    def stop(self):
        print("stop")

    @classmethod
    def number(cls):
        return cls.num
    @classmethod
    def add_car(cls):
        cls.num+=1


class Tank(Oop):
    def speak(self):
        print("yes I am")

