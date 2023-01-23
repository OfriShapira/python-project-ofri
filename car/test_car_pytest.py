import inspect
from os import environ

import pytest as pytest
from dotenv import load_dotenv

from car.car_ex import Car
from car.utils import Utils


@pytest.fixture
def car():
    load_dotenv()
    return Car()


@pytest.mark.start_drive
@pytest.mark.parametrize("current_km, gear", [(300, 2), (1000, 1), (200, 6)])
def test_start_drive_returns_true(car, current_km, gear):
    """
    Test to check if the method returns the true
    :param car: the car object
    :param current_km: the kilometers value dor the drive
    :param gear: the gear value for the drive
    :return: None
    """
    try:
        assert car.start_drive(current_km, gear) is True
        Utils.write_to_log(environ["TEST_PASS_WITH_PARAMS"].format(inspect.stack()[0][3], (current_km, gear)))
    except BaseException as b:
        Utils.write_to_log(environ["TEST_FAIL_NO_PARAMS"].format(inspect.stack()[0][3], (current_km, gear), b))


@pytest.mark.start_drive
def test_start_drive_raise_value_error(car):
    """
    Test to check if the method throws the right exceptions
    :param car: the car object
    :return: None
    """
    car.start_drive()
    try:
        with pytest.raises(ValueError):
            car.start_drive()
        Utils.write_to_log(environ["TEST_PASS_NO_PARAMS"].format(inspect.stack()[0][3]))

    except BaseException as b:
        Utils.write_to_log(environ["TEST_FAIL_NO_PARAMS"].format(inspect.stack()[0][3], b))


@pytest.mark.start_drive
@pytest.mark.parametrize("current_km, gear", [("a", 3), (3, "a")])
def test_start_drive_raise_type_error(car, current_km, gear):
    """
    Test to check if the method throws the right exceptions
    :param car: the car object
    :return: None
    """
    try:
        with pytest.raises(TypeError):
            car.start_drive(current_km, gear)
        Utils.write_to_log(environ["TEST_PASS_WITH_PARAMS"].format(inspect.stack()[0][3], (current_km, gear)))

    except BaseException as b:
        Utils.write_to_log(environ["TEST_FAIL_WITH_PARAMS"].format(inspect.stack()[0][3], (current_km, gear), b))


@pytest.mark.start_drive
@pytest.mark.parametrize("current_km, gear", [(3, 7)])
def test_start_drive_raise_over_flow(car, current_km, gear):
    """
    Test to check if the method throws the right exceptions
    :param car: the car object
    :return: None
    """
    try:
        with pytest.raises(OverflowError):
            car.start_drive(current_km, gear)

        Utils.write_to_log(environ["TEST_PASS_WITH_PARAMS"].format(inspect.stack()[0][3], (current_km, gear)))

    except BaseException as b:
        Utils.write_to_log(environ["TEST_FAIL_WITH_PARAMS"].format(inspect.stack()[0][3], (current_km, gear), b))


@pytest.mark.stop_drive
def test_stop_drive_returned_value(car):
    """
   Test to check if the method return the right value
   :param car: the car object
   :return: None
   """
    try:
        car.start_drive()
        assert car.stop_drive() is True
    except AssertionError as a:
        Utils.write_to_log(environ["TEST_PASS_NO_PARAMS"].format(inspect.stack()[0][3], a))


@pytest.mark.stop_drive
def test_stop_drive_raise_value_error(car):
    """
   Test to check if the method raise the right exception
   :param car: the car object
   :return: None
   """
    car.is_drive_on = False
    try:
        with pytest.raises(ValueError):
            car.stop_drive()
        Utils.write_to_log(environ["TEST_PASS_NO_PARAMS"].format(inspect.stack()[0][3]))

    except BaseException as b:
        Utils.write_to_log(environ["TEST_FAIL_NO_PARAMS"].format(inspect.stack()[0][3], b))


@pytest.mark.start_engine
def test_start_engine_value(car):
    """
   Test to check if the method return the right value
   :param car: the car object
   :return: None
   """
    try:
        assert car.start_engine() is True
        Utils.write_to_log(environ["TEST_PASS_NO_PARAMS"].format(inspect.stack()[0][3]))

    except AssertionError as a:
        Utils.write_to_log(environ["TEST_FAIL_NO_PARAMS"].format(inspect.stack()[0][3], a))


