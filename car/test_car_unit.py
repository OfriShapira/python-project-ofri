import unittest

from car.car_ex import Car


class CarTestCase(unittest.TestCase):
    def setUp(self):
        """
        Set up the test case
        :return: None
        """
        self.c = Car()

    def test_start_drive_returns_true(self):
        """
        Test to check if the method returns the right value
        """
        self.assertEqual(self.c.start_drive(), True)

    def test_start_drive_raise_value_error(self):
        """
        Test to check if the method throws the right exceptions
        """
        self.c.start_drive()
        with self.assertRaises(ValueError):
            self.c.start_drive()

    def test_start_drive_raise_type_error(self):
        """
        Test to check if the method throws the right exception
        """
        with self.assertRaises(TypeError):
            self.c.start_drive("a", 3)

    def test_start_drive_raise_over_flow(self):
        """
        Test to check if the method throws the right exception
        """
        with self.assertRaises(OverflowError):
            self.c.start_drive(3, 7)

    def test_stop_drive_returned_value(self):
        """
        Test to check if the method return the right value
        """
        self.c.start_drive()
        self.assertTrue(self.c.stop_drive())

    def test_stop_drive_raise_value_error(self):
        """
        Test to check if the method raise the right exception
        """
        self.c.is_drive_on = False
        with self.assertRaises(ValueError):
            self.c.stop_drive()

    def test_start_engine_value(self):
        """
        Test to check if the method return the right value
        """
        self.assertTrue(self.c.start_engine())

    def test_start_engine_raise_value_error(self):
        """
        Test to check if the method raises the right exception
        """
        self.c.start_engine()
        with self.assertRaises(ValueError):
            self.c.start_engine()

    def test_stop_engine_value(self):
        """
        Test to check if the method return the right value
        """
        self.c.start_engine()
        self.assertTrue(self.c.stop_engine())

    def test_stop_engine_raise_value_error(self):
        """
        Test to check if the method return the right value
        """
        self.c.is_engine_on = False
        with self.assertRaises(ValueError):
            self.c.stop_engine()

    def test_add_fuel_returned_value(self):
        """
        Test to check if the method return the right value
        """
        self.c.start_drive(20, 3)
        self.c.stop_drive()
        self.c.is_engine_on = False
        self.c.add_fuel(1)
        self.assertEqual(self.c.fuel, 50)

    def test_add_fuel_raise_overflow_error(self):
        """
        Test to check if the method raises the right exception
        """
        with self.assertRaises(OverflowError):
            self.c.add_fuel(100)

    def test_add_fuel_raise_permission_error(self):
        """
       Test to check if the method raises the right exception
       """
        with self.assertRaises(PermissionError):
            self.c.start_drive(50, 5)
            self.c.add_fuel(5)

    def test_add_fuel_raise_type_error(self):
        """
       Test to check if the method raises the right exception
       """
        self.c.start_drive()
        self.c.stop_drive()
        self.c.stop_engine()

        with self.assertRaises(TypeError):
            self.c.add_fuel('a')

    def test_add_fuel_raise_value_error(self):
        """
       Test to check if the method raises the right exception
       """
        self.c.start_drive(50, 5)
        self.c.stop_drive()
        self.c.stop_engine()
        with self.assertRaises(ValueError):
            self.c.add_fuel(-1)

    def test_consume_returned_value(self):
        """
        Test to check if the method return the right value
        """
        self.assertTrue(self.c.consume(50))
        self.assertTrue(self.c.fuel == 47.5)

    def test_consume_raise_overflow_error(self):
        """
       Test to check if the method raises the right exception
       """
        with self.assertRaises(OverflowError):
            self.c.consume(10001)

    def test_consume_raise_value_error(self):
        """
       Test to check if the method raises the right exception
       """
        with self.assertRaises(ValueError):
            self.c.consume(-1)

    def test_consume_raise_type_error(self):
        """
        Test to check if the method raises the right exception
        """
        with self.assertRaises(TypeError):
            self.c.consume('km')

    def test_get_current_car_status_returned_value(self):
        """
        Test to check if the method returns the right value
        """
        self.assertIsInstance(self.c.get_current_car_status(), str)


if __name__ == '__main__':
    unittest.main()
