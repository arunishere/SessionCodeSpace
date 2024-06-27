class Person:

    version = 3.0
    person_count = 0

    def __init__(self):

        Person.person_count += 1

    def setValues(self, name, age, location):

        self.name = name
        self.age = age
        self.location  = location

    def getValues(self):
        return self.name, self.age, self.location

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

person_1 = Person()
person_2 = Person()
person_3 = Person()

# person_2.setLocation('Convertry')
# print(person_2.getVersion())

person_1.setValues('Jack', 32, "Chicago")
# print(person_1.getValues())

print(person_1.age)