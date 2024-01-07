from sensor import Sensor
from display import Display
from pathlib import Path
from datetime import datetime
import json

class CarPark:
    def __init__(self,
                 location,
                 capacity,
                 plates=None,
                 sensors=None,
                 displays=None,
                 log_file=Path("log.txt"),
                 config_file=Path("config.json")):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.displays = displays or []
        self.sensors = sensors or []
        # convert file name to path and create it
        self.log_file = log_file if isinstance(log_file, Path) else Path(log_file)
        # create the file if it doesn't exist:
        self.log_file.touch(exist_ok=True)

    def to_json(self, file_name):
        with open(file_name,"w") as file:
            json.dump({"location": self.location,
                       "capacity": self.capacity,
                       "log_file": str(self.log_file)}, file)

    @staticmethod
    def from_json(file_name):
        """Allows the creation of an instance of a car park from json.
        >>>car_park = CarPark.from_json('some_file.txt')
        """

        with open(file_name, "r") as file:
            conf = json.load(file)
        return CarPark(location=conf["location"],
                       capacity=int(conf["capacity"]),
                       log_file=conf["log_file"])

    @property
    def available_bays(self):
        # car_park.available_bays
        return max(0, self.capacity - len(self.plates))
    def __str__(self):
        return f"Carpark at {self.location} with a capacity of {self.capacity} vehicles"

    def register(self, component):
        """Registers component of a car park"""
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Invalid component type!")

        if isinstance(component, Sensor):
            self.sensors.append(component)
        elif isinstance(component, Display):
            self.sensors.append(component)

    def _log_car(self, action, plate):
        with self.log_file.open(mode='a') as file:
            file.write(f'{plate} {action} on the {datetime.now().strftime("%d-%m %H:%M")}\n')
    def add_car(self,plate):
        self.plates.append(plate)
        self._log_car("entered", plate)


    def remove_car(self,plate):
        self.plates.remove(plate)
        self._log_car("exited", plate)


    def update_displays(self):
        for display in self.displays:
            display.update({"Bays": self.available_bays,
                            "Temperature": 42}
                           )
            print(f"Updating: {display}")

    def _log_car_activity(self, plate, action):
        with self.log_file.open("a") as f:
            f.write(f"{plate} {action} at {datetime.now()}\n")

    def write_config(self):
        with open("config.json", "w") as f:  # TODO: use self.config_file; use Path; add optional parm to __init__
            json.dump({"location": self.location,
                       "capacity": self.capacity,
                       "log_file": str(self.log_file)}, f)

    @staticmethod
    def from_config(config_file=Path("config.json")):
        config_file = config_file if isinstance(config_file, Path) else Path(config_file)
        with config_file.open() as f:
            config = json.load(f)
        return CarPark(config["location"], config["capacity"], log_file=config["log_file"])