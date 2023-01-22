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
    Test to check if the method returns the right value
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
    except AssertionError as a:
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
        with pytest.raises(TypeError) as info:
            Utils.write_to_log(environ["TEST_PASS_WITH_PARAMS"].format(inspect.stack()[0][3], (current_km, gear)))
            car.start_drive(current_km, gear)
    except BaseException as b:
        Utils.write_to_log(environ["TEST_FAIL_WITH_PARAMS"].format(inspect.stack()[0][3], (current_km, gear), b))


@pytest.mark.start_drive
@pytest.mark.parametrize("current_km, gear", [(3, 3)])
def test_start_drive_raise_over_flow(car, current_km, gear):
    """
    Test to check if the method throws the right exceptions
    :param car: the car object
    :return: None
    """
    try:
        with pytest.raises(OverflowError):
            Utils.write_to_log(environ["TEST_PASS_WITH_PARAMS"].format(inspect.stack()[0][3], (current_km, gear)))
            car.start_drive(current_km, gear)
    except BaseException as b:
        Utils.write_to_log(environ["TEST_FAIL_WITH_PARAMS"].format(inspect.stack()[0][3], (current_km, gear), b))


@pytest.mark.stop_drive
def test_stop_drive_value(car):
    """
   Test to check if the method return the right value
   :param car: the car object
   :return: None
   """
    car.start_drive()
    assert car.stop_drive() is True


@pytest.mark.stop_drive
def test_stop_drive_raise_value_error(car):
    """
   Test to check if the method return the right value
   :param car: the car object
   :return: None
   """
    car.start_drive()
    try:
        with pytest.raises(ValueError):
            Utils.write_to_log(environ["TEST_PASS_WITH_PARAMS"].format(inspect.stack()[0][3]))
            car.stop_drive()
    except BaseException as b:
        Utils.write_to_log(environ["TEST_FAIL_NO_PARAMS"].format(inspect.stack()[0][3], b))


@pytest.mark.start_engine
def test_start_engine_value(car):
    """
   Test to check if the method return the right value
   :param car: the car object
   :return: None
   """
    assert car.start_engine() is True


@pytest.mark.start_engine
def test_stop_engine_value(car):
    """
   Test to check if the method return the right value
   :param car: the car object
   :return: None
   """
    car.start_engine()
    assert car.stop_engine() is True

def test_add_fuel(car):
    car.start_drive(40, 1)
    assert car.add_fuel(2) is True
    assert car.money == 480
    assert car.fuel == 50


def test_consume(car):
    assert car.consume(50) is True
