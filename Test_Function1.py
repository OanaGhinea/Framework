import unittest
from Function1 import isprime, prime_list

# Scrieti teste unitare pentru functia is_prime
# Scrieti test unitar pentru functia list_of_primes_in_interval

class FunctionTestCase(unittest.TestCase):
    def isprime_01(self):
        expected_result = True
        actual_result = is_prime(13)
        self.assertIsInstance(actual_result, bool )
        self.assertEqual(expected_result, actual_result)

    def  isprime_02(self):
        expected_result = False
        actual_result = is_prime(24)
        self.assertIsInstance(actual_result, bool)
        self.assertEqual(expected_result, actual_result)

    def test_prime_list(self):
        expected_result = [3,5,7,11,13,17,19,23,29,31]
        actual_result = prime_list(3, 32)
        self.assertIsInstance(actual_result, list )
        self.assertEqual(expected_result, actual_result)

if __name__ == "__main__":
    if __name__ == "__main__":
        unittest.main()
