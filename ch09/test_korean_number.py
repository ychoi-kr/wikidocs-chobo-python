from korean_0_to_100 import korean_number
import unittest


class TestKoreanNumber(unittest.TestCase):
    def test_0(self):
        self.assertEqual(korean_number(0), '영')
        
    def test_1(self):
        self.assertEqual(korean_number(1), '일')

    def test_2(self):
        self.assertEqual(korean_number(2), '이')

    def test_10(self):
        self.assertEqual(korean_number(10), '십')

    def test_11(self):
        self.assertEqual(korean_number(11), '십일')

    def test_12(self):
        self.assertEqual(korean_number(12), '십이')

    def test_20(self):
        self.assertEqual(korean_number(20), '이십')

    def test_21(self):
        self.assertEqual(korean_number(21), '이십일')

    def test_31(self):
        self.assertEqual(korean_number(31), '삼십일')

    def test_41(self):
        self.assertEqual(korean_number(41), '사십일')

    def test_100(self):
        self.assertEqual(korean_number(100), '백')


if __name__ == '__main__':
    unittest.main()

