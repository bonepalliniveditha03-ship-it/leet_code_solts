from collections import deque

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:

        m = len(classroom)
        n = len(classroom[0])

        # Find start and give each litter an ID
        litter_no = {}
        k = 0

        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'S':
                    sx, sy = i, j

                elif classroom[i][j] == 'L':
                    litter_no[i * n + j] = k
                    k += 1

        # Bitmask when all litter is collected
        full_mask = (1 << k) - 1

        # best[(position, mask)] = maximum energy
        # with which we have reached this state
        best = {}

        start_pos = sx * n + sy
        best[(start_pos, 0)] = energy

        q = deque()
        q.append((sx, sy, energy, 0))

        moves = 0

        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        while q:

            # BFS level = number of moves
            for _ in range(len(q)):

                x, y, e, mask = q.popleft()

                # All litter collected
                if mask == full_mask:
                    return moves

                # Cannot move without energy
                if e == 0:
                    continue

                for dx, dy in directions:

                    nx = x + dx
                    ny = y + dy

                    # Outside grid
                    if nx < 0 or nx >= m or ny < 0 or ny >= n:
                        continue

                    # Wall
                    if classroom[nx][ny] == 'X':
                        continue

                    # One move consumes one energy
                    new_energy = e - 1
                    new_mask = mask

                    cell = classroom[nx][ny]
                    pos = nx * n + ny

                    # Recharge
                    if cell == 'R':
                        new_energy = energy

                    # Collect litter
                    elif cell == 'L':
                        new_mask |= 1 << litter_no[pos]

                    state = (pos, new_mask)

                    # If we have already reached the same
                    # position + mask with >= energy,
                    # this state is useless.
                    if best.get(state, -1) >= new_energy:
                        continue

                    best[state] = new_energy

                    q.append(
                        (nx, ny, new_energy, new_mask)
                    )

            moves += 1

        return -1