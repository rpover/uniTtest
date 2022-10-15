from main import find_max
import unittest

class TestFunction(unittest.TestCase):
	def test_find_max(self):
		self.assertEqual(find_max(5278), 8)


if __name__ == '__main__':
	unittest.main()