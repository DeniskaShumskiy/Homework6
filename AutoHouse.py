from enum import Enum

class Workers(Enum):
    director = 1
    accounting = 2
    managers = 3
    mechanics = 4

class Total_employees:
    Total = 10

    def __init__(self, a):
        self.a = a

    @classmethod
    def new_employees(cls):
        cls.Total += 1

    @staticmethod
    def number_of_employees():
        return 10



print(f"Кол-во работников в автосалоне {Total_employees.number_of_employees()}")
a = Total_employees(1)
a.new_employees() # добавился один работник
print(f"Теперь работников в автосалоне {Total_employees.Total}")

class Auto:
    def __init__ (self,
                  model: str,
                  motor: float,
                  color: str,
                  acceleration: float
                  ) -> None:
        self.model = model
        self._motor = motor
        self.color = color
        self.acceleration = acceleration

    def __gt__(self, other):
        if isinstance(other, Auto):
            return self._motor > other._motor
        raise ValueError("Нужен экземпляр класса Auto или Moto")


    def __ge__(self, other):
        if isinstance(other, Auto):
            return self._motor >= other._motor
        raise ValueError("Нужен экземпляр класса Auto или Moto")


    def __eq__(self, other):
        if isinstance(other, Auto):
            return self._motor == other._motor
        raise ValueError("Нужен экземпляр класса Auto или Moto")


    def __ne__(self, other):
        if isinstance(other, Auto):
            return self._motor != other._motor
        raise ValueError("Нужен экземпляр класса Auto или Moto")


    def __lt__(self, other):
        if isinstance(other, Auto):
            return self._motor < other._motor
        raise ValueError("Нужен экземпляр класса Auto или Moto")


    def __le__(self, other):
        if isinstance(other, Auto):
            return self._motor <= other._motor
        raise ValueError("Нужен экземпляр класса Auto или Moto")

    def __len__(self):
            return len(self.model)


class Moto(Auto):
    def __init__ (self,
                  model: str,
                  motor: float,
                  color: str,
                  acceleration: float
                  ) -> None:
        super().__init__(model, motor, color, acceleration)

class Prices(Moto, Auto):
    def __init__(self, BMW_E90, AUDI_A6, DODGE,
                 FORD, ACURA, TOYOTA,
                 Suzuki, Kawasaki, Honda,
                 Yamaha: int,
                 ):
        self.BMW_E90 = BMW_E90
        self.AUDI_A6 = AUDI_A6
        self.DODGE = DODGE
        self.FORD = FORD
        self.ACURA = ACURA
        self.TOYOTA = TOYOTA
        self.Suzuki = Suzuki
        self.Kawasaki = Kawasaki
        self.Honda = Honda
        self.Yamaha = Yamaha


# Auto
BMW_E90 = Auto("BMW", 3.0, "Black", 7.5)
AUDI_A6 = Auto("AUDI", 2.5, "Yellow", 8.2)
DODGE = Auto("DODGE", 6.7, "Black", 4.5)
FORD = Auto("FORD", 2.0, "Yellow", 6.2)
ACURA = Auto("ACURA", 3.2, "White", 6.1)
TOYOTA = Auto("TOYOTA", 3.0, "Orange", 7.0)
# Moto
Suzuki = Moto("Suzuki", 1.0, "Black", 3.0)
Kawasaki = Moto("Kawasaki", 1.0, "Yellow", 3.1)
Honda = Moto("Honda", 1.0, "White", 3.2)
Yamaha = Moto("Yamaha", 1.0, "White", 3.3)

# Сравнить больше ли объём двигателя у Acura, чем у Yamaha

print(ACURA > Yamaha)

price = Prices(30000, 20000,25000,
               27000,32000,15000,
               10000,9000,11000,
               12000
               )

# Нужно вывести стоимость BMW и Audi

print(f"Стоимость BMW {price.BMW_E90}$, Стоимость Audi {price.AUDI_A6}$")



