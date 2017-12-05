import unittest
from transport import Plane


class MyTest(unittest.TestCase):

    def test_object_creation(self):
        plane_name = 'testname'
        delay = 0.3
        boundary = 45
        mu = 0
        sigma = 1
        plane = Plane(plane_name, delay=delay, boundary=boundary, mu=mu, sigma=mu)
        self.assertEqual(plane.name, plane_name)
        self.assertAlmostEqual(plane.delay, delay)

    def test_failed_object_creation_with_negative_delay(self):
        plane_name = 'testname'
        delay = - 0.3
        boundary = 45
        mu = 0
        sigma = 1
        with self.assertRaises(Exception):
            plane = Plane(plane_name, delay=delay, boundary=boundary, mu=mu, sigma=mu)

    def test_failed_object_creation_with_wrong_boundary_type(self):
        plane_name = 'testname'
        delay = 0.3
        boundary = 'test'
        mu = 0
        sigma = 1
        with self.assertRaises(TypeError):
            plane = Plane(plane_name, delay=delay, boundary=boundary, mu=mu, sigma=mu)

    def test_failed_object_creation_with_none_boundary(self):
        plane_name = 'testname'
        delay = 0.3
        boundary = None
        mu = 0
        sigma = 1
        with self.assertRaises(TypeError):
            plane = Plane(plane_name, delay=delay, boundary=boundary, mu=mu, sigma=mu)


    def test_str(self):
        plane_name = 'testname'
        delay = 0.3
        boundary = 45
        mu = 0
        sigma = 1
        plane = Plane(plane_name, delay=delay, boundary=boundary, mu=mu, sigma=mu)
        self.assertEqual(plane.__str__(), str(plane.orientation))

    def test_fly_with_small_positive_boundary(self):
        plane_name = 'testname'
        delay = 0.01
        boundary = 13
        mu = 0.1
        sigma = 1
        plane = Plane(plane_name, delay=delay, boundary=boundary, mu=mu, sigma=mu)
        plane.fly()
        self.assertTrue(abs(plane.orientation) < 1.)

    def test_fly_with_big_positive_boundary(self):
        plane_name = 'testname'
        delay = 0.01
        boundary = 200
        mu = 0.1
        sigma = 1
        plane = Plane(plane_name, delay=delay, boundary=boundary, mu=mu, sigma=mu)
        plane.fly()
        self.assertTrue(abs(plane.orientation) < 1.)

    def test_fly_with_close_to_zero_boundary(self):
        plane_name = 'testname'
        delay = 0.01
        boundary = 0.01
        mu = 0.1
        sigma = 1
        plane = Plane(plane_name, delay=delay, boundary=boundary, mu=mu, sigma=mu)
        plane.fly()
        self.assertTrue(abs(plane.orientation) < 1.)

    def test_fly_with_negative_boundary(self):
        plane_name = 'testname'
        delay = 0.01
        boundary = -12
        mu = 0.1
        sigma = 1
        plane = Plane(plane_name, delay=delay, boundary=boundary, mu=mu, sigma=mu)
        plane.fly()
        self.assertTrue(abs(plane.orientation) < 1.)

    def test_fly_fail_with_wrong_gauss_values(self):
        plane_name = 'testname'
        delay = 0.01
        boundary = -12
        mu = - 0.1
        sigma = 1
        plane = Plane(plane_name, delay=delay, boundary=boundary, mu=mu, sigma=mu)
        with self.assertRaises(ValueError):
            plane.fly()
