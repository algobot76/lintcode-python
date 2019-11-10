class Solution:
    """
    @param: : a string to be split
    @return: all possible split string array
    """

    def splitString(self, s):
        ans = []
        self.dfs(s, [], ans)
        return ans

    def dfs(self, s, path, ans):
        if s == "":
            ans.append(path[:])
            return

        for i in range(2):
            if i + 1 <= len(s):
                path.append(s[:i + 1])
                self.dfs(s[i + 1:], path, ans)
                path.pop()
