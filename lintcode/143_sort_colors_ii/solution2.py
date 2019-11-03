class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """

    def sortColors2(self, colors, k):
        self.quick_sort(colors, 0, len(colors) - 1)

    def quick_sort(self, arr, start, end):
        if start >= end:
            return

        left, right = start, end
        pivot = arr[(start + end) // 2]

        while left <= right:
            while left <= right and arr[left] < pivot:
                left += 1
            while left <= right and arr[right] > pivot:
                right -= 1
            if left <= right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
        self.quick_sort(arr, start, right)
        self.quick_sort(arr, left, end)
