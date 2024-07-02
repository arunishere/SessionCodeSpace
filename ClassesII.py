'''

Oops Concepts

1.Instance / Object
2.Method - Function inside a Class
3.self - the instance itself
4.instance attributes - attributes that are specific for a particular instance (instance members)
5.class attributes - attributes that belong to a class which are independent from an instance (class members)
6.Instance Method
7.Class Method or Static Method
8.mutatator method
9. accessor method

'''

class Person:

    version = 3.0
    person_count = 0

    def __init__(self, name, age, location):

        self.name = name
        self.age = age
        self.location  = location

        Person.person_count += 1

    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age
    
    def getLocation(self):
        return self.location
    
    def setName(self, name):
        self.name = name

    def setAge(self, age):
        self.age = age

    def setLocation(self, location):
        self.location  = location

    @staticmethod
    def getVersion():
        return Person.version
    
    @staticmethod
    def getCount():
        return Person.person_count

person_1 = Person('Jack', 32, "Chicago")
person_2 = Person('Celene', 29, "Manchester")
person_3 = Person('Tori', 30, "Manila")

person_2.setLocation('Convertry')
print(person_2.getVersion())