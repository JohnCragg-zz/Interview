import random
from decimal import *


class RandomGen(object):
    # Values that may be returned by next_num()
    def __init__(self, nums, prob):
        self._random_nums = nums
        self._probabilities = prob
        self.size = len(nums)
        self.ranges = self.create_ranges()

    def create_ranges(self, acc=Decimal('0'), i=0, ranges={}):
        if i == self.size - 1:
            ranges[(acc, Decimal('1'))] = self._random_nums[i]
            return ranges
        else:
            prob = Decimal(str(self._probabilities[i]))
            ranges[(acc, acc + prob)] = self._random_nums[i]
            i += 1
            acc += prob
            return self.create_ranges(acc, i, ranges)

    def next_num(self):
        """
        Returns one of the randomNums. When this method is called
        multiple times over a long period, it should return the
        numbers roughly with the initialized probabilities.
        """
        size = len(self._random_nums)
        if size != len(self._probabilities):
            raise ValueError("Lengths of numbers and probabilities don't match")
        else:
            next_num = random.random()
            for i in self.ranges.keys():
                as_decimal = Decimal(str(next_num))
                if as_decimal.compare(i[0]) == Decimal('1') and as_decimal.compare(i[1]) == Decimal('-1'):
                    return self.ranges[i]
