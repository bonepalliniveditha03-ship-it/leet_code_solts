from typing import List

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        size = 4 * n

        tree = [0] * size
        lazy = [0] * size
        squares = [0] * size

        def update(node, start, end, l, r, val):
            if l > end or r < start:
                return

            if l <= start and end <= r:
                squares[node] = (squares[node] + 2 * val * tree[node] + (end - start + 1) * val * val) % MOD
                tree[node] = (tree[node] + (end - start + 1) * val) % MOD
                lazy[node] = (lazy[node] + val) % MOD
                return

            mid = (start + end) // 2
            push(node, start, end, mid)

            update(node * 2, start, mid, l, r, val)
            update(node * 2 + 1, mid + 1, end, l, r, val)

            tree[node] = (tree[node * 2] + tree[node * 2 + 1]) % MOD
            squares[node] = (squares[node * 2] + squares[node * 2 + 1]) % MOD

        def push(node, start, end, mid):
            val = lazy[node]
            if val == 0:
                return

            for child, left, right in [
                (node * 2, start, mid),
                (node * 2 + 1, mid + 1, end)
            ]:
                length = right - left + 1
                squares[child] = (squares[child] + 2 * val * tree[child] + length * val * val) % MOD
                tree[child] = (tree[child] + length * val) % MOD
                lazy[child] = (lazy[child] + val) % MOD

            lazy[node] = 0

        last = {}
        ans = 0

        for i, x in enumerate(nums):
            prev = last.get(x, -1) + 1

            update(1, 0, n - 1, prev, i, 1)

            ans = (ans + squares[1]) % MOD
            last[x] = i

        return ans

        