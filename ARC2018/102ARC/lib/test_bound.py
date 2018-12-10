""" test_bound.py for tesging bound.py """
from bound import lower_bound, upper_bound
import unittest

class BoundTest(unittest.TestCase):
    def setUp(self):
        self.normal_array = [1,2,3,4,5,6,7]

    def test_lower(self):
        l = lower_bound(5,self.normal_array)
        self.assertEqual(l,4)

    def test_none_lower(self):
        l = lower_bound(8,self.normal_array)
        self.assertEqual(l,len(self.normal_array))
    
    def test_upper(self):
        u = upper_bound(5,self.normal_array)
        self.assertEqual(u,3)

    def test_none_upper(self):
        u = upper_bound(-1,self.normal_array)
        self.assertEqual(u,-1)

    def test_func_lower(self):
        l = lower_bound(34, [1,2,3,4,5,6], func=lambda k,array,ind: k<=2**array[ind])
        self.assertEqual(l,5)

    def test_func_upper(self):
        u = upper_bound(29, [1,2,3,4,5], func=lambda k,array,ind: 3**array[ind]<k)
        self.assertEqual(u, 2)

