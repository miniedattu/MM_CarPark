from car_park import CarPark
from sensor import Sensor
from display import Display
from sensor import EntrySensor
from sensor import ExitSensor

def main():
    # create a car park
    car_park=CarPark(location="Moondalup", capacity=100)
    # Create displays and sensors
    main_display = Display(id=1, car_park=car_park)
    entry_sensor = EntrySensor(id=2, car_park=car_park)
    exit_sensor = ExitSensor(id=3, car_park=car_park)

    # Register displays and sensors with the car park
    car_park.register(main_display)
    car_park.register(entry_sensor)
    car_park.register(exit_sensor)

    # Simulate car detection and entry
    entry_sensor.detect_vehicle()

    # Update displays with the current status
    car_park.update_displays()

    # Simulate car leaving
    exit_sensor.detect_vehicle()

    # Update displays after exit
    car_park.update_displays()


if __name__ == "__main__":
    main()


# THE END!!!!!!!!!!!