class Carpark:
    def __init__(self,
                 location="Unknown",
                 capacity=0,
                 current_vahicle_count=0,
                 sensors=None,
                 displays=None):
        self.capacity = capacity
        self.current_vehicle_count = current_vahicle_count
        self.location = location
        self.displays = displays or []
        self.sensors = sensors or []
    def __str__(self):
        return f"Carpark at {self.location} with a capacity of {self.capacity} vehicles"

