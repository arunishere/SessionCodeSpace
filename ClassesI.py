class Car:

    Count = 0

    def __init__(self, brand, model):

        self.brand = brand
        self.model = model
        Car.Count += 1

    def className():

        print("We are inside the Class Car")

    def classAdd(a,b):

        print("We can add number using this class", a+b)

    def carDetails(self):

        print('Model: ', self.model)
        print('Brand:', self.brand)

    def getCount():
        print('Total Instances: ', Car.Count)


car1 = Car('BMW', 'X3')
# car1.carDetails()

car2 = Car('Kia', 'Seltos')
# car2.carDetails()

# car2.Country

car3 = Car('Volvo', 'V40')

Car.getCount()