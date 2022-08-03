import unittest
import fizzbuzz

class FizzBuzzTest(unittest.TestCase):

    def test_fizz(self):
        number = 6

        result = fizzbuzz.get_replay(number)

        self.assertEqual(result, 'Fizz')

    def test_buzz(self):
        number = 10

        result = fizzbuzz.get_replay(number)

        self.assertEqual(result, 'Buzz')

    def test_fizzbuzz(self):
        number = 15

        result = fizzbuzz.get_replay(number)

        self.assertEqual(result, 'FizzBuzz')

if __name__ == '__maine__':
    unittest.main()