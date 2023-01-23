from os import environ

from dotenv import load_dotenv


class Car:
    """
    Class represents a car
    """
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

    def start_drive(self, current_road_km=int(environ["DEFAULT_VALUE_KM"]),
                    current_gear=int(environ["DEFAULT_VALUE_GEAR"])):
        """
        Name: Ofri Shapira\n
        Date: 22/1/22\n
        Method to start the drive.
        :param current_road_km: the km number to drive
        :param current_gear: the gear value
        :return: true if the car complete the drive
        """
        # check fot the type validity of the method arguments
        if not isinstance(current_road_km, (int, float)):
            raise TypeError(environ["TYPE_ERROR"].format('km'))
        if not isinstance(current_gear, (int, float)):
            raise TypeError(environ["TYPE_ERROR"].format('gear'))

        # if the engine is off, start it
        if not self.is_engine_on:
            self.start_engine()

        # if the drive mode is on - throw exception
        if self.is_drive_on:
            raise ValueError(environ["DRIVE_ERROR_1"])

        # if the gear that been inserted is out of boundaries, throw exception
        if current_gear > int(environ["GEAR_MAX"]) or current_gear <= 0:
            raise OverflowError(environ["GEAR_ERROR_1"])

        # if the km value is higher than what the car can drive, according to its fuel, throw exception
        if current_road_km > self.fuel * int(environ["LITER_T0_KM"]):
            raise OverflowError(environ["KM_TOO_HIGH"])

        # if we reached here, start the drive
        else:
            print(environ["DRIVE_START"])
            self.is_drive_on = True
            self.consume(current_road_km)
            return True

    def stop_drive(self):
        """
        Name: Ofri Shapira\n
        Date: 22/1/22\n
        Method to stop the drive mode
        :return: True if the drive stopped successfully
        """
        # if the drive mode is already off, throw an error
        if not self.is_drive_on:
            raise ValueError(environ["DRIVE_ERROR_2"])

        # stop the drive
        else:
            print(environ["DRIVE_FINISHED"])
            self.is_drive_on = False
            return True

    def start_engine(self):
        """
        Name: Ofri Shapira\n
        Date: 22/1/22\n
        Method to start the engine
        :return: True if the engine start successfully
        """
        # if the engine is already on, throw error
        if self.is_engine_on:
            raise ValueError(environ["ENGINE_ERROR_2"])

        # start the engine
        else:
            print(environ["ENGINE_START"])
            self.is_engine_on = True
            return True

    def stop_engine(self):
        """
        Name: Ofri Shapira\n
        Date: 22/1/22\n
        Method to stop the engine.
        :return: True if the engine stopped successfully
        """
        # if the engine is already off, throw error
        if not self.is_engine_on:
            raise ValueError(environ["ENGINE_ERROR_1"])

        # stop the engine
        else:
            self.is_engine_on = False
            print(environ["ENGINE_STOP"])
            return True

    def add_fuel(self, fuel_to_add):
        """
        Name: Ofri Shapira\n
        Date: 22/1/22\n
        Method to add fuel to the tank.
        :param fuel_to_add: the amount of fuel to add
        :return: True if the fuel been added successfully
        """
        #  check if the engine is off
        if self.is_drive_on or self.is_engine_on:
            raise PermissionError(environ["PERMISSION_ERROR"])

        #  check if the fuel amount value is of the right type
        if not isinstance(fuel_to_add, (int, float)):
            raise TypeError(environ["TYPE_ERROR"].format('fuel level value'))

        # check if the fuel amount value is below 0
        if fuel_to_add < 0:
            raise ValueError(environ["VALUE_ERROR"].format('fuel'))

        # check if the fuel amount to add is valid, if so, add it to the tank
        if fuel_to_add + self.fuel > float(environ["FUEL"]):
            raise OverflowError(environ["FUEL_ERROR_TOO_HIGH"])

        if fuel_to_add * float(environ["FUEL_PRICE"]) > float(environ["MONEY"]):
            raise OverflowError(environ["FUEL_ERROR_TOO_EXPENSIVE"])

        # if we reached here, we can add the fuel into the tank
        self.fuel += fuel_to_add
        self.money -= (fuel_to_add * float(environ["FUEL_PRICE"]))
        print(environ["ADDED_FUEL"].format(fuel_to_add, self.fuel, self.money))
        return True

    def consume(self, km):
        """
        Name: Ofri Shapira\n
        Date: 22/1/22\n
        Method to calculate the consumption and apply it
        :param km: the km value that the car drove
        :return: True if the car consumed successfully
        """
        # check if the km value is negative
        if km < 0:
            raise ValueError(environ["VALUE_ERROR"].format('km'))

        # check if the km value is int or float, otherwise throw exception
        if not isinstance(km, (int, float)):
            raise TypeError(environ["TYPE_ERROR"].format('km'))

        # convert the km to liters
        liter_to_fuel = km / float(environ["LITER_T0_KM"])
        if liter_to_fuel > float(environ["FUEL"]):
            raise OverflowError(environ["KM_TOO_HIGH"])
        else:
            self.fuel -= liter_to_fuel
            return True

    def get_current_car_status(self):
        """
        Name: Ofri Shapira\n
        Date: 22/1/22\n
        Method to get the current car status
        :return: String represent the car status
        """
        return environ["CURRENT_STATUS"].format(self.fuel, self.money)
