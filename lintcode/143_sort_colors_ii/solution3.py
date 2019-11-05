class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """

    def sortColors2(self, colors, k):
        self.quick_sort(colors, 1, k, 0, len(colors) - 1)

    def quick_sort(self, arr, first_color, last_color, start, end):
        if start >= end or first_color == last_color:
            return

        left, right = start, end
        pivot_color = (first_color + last_color) // 2

        while left <= right:
            while left <= right and arr[left] <= pivot_color:
                left += 1
            while left <= right and arr[right] > pivot_color:
                right -= 1
            if left <= right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1

        self.quick_sort(arr, first_color, pivot_color, start, right)
        self.quick_sort(arr, pivot_color + 1, last_color, left, end)
