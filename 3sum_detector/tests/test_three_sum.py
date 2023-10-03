import unittest
from three_sum.three_sum import detect_three_sum

class ThreeSumTest(unittest.TestCase):
    def test_init(self):
        self.assertEquals(detect_three_sum([]), [])

    def test_usecase_0(self):
        self.assertEquals(detect_three_sum([-1, 1, 0]), [(-1,0,1)])

    def test_usecase_1(self):
        self.assertEquals(detect_three_sum(
            [-3, 3, 4, -3, 1, 2]
            ), [
                (-3, 1, 2)
            ]
        )
    
    def test_usecase_2(self):
        test_solution = [
            (-1, -1, 2),
            (-1, 0, 1),
            (-2, 0, 2),
            (-2, -1, 3)
        ]
        solution = detect_three_sum([-1, -1, 2, 0, -2, 1, 3])
        self.assertEqual(len(solution), len(test_solution))
        for sub_solution in solution:
            self.assertTrue(sub_solution in test_solution)
    
    def test_usecase_3(self):
        test_solution = [
            (0, 0, 0)
        ]
        solution = detect_three_sum([0, 0, 0, 0, 0, 0])
        self.assertEqual(len(solution), len(test_solution))
        for sub_solution in solution:
            self.assertTrue(sub_solution in test_solution)