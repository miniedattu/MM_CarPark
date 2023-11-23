from sensor import Sensor
from display import Display
class CarPark:
    def __init__(self,
                 location,
                 capacity,
                 plates=None,
                 sensors=None,
                 displays=None):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.displays = displays or []
        self.sensors = sensors or []
    def __str__(self):
        return f"Carpark at {self.location} with a capacity of {self.capacity} vehicles"

    def register(self, component):
        """Registers component of a car park"""
        if not isinstance(component,(Sensor,Display)):
            raise TypeError("Invalid component type!")

        if isinstance(component,Sensor):
            self.sensors.append(component)
        elif isinstance(component,Display):
            self.sensors.append(component)

    def add_car(self,plate):
        self.plates.append(plate)

    def remove_car(self,plate):
        self.plates.remove(plate)

    def update_displays(self):
        for display in self.display:
            display.update()
            print(f"Updating: {display}")