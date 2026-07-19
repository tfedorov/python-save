#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target

import unittest
from typing import Any

def calculate(nums:list[int], target):
    already_find = {}
    for el_idx in range(len(nums)):
        el = nums[el_idx]
        need_to_find = target - el
        if need_to_find in already_find:
            return (already_find[need_to_find],el_idx)
        el_to_match = el
        already_find[el_to_match] = el_idx
    return (-1,-1)

##def calculate(nums:list[int], target):
    ##    for el1_ind in range(len(nums)):
    ##        el1 = nums[el1_ind]
    ##        el1_match = target - el1
    ##        for el2_ind in range(len(nums)):
    ##           el2 = nums[el2_ind]
    ##           if el1_match == el2:
    ##               return (el1_ind,el2_ind)
##   return (0,0)

class TaksTestCase(unittest.TestCase):
    def test_default(self):
        nums: list[int] = [2,7,11,15]
        target = 9
        result = calculate(nums,target)

        expected = (0,1)
        self.assertEqual(expected, result)

    def test_none(self):
        nums: list[int] = []
        target = 9
        result = calculate(nums,target)

        expected = (-1,-1)
        self.assertEqual(expected, result)

    def test_last(self):
        nums: list[int] = [2,7,11,15]
        target = 26
        result = calculate(nums,target)

        expected = (2,3)
        self.assertEqual(expected, result)

if __name__ == "__main__":
    unittest.main()