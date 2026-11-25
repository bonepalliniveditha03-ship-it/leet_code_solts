class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        # Coordinate compression
        mp = {v: i + 1 for i, v in enumerate(sorted(set(nums)))}
        a = [mp[x] for x in nums] + [0]
        m = n + 1

        # Build suffix array
        p = sorted(range(m), key=lambda i: a[i])
        c = [0] * m

        for i in range(1, m):
            c[p[i]] = c[p[i - 1]] + (a[p[i]] != a[p[i - 1]])

        k = 0
        while (1 << k) < m:
            length = 1 << k
            pn = [(x - length) % m for x in p]

            cnt = [0] * (max(c) + 1)
            for x in pn:
                cnt[c[x]] += 1

            pos = [0] * len(cnt)
            for i in range(1, len(cnt)):
                pos[i] = pos[i - 1] + cnt[i - 1]

            p_new = [0] * m
            for x in pn:
                cl = c[x]
                p_new[pos[cl]] = x
                pos[cl] += 1

            p = p_new
            cn = [0] * m

            for i in range(1, m):
                cur, prev = p[i], p[i - 1]
                cn[cur] = cn[prev] + (
                    (c[cur], c[(cur + length) % m]) !=
                    (c[prev], c[(prev + length) % m])
                )

            c = cn
            k += 1

        sa = [x for x in p if x != n]

        # Build LCP array (Kasai algorithm)
        rank = [0] * n
        for i in range(n):
            rank[sa[i]] = i

        lcp = [0] * n
        h = 0

        for i in range(n):
            r = rank[i]

            if r == 0:
                h = 0
                continue

            j = sa[r - 1]

            while i + h < n and j + h < n and nums[i + h] == nums[j + h]:
                h += 1

            lcp[r] = h

            if h > 0:
                h -= 1

        # Find minimum unique subarray length
        ans = n

        for r in range(n):
            longest = lcp[r]

            if r + 1 < n:
                longest = max(longest, lcp[r + 1])

            length = longest + 1

            if length <= n - sa[r]:
                ans = min(ans, length)

        return ans