@pytest.mark.start_engine
def test_start_engine_raise_value_error(car):
    """
   Test to check if the method raises the right exception
   :param car: the car object
   :return: None
   """
    try:
        car.start_engine()
        with pytest.raises(ValueError):
            car.start_engine()
        Utils.write_to_log(environ["TEST_PASS_NO_PARAMS"].format(inspect.stack()[0][3]))

    except BaseException as b:
        Utils.write_to_log(environ["TEST_FAIL_NO_PARAMS"].format(inspect.stack()[0][3], b))


@pytest.mark.stop_engine
def test_stop_engine_value(car):
    """
   Test to check if the method return the right value
   :param car: the car object
   :return: None
   """
    try:
        car.start_engine()
        assert car.stop_engine() is True
        Utils.write_to_log(environ["TEST_PASS_NO_PARAMS"].format(inspect.stack()[0][3]))

    except AssertionError as a:
        Utils.write_to_log(environ["TEST_FAIL_NO_PARAMS"].format(inspect.stack()[0][3], a))


@pytest.mark.stop_engine
def test_stop_engine_raise_value_error(car):
    """
   Test to check if the method return the right value
   :param car: the car object
   :return: None
   """
    try:
        car.is_engine_on = False
        with pytest.raises(ValueError):
            car.stop_engine()
        Utils.write_to_log(environ["TEST_PASS_NO_PARAMS"].format(inspect.stack()[0][3]))
    except BaseException as b:
        Utils.write_to_log(environ["TEST_FAIL_NO_PARAMS"].format(inspect.stack()[0][3], b))


@pytest.mark.add_fuel
@pytest.mark.parametrize("fuel_to_add, fuel_result, road_km, money_result", [(1, 50, 20, 490), (1.5, 50, 49, 485)])
def test_add_fuel_returned_value(car, fuel_to_add, fuel_result, road_km, money_result):
    """
   Test to check if the method return the right value
   :param car: the car object
   :return: None
   """
    try:
        car.start_drive(road_km, 3)
        car.stop_drive()
        car.is_engine_on = False
        assert car.add_fuel(fuel_to_add) is True
        assert car.fuel == fuel_result
        assert car.money == money_result
        Utils.write_to_log(environ["TEST_PASS_WITH_PARAMS"].format(inspect.stack()[0][3],
                                                                   (fuel_to_add, fuel_result, road_km, money_result)))

    except AssertionError as a:
        Utils.write_to_log(environ["TEST_FAIL_NO_PARAMS"].format(inspect.stack()[0][3], a))


@pytest.mark.add_fuel
@pytest.mark.parametrize("fuel_to_add", [100, 1])
def test_add_fuel_raise_overflow_error(car, fuel_to_add):
    """
   Test to check if the method raises the right exception
   :param car: the car object
   :param fuel_to_add: the fuel amount to add
   :return: None
   """
    try:
        with pytest.raises(OverflowError):
            car.add_fuel(fuel_to_add)

        Utils.write_to_log(environ["TEST_PASS_WITH_PARAMS"].format(inspect.stack()[0][3], fuel_to_add))

    except BaseException as b:
        Utils.write_to_log(environ["TEST_FAIL_WITH_PARAMS"].format(inspect.stack()[0][3], fuel_to_add, b))


@pytest.mark.add_fuel
@pytest.mark.parametrize("fuel_to_add, distance", [(5, 50)])
def test_add_fuel_raise_permission_error(car, fuel_to_add, distance):
    """
   Test to check if the method raises the right exception
   :param car: the car object
   :param fuel_to_add: the fuel amount to add
   :return: None
   """
    car.start_drive(distance)
    try:
        with pytest.raises(PermissionError):
            car.add_fuel(fuel_to_add)

        Utils.write_to_log(environ["TEST_PASS_WITH_PARAMS"].format(inspect.stack()[0][3], fuel_to_add, distance))

    except BaseException as b:
        Utils.write_to_log(environ["TEST_FAIL_WITH_PARAMS"].format(inspect.stack()[0][3], (fuel_to_add, distance), b))


