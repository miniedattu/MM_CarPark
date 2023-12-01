import unittest
from car_park import CarPark
from sensor import ConcreteSensor

class TestSensor(unittest.TestCase):
    def test_init_method(self):
        car_park = CarPark(location="Test Location", capacity=100)
        sensor = ConcreteSensor(id=1, car_park=car_park, is_active=True)

        self.assertEqual(sensor.id, 1)
        self.assertEqual(sensor.car_park, car_park)
        self.assertTrue(sensor.is_active)

    def test_detect_vehicle_method(self):
        car_park_mock = CarPark(location="Test Location", capacity=100)
        sensor = ConcreteSensor(id=1, car_park=car_park_mock)

        # Mock the _scan_plate method for testing purposes
        original_scan_plate = sensor._scan_plate
        sensor._scan_plate = lambda: "TEST123"

        try:
            # Capture the logs during detect_vehicle
            with self.assertLogs() as log:
                sensor.detect_vehicle()

            # Assert that the log contains the expected message
            self.assertIn("Incoming 🚘 vehicle detected. Plate: TEST123", log.output[0])

        finally:
            # Restore the original _scan_plate method
            sensor._scan_plate = original_scan_plate

if __name__ == '__main__':
    unittest.main()
