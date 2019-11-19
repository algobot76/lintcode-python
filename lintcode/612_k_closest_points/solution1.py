import heapq

from lintcode.utils import Point

"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""


class Solution:
    """
    @param points: a list of points
    @param origin: a point
    @param k: An integer
    @return: the k closest points
    """

    def kClosest(self, points, origin, k):
        heap = []
        for point in points:
            dist = self.get_distance(point, origin)
            heapq.heappush(heap, (-dist, -point.x, -point.y))
            if len(heap) > k:
                heapq.heappop(heap)

        ans = []
        while len(heap) > 0:
            _, x, y = heapq.heappop(heap)
            ans.append(Point(-x, -y))
        ans.reverse()

        return ans

    def get_distance(self, point, origin):
        return (point.x - origin.x) ** 2 + (point.y - origin.y) ** 2
