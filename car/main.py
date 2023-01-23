from car.car_ex import Car
from car.utils import Utils

if __name__ == "__main__":
    try:
        car = Car()
        # car.start_drive(300, 2)
        # car.add_fuel(2)
        # car.stop_engine()
        # car.add_fuel(44)
        # car.start_drive(4444, 2)
        # car.stop_engine()
        # car.start_engine()
        #
        # car.start_drive(1001, 3)
        #
        # car.get_current_car_status()
        # car.add_fuel(10)
    except BaseException as e:
        Utils.write_to_log(str(e))
        print(e)
