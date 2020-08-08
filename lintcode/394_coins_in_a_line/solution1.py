class Solution:
    """
    @param n: An integer
    @return: A boolean which equals to true if the first player will win
    """

    def firstWillWin(self, n):
        f = [False, True, True]
        for i in range(3, n + 1):
            f[i % 3] = not f[(i - 1) % 3] or not f[(i - 2) % 3]
        return f[n % 3]
