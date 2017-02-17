#!/usr/bin/python

import unittest

class TestStatisticalFunctions(unittest.TestCase):

    def test_average(self):
        self.assertEqual(average([40,60,140]),80.0)
        self.assertEqual(round(average([2,3,8]),4.3))
        with self.assertRaises(ZeroDivisionError):
            average([])
        with self.assertRaises(TypeError):
            average(40,60,140)

#invokes all tests            
unittest.main()
