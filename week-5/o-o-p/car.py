class Car():
    def __init__(self, brand, color):
        print("Creating Car...")
        self.color = color
        self.engine_started = False
        self.brand = brand

    def start_engine(self):
        self.engine_started = True

    def stop_engine(self):
        self.engine_started = False        

    def acceleration(self):
        if self.engine_started:
            print("Accelerating to the speed of sound..")
        else:
            print("Start the engine first...")  

    def display_info(self):
        print(f"My {self.brand}'s {self.color}")




my_car = Car("Toyota", "White")

my_car.start_engine()

my_car.acceleration()

my_car.stop_engine()

my_car.acceleration()








another_car = Car("Porsche", "Red")

another_car.acceleration()




my_garage = []
my_garage.append(my_car)
my_garage.append(another_car)

