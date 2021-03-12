import unittest

from main import is_prime_v1 as is_prime


class PrimeTest(unittest.TestCase):
    def test_is_prime_ok(self):
        for i in [1,3,4,34,4,]:
            self.assertTrue(is_prime(i))

    def test_is_prime_no(self):
        for i in [1, 4, 6, 9, 10, 11]:
            self.assertFalse(is_prime(i))
    def test_is_prime_negative(self):
        self.assertFalse(is_prime(-1))


    def test_is_prime_raise_typeerror(self):
        with self.assertRaises(TypeError):
            is_prime('strings')

if __name__ == '__main__':
    unittest.main()

