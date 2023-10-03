import unittest 
from longest_consecutive_sequence.consecutive_sequence_counter import count_sequences

class ConsecutiveSequenceCounterTest(unittest.TestCase):

    def test_init(self):
        self.assertEqual(count_sequences([]), 0)
    
    def test_case_0(self):
        self.assertEqual(count_sequences([1,2,3]), 3)

    def test_case_1(self):
        self.assertEqual(count_sequences([100, 4, 200, 1, 3, 2]), 4)

if __name__ is "__main__":
    unittest.main()