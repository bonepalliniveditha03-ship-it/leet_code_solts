class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        from collections import deque

        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        parent = [-1] * n
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        timer = 0

        stack = [(0, -1, 0)]

        while stack:
            node, par, state = stack.pop()

            if state == 0:
                parent[node] = par
                tin[node] = timer
                timer += 1

                stack.append((node, par, 1))

                for nei in reversed(graph[node]):
                    if nei != par:
                        depth[nei] = depth[node] + 1
                        stack.append((nei, node, 0))
            else:
                tout[node] = timer

        LOG = n.bit_length()
        up = [[-1] * n for _ in range(LOG)]
        up[0] = parent[:]

        for j in range(1, LOG):
            for i in range(n):
                p = up[j - 1][i]
                if p != -1:
                    up[j][i] = up[j - 1][p]

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]

            for j in range(LOG):
                if diff & (1 << j):
                    u = up[j][u]

            if u == v:
                return u

            for j in range(LOG - 1, -1, -1):
                if up[j][u] != up[j][v]:
                    u = up[j][u]
                    v = up[j][v]

            return parent[u]

        class Fenwick:
            def __init__(self, size):
                self.size = size
                self.bit = [0] * (size + 1)

            def add(self, i, val):
                i += 1
                while i <= self.size:
                    self.bit[i] ^= val
                    i += i & -i

            def query(self, i):
                result = 0
                i += 1
                while i > 0:
                    result ^= self.bit[i]
                    i -= i & -i
                return result

            def update_range(self, left, right, val):
                if left >= right:
                    return
                self.add(left, val)
                self.add(right, val)

        chars = list(s)
        bit = Fenwick(n + 1)

        for i in range(n):
            mask = 1 << (ord(chars[i]) - ord('a'))
            bit.update_range(tin[i], tout[i], mask)

        answer = []

        for q in queries:
            parts = q.split()

            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]

                old_mask = 1 << (ord(chars[u]) - ord('a'))
                new_mask = 1 << (ord(c) - ord('a'))

                bit.update_range(tin[u], tout[u], old_mask ^ new_mask)
                chars[u] = c

            else:
                u = int(parts[1])
                v = int(parts[2])

                w = lca(u, v)

                mask_u = bit.query(tin[u])
                mask_v = bit.query(tin[v])
                mask_w = 1 << (ord(chars[w]) - ord('a'))

                path_mask = mask_u ^ mask_v ^ mask_w

                answer.append((path_mask & (path_mask - 1)) == 0)

        return answer