@pytest.mark.add_fuel
@pytest.mark.parametrize("fuel_to_add", ['', '5', True, []])
def test_add_fuel_raise_type_error(car, fuel_to_add):
    """
   Test to check if the method raises the right exception
   :param car: the car object
   :param fuel_to_add: the fuel amount to add
   :return: None
   """
    car.start_drive()
    car.stop_drive()
    car.stop_engine()
    try:
        with pytest.raises(TypeError):
            car.add_fuel(fuel_to_add)

        Utils.write_to_log(environ["TEST_PASS_WITH_PARAMS"].format(inspect.stack()[0][3], fuel_to_add))

    except BaseException as b:
        Utils.write_to_log(environ["TEST_FAIL_WITH_PARAMS"].format(inspect.stack()[0][3], fuel_to_add, b))


@pytest.mark.add_fuel
@pytest.mark.parametrize("fuel_to_add", [-1])
def test_add_fuel_raise_value_error(car, fuel_to_add):
    """
   Test to check if the method raises the right exception
   :param car: the car object
   :param fuel_to_add: the fuel amount to add
   :return: None
   """
    car.start_drive(50, 5)
    car.stop_drive()
    car.stop_engine()
    try:
        with pytest.raises(ValueError):
            car.add_fuel(fuel_to_add)

        Utils.write_to_log(environ["TEST_PASS_WITH_PARAMS"].format(inspect.stack()[0][3], fuel_to_add))

    except BaseException as b:
        Utils.write_to_log(environ["TEST_FAIL_WITH_PARAMS"].format(inspect.stack()[0][3], fuel_to_add, b))


@pytest.mark.consume
@pytest.mark.parametrize("km, result_fuel", [(50, 47.5), (100, 45.0), (0, 50)])
def test_consume_returned_value(car, km, result_fuel):
    """
   Test to check if the method return the right value
   :param car: the car object
   :param km: the km been of the past drive
   :return: None
   """
    try:
        assert car.consume(km) is True
        assert car.fuel == result_fuel
        Utils.write_to_log(environ["TEST_PASS_WITH_PARAMS"].format(inspect.stack()[0][3], (km, result_fuel)))

    except AssertionError as a:
        Utils.write_to_log(environ["TEST_FAIL_WITH_PARAMS"].format(inspect.stack()[0][3], (km, result_fuel), a))


@pytest.mark.consume
@pytest.mark.parametrize("km", [10001])
def test_consume_raise_overflow_error(car, km):
    """
   Test to check if the method raise the right exception
   :param car: the car object
   :param km: the km been of the past drive
   :return: None
   """
    try:
        with pytest.raises(OverflowError):
            car.consume(km)

        Utils.write_to_log(environ["TEST_PASS_WITH_PARAMS"].format(inspect.stack()[0][3], km))

    except BaseException as b:
        Utils.write_to_log(environ["TEST_FAIL_WITH_PARAMS"].format(inspect.stack()[0][3], km, b))


@pytest.mark.consume
@pytest.mark.parametrize("km", [-1])
def test_consume_raise_value_error(car, km):
    """
   Test to check if the method raise the right exception
   :param car: the car object
   :param km: the km been of the past drive
   :return: None
   """
    try:
        with pytest.raises(ValueError):
            car.consume(km)

        Utils.write_to_log(environ["TEST_PASS_WITH_PARAMS"].format(inspect.stack()[0][3], km))

    except BaseException as b:
        Utils.write_to_log(environ["TEST_FAIL_WITH_PARAMS"].format(inspect.stack()[0][3], km, b))


@pytest.mark.consume
@pytest.mark.parametrize("km", ['a'])
def test_consume_raise_type_error(car, km):
    """
   Test to check if the method raise the right exception
   :param car: the car object
   :param km: the km been of the past drive
   :return: None
   """
    try:
        with pytest.raises(TypeError):
            car.consume(km)

        Utils.write_to_log(environ["TEST_PASS_WITH_PARAMS"].format(inspect.stack()[0][3], km))

    except BaseException as b:
        Utils.write_to_log(environ["TEST_FAIL_WITH_PARAMS"].format(inspect.stack()[0][3], km, b))


@pytest.mark.get_current_car_status
def test_get_current_car_status_returned_value(car):
    """
   Test to check if the method return the right value
   :param car: the car object
   :return: None
   """
    try:
        assert isinstance(car.get_current_car_status(), str)
        Utils.write_to_log(environ["TEST_PASS_NO_PARAMS"].format(inspect.stack()[0][3]))

    except AssertionError as a:
        Utils.write_to_log(environ["TEST_FAIL_NO_PARAMS"].format(inspect.stack()[0][3], a))
