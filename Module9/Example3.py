class Animal:
    def __init__(self,name):        #shembulli per ni konstruktor dhe nje variabel e cila po inciohet per kete klase
        self.name=name


    def sound(self):
        print("Some generic animal song")

    def description(self):
        print(f"This is an animal named{self.name}")

class Dog(Animal):

    def __init__(self, breed, name):            #ketu eshte konstruktori i klases dhe ketu eshte variabla e klases
        self.breed=breed                            #variabla qe vlen vetem per kete klase
        super().__init__(name)                           #ketu thirret konstruktori i superklases

    def sound(self):
        print("Woof! woof!")

    def description(self):
        super().description()
        print(f"Breed:{self.breed}")

class Cat(Animal):
    def __init__(self,color,name):
        self.color=color
        super().__init__(name)


class Cat(Animal):
    def sound(self):
        print("Meow! Meow!")

    def description(self):
        super().description()
        print(f"Color:{self.color}")

rex=Dog("Golden Retriver", "Rex")
rex.sound()
rex.description()

cat = Cat("Black Retrivr", "Rex")
rex.sound()
rex.description()

cat=Cat("Black","Tom")
cat.sound()
cat.description()
#kafshe=Animal()
#kafshe.sound()
#rex=Dog()
#rex.sound()
#tom=Cat()
#tom.sound()