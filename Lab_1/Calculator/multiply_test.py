import calculator as c
import unittest

class TestMultiply(unittest.TestCase):

	def test_both_pos(self):
		res=c.multiply(2,3)
		self.assertEqual(res,6)

	def test_pos_neg(self):
		res=c.multiply(2,-3)
		self.assertEqual(res,-6)

	def test_pos_neg(self):
		res=c.multiply(-2,3)
		self.assertEqual(res,-6)

	def test_both_neg(self):
		res=c.multiply(-2,3)
		self.assertEqual(res,-6)

if __name__ == '__main__':
    unittest.main()