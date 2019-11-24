class Solution:
    """
    @param arr: An integer array
    @param k: An integer
    @return: return the pair of movies index with the longest total duration
    """

    def FlightDetails(self, arr, k):
        k -= 30
        movies = []
        for i in range(len(arr)):
            movies.append((arr[i], i))

        movies.sort(key=lambda x: x[0])
        left = 0
        right = len(arr) - 1
        longest_movie = 0
        longest_duration = 0
        ans = [-1, -1]
        while left < right:
            m1 = movies[left]
            m2 = movies[right]
            duration = m1[0] + m2[0]
            if duration >= k:
                right -= 1
            else:
                if (m1[0] >= longest_movie or
                    m2[0] >= longest_movie) and duration >= longest_duration:
                    longest_movie = max(m1[0], m2[0])
                    longest_duration = duration
                    ans = [m1[1], m2[1]]
                left += 1

        return sorted(ans)
