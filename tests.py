import unittest
from transport import Plane


class MyTest(unittest.TestCase):
	
	def test_object_creation(self):
		plane_name = 'testname'
		delay = 0.3
		boundary = 45
		mu = 0
		sigma = 1
		plane = Plane(plane_name, delay, boundary=boundary, mu=mu, sigma=mu)
		self.assertEqual(plane.name, plane_name)
		self.assertEqual(plane.delay, delay)

	def test_failed_object_creation_with_wrong_delay(self):
		plane_name = 'testname'
		delay = - 0.3
		boundary = 45
		mu = 0
		sigma = 1
		with self.assertRaises(Exception):
			plane = Plane(plane_name, delay, boundary=boundary, mu=mu, sigma=mu)

	def test_str(self):
		plane_name = 'testname'
		delay = 0.3
		boundary = 45
		mu = 0
		sigma = 1
		plane = Plane(plane_name, delay, boundary=boundary, mu=mu, sigma=mu)
		self.assertEqual(plane.__str__(), str(plane.orientation))