from unittest import TestCase

from AHL import RandomGen
from decimal import Decimal


def _create_count_from_rg(nums):
    acc = {}
    for i in nums:
        acc[i] = 0
    return acc


def _test_case(rg, count_by_number, trials, nums_and_probabilities):
    for i in range(0, trials):
        a = rg.next_num()
        count_by_number[a] = count_by_number[a] + 1
    for num, prob in nums_and_probabilities:
        expected = trials * prob
        if not (expected - 4 <= count_by_number[num] <= expected + 4):
            return 0
    return 1


class TestRandomGen(TestCase):
    def test_create_ranges_with_multiple_numbers(self):
        rg = RandomGen([-1, 0, 1, 2, 3], [0.01, 0.3, 0.58, 0.1, 0.01])
        actual = rg.ranges
        expected = {
            (Decimal('0'), Decimal('0.01')): -1,
            (Decimal('0.01'), Decimal('0.31')): 0,
            (Decimal('0.31'), Decimal('0.89')): 1,
            (Decimal('0.89'), Decimal('0.99')): 2,
            (Decimal('0.99'), Decimal('1')): 3
        }
        self.assertEqual(actual, expected)

    def test_create_ranges_with_single_number(self):
        rg = RandomGen([1], [1])
        actual = rg.ranges
        expected = {
            (Decimal('0'), Decimal('1')): 1
        }
        self.assertEqual(actual, expected)

    def test_next_num(self, nums=[-1, 0, 1, 2, 3], probabilities=[0.01, 0.3, 0.58, 0.1, 0.01]):
        rg = RandomGen(nums, probabilities)
        zipped = zip(nums, probabilities)
        res = 0
        for i in range(0, 10):
            count_by_number = _create_count_from_rg(nums)
            res += _test_case(rg, count_by_number, 100, zipped)
        print(res)
        assert (res >= 8)
