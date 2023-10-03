import unittest
from islands_counter.island import count_islands

class IslandCounterTest(unittest.TestCase):
    def test_init(self):
        self.assertEqual(count_islands([[]], 0, 0), 0)

    def test_no_island(self):
        self.assertEqual(count_islands([
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]], 4, 4), 0)
        
    def test_case_0(self):
        self.assertEqual(count_islands([
            [1, 1, 1, 0, 0, 0],
            [1, 1, 1, 0, 0, 0],
            [1, 1, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 1, 1]], 6, 6), 3)
        
    def test_case_1(self):
        self.assertEqual(count_islands([
            [1, 0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0, 1]], 6, 6), 18)

if __name__ is "__main__":
    unittest.main()