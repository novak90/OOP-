from random import randint

class Vehicle:
    def __init__(self,engine,brand,speed,oil_brand):
        self.engine = engine
        self.brand = brand
        self.speed = speed
        self.oil_brand = oil_brand

    def start_engine(self):
            if not Vehicle["engine_on"] and Vehicle["reserve"] > 0:
                Vehicle["engine_on"] = True
                return "Двигатель запущен."
            return "Двигатель уже был запущен."


    def stop_engine(self):
        if Vehicle["engine_on"]:
            Vehicle["engine_on"] = False
            return "Двигатель остановлен."
        return "Двигатель уже был остановлен."

    def get_brand(self):
        return f"Бренд вентилятора {self['Brand']}."

    def get_oil_brand(self):
        return f"бренд масла {self['oil_brand']}."

    def get_speed(self):
        self.speed = randint(1, 1000)

class Plane(Vehicle):
    def __init__(self,engine,brand,speed,oil_brand):
        super(). __init__(engine,brand,speed,oil_brand)


class Car (Vehicle):

    if __name__ == "__main__":
    # Write your solution here
    pass