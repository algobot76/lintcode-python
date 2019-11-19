import sys


class Solution:
    """
    @param nums: an integer array
    @param target: An integer
    @return: the difference between the sum and the target
    """

    def twoSumClosest(self, nums, target):
        nums.sort()
        left = 0
        right = len(nums) - 1

        diff = sys.maxsize
        while left < right:
            sum_ = nums[left] + nums[right]
            if sum_ > target:
                right -= 1
            else:
                left += 1
            diff = min(diff, abs(sum_ - target))

        return diff
