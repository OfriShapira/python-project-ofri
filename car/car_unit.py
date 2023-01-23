import inspect
import unittest
from os import environ

from dotenv import load_dotenv

from car.car_ex import Car
from car.utils import Utils


class CarTestCase(unittest.TestCase):
    def setUp(self):
        """
        Set up the test case
        """
        load_dotenv()
        self.c = Car()

    def test_start_drive_returns_true(self):
        """
        Test to check if the method returns the right value
        """
        try:
            self.assertEqual(self.c.start_drive(), True)
            Utils.write_to_log(environ["TEST_PASS_NO_PARAMS"].format(inspect.stack()[0][3]))

        except BaseException:
            Utils.write_to_log(environ["TEST_FAIL_NO_PARAMS"].format(inspect.stack()[0][3]))

    def test_start_drive_raise_value_error(self):
        """
        Test to check if the method throws the right exceptions
        """
        try:
            self.c.start_drive()
            with self.assertRaises(ValueError):
                self.c.start_drive()
            Utils.write_to_log(environ["TEST_PASS_NO_PARAMS"].format(inspect.stack()[0][3]))
        except BaseException as b:
            Utils.write_to_log(environ["TEST_FAIL_NO_PARAMS"].format(inspect.stack()[0][3], b))

    def test_start_drive_raise_type_error(self):
        """
        Test to check if the method throws the right exception
        """
        try:
            with self.assertRaises(TypeError):
                self.c.start_drive("a", 3)
        except BaseException as b:
            Utils.write_to_log(environ["TEST_FAIL_NO_PARAMS"].format(inspect.stack()[0][3], b))

    def test_start_drive_raise_over_flow(self):
        """
        Test to check if the method throws the right exception
        """
        try:
            with self.assertRaises(OverflowError):
                self.c.start_drive(3, 7)
            Utils.write_to_log(environ["TEST_PASS_NO_PARAMS"].format(inspect.stack()[0][3]))
        except BaseException as b:
            Utils.write_to_log(environ["TEST_FAIL_NO_PARAMS"].format(inspect.stack()[0][3], b))

    def test_stop_drive_returned_value(self):
        """
        Test to check if the method return the right value
        """
        try:
            self.c.start_drive()
            self.assertTrue(self.c.stop_drive())
            Utils.write_to_log(environ["TEST_PASS_NO_PARAMS"].format(inspect.stack()[0][3]))
        except BaseException as b:
            Utils.write_to_log(environ["TEST_FAIL_NO_PARAMS"].format(inspect.stack()[0][3], b))

    def test_stop_drive_raise_value_error(self):
        """
        Test to check if the method raise the right exception
        """
        try:
            self.c.is_drive_on = False
            with self.assertRaises(ValueError):
                self.c.stop_drive()
            Utils.write_to_log(environ["TEST_PASS_NO_PARAMS"].format(inspect.stack()[0][3]))

        except BaseException as b:
            Utils.write_to_log(environ["TEST_PASS_NO_PARAMS"].format(inspect.stack()[0][3]))

    def test_start_engine_value(self):
        """
        Test to check if the method return the right value
        """
        try:
            self.assertTrue(self.c.start_engine())
            Utils.write_to_log(environ["TEST_PASS_NO_PARAMS"].format(inspect.stack()[0][3]))

        except BaseException as b:
            Utils.write_to_log(environ["TEST_FAIL_NO_PARAMS"].format(inspect.stack()[0][3], b))

    def test_start_engine_raise_value_error(self):
        """
        Test to check if the method raises the right exception
        """
        try:
            self.c.start_engine()
            with self.assertRaises(ValueError):
                self.c.start_engine()
            Utils.write_to_log(environ["TEST_PASS_NO_PARAMS"].format(inspect.stack()[0][3]))

        except BaseException as b:
            Utils.write_to_log(environ["TEST_FAIL_NO_PARAMS"].format(inspect.stack()[0][3], b))

    def test_stop_engine_value(self):
        """
        Test to check if the method return the right value
        """
        try:

            self.c.start_engine()
            self.assertTrue(self.c.stop_engine())
            Utils.write_to_log(environ["TEST_PASS_NO_PARAMS"].format(inspect.stack()[0][3]))

        except AssertionError as b:
            Utils.write_to_log(environ["TEST_FAIL_NO_PARAMS"].format(inspect.stack()[0][3], b))

    def test_stop_engine_raise_value_error(self):
        """
        Test to check if the method return the right value
        """
        try:
            self.c.is_engine_on = False
            with self.assertRaises(ValueError):
                self.c.stop_engine()
            Utils.write_to_log(environ["TEST_PASS_NO_PARAMS"].format(inspect.stack()[0][3]))

        except BaseException as b:
            Utils.write_to_log(environ["TEST_FAIL_NO_PARAMS"].format(inspect.stack()[0][3], b))

    def test_add_fuel_returned_value(self):
        """
        Test to check if the method return the right value
        """
        try:
            self.c.start_drive(20, 3)
            self.c.stop_drive()
            self.c.is_engine_on = False
            self.c.add_fuel(1)
            self.assertEqual(self.c.fuel, 50)
            Utils.write_to_log(environ["TEST_PASS_NO_PARAMS"].format(inspect.stack()[0][3]))

        except BaseException as b:
            Utils.write_to_log(environ["TEST_FAIL_NO_PARAMS"].format(inspect.stack()[0][3], b))

    def test_add_fuel_raise_overflow_error(self):
        """
        Test to check if the method raises the right exception
        """
        try:
            with self.assertRaises(OverflowError):
                self.c.add_fuel(100)
            Utils.write_to_log(environ["TEST_PASS_NO_PARAMS"].format(inspect.stack()[0][3]))

        except AssertionError as b:
            Utils.write_to_log(environ["TEST_FAIL_NO_PARAMS"].format(inspect.stack()[0][3], b))

    def test_add_fuel_raise_permission_error(self):
        """
       Test to check if the method raises the right exception
       """
        try:
            with self.assertRaises(PermissionError):
                self.c.start_drive(50, 5)
                self.c.add_fuel(5)
            Utils.write_to_log(environ["TEST_PASS_NO_PARAMS"].format(inspect.stack()[0][3]))

        except AssertionError as b:
            Utils.write_to_log(environ["TEST_FAIL_NO_PARAMS"].format(inspect.stack()[0][3], b))

    def test_add_fuel_raise_type_error(self):
        """
       Test to check if the method raises the right exception
       """
        try:
            self.c.start_drive()
            self.c.stop_drive()
            self.c.stop_engine()

            with self.assertRaises(TypeError):
                self.c.add_fuel('a')
            Utils.write_to_log(environ["TEST_PASS_NO_PARAMS"].format(inspect.stack()[0][3]))

        except AssertionError as a:
            Utils.write_to_log(environ["TEST_FAIL_NO_PARAMS"].format(inspect.stack()[0][3], a))

    def test_add_fuel_raise_value_error(self):
        """
       Test to check if the method raises the right exception
       """
        try:
            self.c.start_drive(50, 5)
            self.c.stop_drive()
            self.c.stop_engine()
            with self.assertRaises(ValueError):
                self.c.add_fuel(-1)
            Utils.write_to_log(environ["TEST_PASS_NO_PARAMS"].format(inspect.stack()[0][3]))

        except AssertionError as b:
            Utils.write_to_log(environ["TEST_FAIL_NO_PARAMS"].format(inspect.stack()[0][3], b))

    def test_consume_returned_value(self):
        """
        Test to check if the method return the right value
        """
        try:
            self.assertTrue(self.c.consume(50))
            self.assertTrue(self.c.fuel == 47.5)
            Utils.write_to_log(environ["TEST_PASS_NO_PARAMS"].format(inspect.stack()[0][3]))

        except BaseException as b:
            Utils.write_to_log(environ["TEST_FAIL_NO_PARAMS"].format(inspect.stack()[0][3], b))

    def test_consume_raise_overflow_error(self):
        """
       Test to check if the method raises the right exception
       """
        try:
            with self.assertRaises(OverflowError):
                self.c.consume(10001)
                Utils.write_to_log(environ["TEST_PASS_NO_PARAMS"].format(inspect.stack()[0][3]))

        except BaseException as b:
            Utils.write_to_log(environ["TEST_FAIL_NO_PARAMS"].format(inspect.stack()[0][3], b))

    def test_consume_raise_value_error(self):
        """
       Test to check if the method raises the right exception
       """
        try:
            with self.assertRaises(ValueError):
                self.c.consume(-1)
            Utils.write_to_log(environ["TEST_PASS_NO_PARAMS"].format(inspect.stack()[0][3]))

        except BaseException as b:
            Utils.write_to_log(environ["TEST_FAIL_NO_PARAMS"].format(inspect.stack()[0][3], b))

    def test_consume_raise_type_error(self):
        """
        Test to check if the method raises the right exception
        """
        try:
            with self.assertRaises(TypeError):
                self.c.consume('km')
            Utils.write_to_log(environ["TEST_PASS_NO_PARAMS"].format(inspect.stack()[0][3]))

        except BaseException as b:
            Utils.write_to_log(environ["TEST_FAIL_NO_PARAMS"].format(inspect.stack()[0][3], b))

    def test_get_current_car_status_returned_value(self):
        """
        Test to check if the method returns the right value
        """
        try:
            self.assertIsInstance(self.c.get_current_car_status(), str)
            Utils.write_to_log(environ["TEST_PASS_NO_PARAMS"].format(inspect.stack()[0][3]))

        except BaseException as b:
            Utils.write_to_log(environ["TEST_FAIL_NO_PARAMS"].format(inspect.stack()[0][3], b))


if __name__ == '__main__':
    unittest.main()
