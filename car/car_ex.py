from os import environ

from dotenv import load_dotenv

from car.utils import Utils


class Car:
    load_dotenv()

    def __init__(self):
        """
        Name: Ofri Shapira\n
        Date: 22/1/22\n
        Constructor for the car class.
        """
        self.gear = float(environ["GEAR"])
        self.money = float(environ["MONEY"])
        self.fuel = float(environ["FUEL"])
        self.is_drive_on = False
        self.is_engine_on = False

    def start_drive(self):
        """
        Name: Ofri Shapira\n
        Date: 22/1/22\n
        Method to start the drive.
        :return: None
        """
        if not self.is_engine_on:
            print(environ["ENGINE_ERROR_1"])
            raise Exception(environ["ENGINE_ERROR_1"])
        if self.is_drive_on:
            #
            print(environ["DRIVE_ERROR_1"])
            raise Exception("DRIVE_ERROR_1")
        print("start driving…")
        current_road_km = int(input("Enter km: "))
        current_gear = int(input("Enter gear, between 1-6: "))
        if current_gear > int(environ["GEAR_MAX"]) or current_gear <= 0:
            raise ValueError(environ["GEAR_ERROR_1"])
        else:
            self.consume(current_road_km)
            self.is_drive_on = True
            print(f"Drove {current_road_km} km successfully...")
            self.get_current_car_status()
            self.stop_drive()

    def stop_drive(self):
        """
        Name: Ofri Shapira\n
        Date: 22/1/22\n
        Method stop the drive mode
        :return: None
        """
        if not self.is_drive_on:
            print(environ["DRIVE_ERROR_2"])
            raise ValueError(environ["DRIVE_ERROR_2"])
        else:
            self.is_drive_on = False

    def start_engine(self):
        """
        Name: Ofri Shapira\n
        Date: 22/1/22\n
        Method to start the engine.
        :return: None
        """
        if self.is_engine_on:
            print(environ["ENGINE_ERROR_2"])
            raise ValueError(environ["ENGINE_ERROR_2"])
        else:
            print("Engine started")
            self.is_engine_on = True

    def stop_engine(self):
        """
        Name: Ofri Shapira\n
        Date: 22/1/22\n
        Method to stop the engine.
        :return: None
        """
        if not self.is_drive_on:
            print(environ["ENGINE_ERROR_1"])
            raise ValueError(environ["ENGINE_ERROR_1"])
        else:
            self.is_engine_on = False
            print("Engine is stopped")

    def add_fuel(self):
        """
        Name: Ofri Shapira\n
        Date: 22/1/22\n
        Method to add fuel to the tank.
        :return: None
        """
        fuel_to_add = float(input("Enter fuel amount: "))
        if fuel_to_add + self.fuel > int(environ["FUEL"]):
            print(environ["FUEL_ERROR_TOO_HIGH"])
            raise OverflowError(environ["FUEL_ERROR_TOO_HIGH"])
        elif fuel_to_add * int(environ["FUEL_PRICE"]) > float(environ["MONEY"]):
            print(environ["FUEL_ERROR_TOO_EXPENSIVE"])
            raise OverflowError(environ["FUEL_ERROR_TOO_EXPENSIVE"])
        else:
            self.fuel += fuel_to_add
            self.money -= (fuel_to_add * 10)

    def consume(self, km):
        """
        Name: Ofri Shapira\n
        Date: 22/1/22\n
        Method to calculate consume and apply it.
        :return: None
        """
        liter_to_fuel = km / int(environ["LITER_TO_FUEL"])
        if liter_to_fuel > int(environ["FUEL"]):
            print(environ["KM_TOO_HIGH"])
            raise OverflowError(environ["KM_TOO_HIGH"])
        else:
            self.fuel -= liter_to_fuel

    def get_current_car_status(self):
        """
        Name: Ofri Shapira\n
        Date: 22/1/22\n
        Method to get the current car status.
        :return: None
        """
        print(f"Current status is: fuel: {self.fuel}, money: {self.money}")

    def show_options(self):
        """
        Name: Ofri Shapira\n
        Date: 22/1/22\n
        Method to show the options to the user.
        :return: None
        """
        print(
            "Options: \n1. Start Drive\n2. Start Engine\n3. Stop Engine\n4. Add fuel\n5. Get Car Status")
        try:
            option_selected = int(input("Enter Option: "))
            if not isinstance(option_selected, int):
                print(environ["The option must be e number"])
            else:
                if option_selected == 1:
                    self.start_drive()
                elif option_selected == 2:
                    self.start_engine()
                elif option_selected == 3:
                    self.stop_engine()
                elif option_selected == 4:
                    self.add_fuel()
                elif option_selected == 5:
                    self.get_current_car_status()
                else:
                    print(environ["NO_OPTION"])
        except BaseException as e:
            Utils.write_to_log(str(e))
        finally:
            self.show_options()
