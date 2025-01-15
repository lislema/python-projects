import unittest
from main import randomNumGen


class TestDiceRolls(unittest.TestCase):
    def test_d6(self):
        # Test d6 range
        for _ in range(100):  # Run multiple times to check randomness
            result = randomNumGen(1)
            self.assertTrue(1 <= result <= 6)

    def test_d10(self):
        # Test d10 range
        result = randomNumGen(2)
        self.assertTrue(1 <= result <= 10)

    def test_d100(self):
        # Test d100 range
        result = randomNumGen(3)
        self.assertTrue(1 <= result <= 100)

    def test_d4(self):
        # Test d4 range
        result = randomNumGen(4)
        self.assertTrue(1 <= result <= 4)

    def test_d8(self):
        # Test d8 range
        result = randomNumGen(5)
        self.assertTrue(1 <= result <= 8)

    def test_d12(self):
        # Test d12 range
        result = randomNumGen(6)
        self.assertTrue(1 <= result <= 12)

    def test_d20(self):
        # Test d20 range
        result = randomNumGen(7)
        self.assertTrue(1 <= result <= 20)

    def test_invalid_choice(self):
        # Test invalid input
        result = randomNumGen(99)
        self.assertEqual(result, "Shouldn't be here. Invalid choice")


if __name__ == '__main__':
    unittest.main()