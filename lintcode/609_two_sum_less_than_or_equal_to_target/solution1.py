class Solution:
    """
    @param nums: an array of integer
    @param target: an integer
    @return: an integer
    """

    def twoSum5(self, nums, target):
        if not nums or len(nums) < 2:
            return 0

        nums.sort()
        left = 0
        right = len(nums) - 1
        count = 0

        while left < right:
            sum_ = nums[left] + nums[right]
            if sum_ <= target:
                count += right - left
                left += 1
            else:
                right -= 1

        return count
