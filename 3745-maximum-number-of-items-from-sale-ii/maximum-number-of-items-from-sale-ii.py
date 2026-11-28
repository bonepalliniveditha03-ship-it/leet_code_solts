class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        items.sort(key=lambda x: x[1])

        n = len(items)
        freq = [0] * (n + 1)

        for f, p in items:
            freq[f] += 1

        for i in range(1, n + 1):
            for j in range(i * 2, n + 1, i):
                freq[i] += freq[j]

        mn = items[0][1]
        ans = 0

        for f, p in items:
            if p >= 2 * mn:
                break

            cnt = freq[f] - 1
            take = min(cnt, budget // p)

            ans += take * 2
            budget -= take * p

        ans += budget // mn

        return ans