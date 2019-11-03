class Solution:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """

    def deduplication(self, nums):
        if not nums:
            return 0

        visited = {}
        result = 0
        for num in nums:
            if num not in visited:
                visited[num] = True
                nums[result] = num
                result += 1

        return result
