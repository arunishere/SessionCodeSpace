class Date:


    def __init__(self, day, month, year):

        self.day = day
        self.month = month
        self.year = year


    def getDate(self):

        return f'{self.day}-{self.month}-{self.year}'


class Time:


    def __init__(self, hours, minutes, seconds="00"):

        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds


    def getTime(self):

        return f'{self.hours}:{self.minutes}:{self.seconds}'


class Appointment(Date, Time):

    def __init__(self, name, age, doctor, day, month, year, hours, minutes):

        Date.__init__(self, day, month, year)
        Time.__init__(self,  hours, minutes)

        self.name = name
        self.age = age
        self.doctor = doctor


    def getData(self):

        print('Appointment Details')
        print('===========================')
        print(f'Appointment Date & Time: {self.getDate() + " " + self.getTime()} \n Name: {self.name} \n Patient Age: {self.age} \n Doctor: {self.doctor}')




