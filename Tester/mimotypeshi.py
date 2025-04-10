class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def greet(self):
        print("Hi!")

class Nurse(Person):
    def __init__(self, name, age):
        super().__init__("Nurse " + name, age)
    
    def intro(self):
        print("Hi, I'm", self.name)
    def introo(self):
        print("Hi, I'm a fatass introooooo", self.name, self.age, "yea")

class Dokter(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
    def adres(self):
        print("Hallo jongeman!")
    def adress(self):
        print("Hallo kerel!")
    def adresss(self):
        print("YOOOOO KEEERRllll")

class Journalist(Dokter):
    def __init__(self, name, age):
        super().__init__(name, age)

person1 = Nurse("Sam", 23)
person2 = Dokter("Kees", 24)
person3 = Dokter("Jan", 25)
person4 = Dokter("Henk", 26)



person2.adress()
person4.adresss()