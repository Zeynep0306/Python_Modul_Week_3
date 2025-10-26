class Vehicle :
    def __init__(self, make, model, year):
        self.make= make
        self.model= model
        self.year= year

    def __str__(self):
        return f"Araba bilgisi: {self.year} {self.model} {self.make}"

class Off_road_vehicle(Vehicle):
    def __init__(self, make,model,year,four_wheel_drive):
        super().__init__(make,model,year)
        self.four_wheel_drive= four_wheel_drive
    def __str__(self):
        super().__str__()
        print(f"Four Wheel Drive:  {'YES' if self.four_wheel_drive else 'NO'}")


class Sports_car(Vehicle):
    def __init__(self, make,model,year, max_speed):
        super().__init__(make,model,year)
        self.max_speed= max_speed
    def __str__(self):
        super().__str__()
        print(f"Max Speed: {self.max_speed} km/h ")

my_offroad= Off_road_vehicle( "Land Rover", 'Defender', 2024, True)
my_offroad.__str__()

my_sports_car= Sports_car("Ferrari", "F8 tributo",2023, 340)
my_sports_car.__str__()
