class Temperature:
    def __init__(self, celsius=0):
        self.__celsius = celsius

    @property
    def celsius(self):
        return self.__celsius

    @celsius.setter
    def celsius(self, temp):
        if temp < -273.15:
            raise ValueError("Temperature cannot be below 273.15")
        self.__celsius = temp


t = Temperature(25)
print(t.celsius)
t.celsius = -300
