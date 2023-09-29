import unittest
from courses_checker.course import check_if_courses_possible, extract_course_chain

class CourseCheckerTest(unittest.TestCase):
    def test_init(self):
        self.assertTrue(check_if_courses_possible(2, []))

    def test_simple(self):
        self.assertTrue(check_if_courses_possible(2, [(0,1)]))
        
    def test_impossible(self):
        self.assertFalse(check_if_courses_possible(2, [(0,1), (1,0)]))

    
    def test_case_1(self):
        self.assertTrue(
            check_if_courses_possible(
            5, 
            [
                (0, 1), (0, 2), (1, 3), (1, 4), (3, 4)
            ]   
            )
        )

class CourseChainerTest(unittest.TestCase):
    def test_init(self):
        self.assertEquals(extract_course_chain(2, []), [0, 1])

    def test_simple(self):
        self.assertEquals(extract_course_chain(2, [(0,1)]), [1, 0])
        
    def test_impossible(self):
        self.assertIsNone(extract_course_chain(2, [(0,1), (1,0)]))
    
    def test_case_1(self):
        self.assertEquals(
            extract_course_chain(
            5, 
            [
                (0, 1), (0, 2), (1, 3), (1, 4), (3, 4)
            ]   
            ), 
            [4, 3, 1, 2, 0]
        )

    def test_case_2(self):
        self.assertEquals(
            extract_course_chain(
            7, 
            [
                (0, 1), (0, 2), (1, 3), (1, 4), (3, 4), (5, 2), (5, 6)
            ]   
            ), 
            [4, 3, 1, 2, 0, 6, 5]
        )

    def test_init(self):
        self.assertEquals(extract_course_chain(2, []), [0, 1])

    def test_simple(self):
        self.assertEquals(extract_course_chain(2, [(0,1)]), [1, 0])
        
    def test_impossible(self):
        self.assertIsNone(extract_course_chain(2, [(0,1), (1,0)]))
    
    def test_case_1(self):
        self.assertEquals(
            extract_course_chain(
            5, 
            [
                (0, 1), (0, 2), (1, 3), (1, 4), (3, 4)
            ]   
            ), 
            [4, 3, 1, 2, 0]
        )

    def test_case_2(self):
        self.assertEquals(
            extract_course_chain(
            7, 
            [
                (0, 1), (0, 2), (1, 3), (1, 4), (3, 4), (5, 2), (5, 6)
            ]   
            ), 
            [4, 3, 1, 2, 0, 6, 5]
        )