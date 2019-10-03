"""
Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""
from collections import deque


class Solution:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """

    def topSort(self, graph):
        indegrees = self.get_indegrees(graph)
        order = []
        start_nodes = [node for node in graph if indegrees[node] == 0]
        queue = deque(start_nodes)
        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbor in node.neighbors:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    queue.append(neighbor)
        return order

    def get_indegrees(self, graph):
        indegrees = {
            x: 0 for x in graph
        }

        for node in graph:
            for neighbor in node.neighbors:
                indegrees[neighbor] += 1
        return indegrees
