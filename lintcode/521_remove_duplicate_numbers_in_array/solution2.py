class Solution:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """

    def deduplication(self, nums):
        if not nums:
            return 0

        nums.sort()
        result = 1
        for i in range(1, len(nums)):
            if nums[i - 1] != nums[i]:
                nums[result] = nums[i]
                result += 1

        return result
