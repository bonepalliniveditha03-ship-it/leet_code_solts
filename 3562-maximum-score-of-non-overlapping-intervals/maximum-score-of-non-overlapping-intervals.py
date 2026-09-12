class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        import bisect

        n = len(intervals)

        arr = []

        for i in range(n):
            l, r, w = intervals[i]
            arr.append([l, r, w, i])

        # Sort by right endpoint
        arr.sort(key=lambda x: x[1])

        ends = [x[1] for x in arr]

        # Find previous non-overlapping interval
        prev = []

        for i in range(n):
            l = arr[i][0]

            # right < left
            j = bisect.bisect_left(ends, l) - 1
            prev.append(j)

        # dp[i][k] = best answer using first i intervals
        dp = [[(0, ()) for _ in range(5)] for _ in range(n + 1)]

        for i in range(1, n + 1):

            l, r, w, idx = arr[i - 1]

            for k in range(1, 5):

                # Option 1: don't take this interval
                dp[i][k] = dp[i - 1][k]

                # Option 2: take this interval
                p = prev[i - 1] + 1

                old_score, old_indices = dp[p][k - 1]

                new_score = old_score + w
                new_indices = tuple(sorted(old_indices + (idx,)))

                cur_score, cur_indices = dp[i][k]

                if new_score > cur_score:
                    dp[i][k] = (new_score, new_indices)

                elif new_score == cur_score:
                    if new_indices < cur_indices:
                        dp[i][k] = (new_score, new_indices)

        # Find best among 0,1,2,3,4 intervals
        best_score = 0
        best_indices = ()

        for k in range(5):
            score, indices = dp[n][k]

            if score > best_score:
                best_score = score
                best_indices = indices

            elif score == best_score and indices < best_indices:
                best_indices = indices

        return list(best_indices)
        