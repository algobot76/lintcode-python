"""
Definition of ArrayReader
class ArrayReader(object):
    def get(self, index):
    	# return the number on given index,
        # return 2147483647 if the index is invalid.
"""


class Solution:
    """
    @param: reader: An instance of ArrayReader.
    @param: target: An integer
    @return: An integer which is the first index of target.
    """

    def searchBigSortedArray(self, reader, target):
        start = 0
        end = 1
        while reader.get(end) < target:
            end <<= 1

        while start + 1 < end:
            mid = (start + end) // 2
            if reader.get(mid) >= target:
                end = mid
            else:
                start = mid

        if reader.get(start) == target:
            return start
        else:
            return -1
