from algorithm import *
import unittest


class FuncsTest(unittest.TestCase):

        def test_max_ident_elem(self):
                self.assertEqual(max_ident_elem([3, 6, 5, 4, 2]), 1)
                self.assertEqual(max_ident_elem([5, 3, 3]), 2)
                self.assertEqual(max_ident_elem([0, -2, -4, -4, 2]), 2)
                self.assertEqual(max_ident_elem([0, 2, 0, 0, 0, 0, 6, 5]), 5)
                self.assertNotEqual(max_ident_elem([-4, 2, -4]), 1)


if __name__ == '__main__':
    unittest.main()


