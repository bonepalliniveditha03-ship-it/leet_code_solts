import heapq

class Solution:
    def assignTasks(self, servers, tasks):
        free = [(w, i) for i, w in enumerate(servers)]
        heapq.heapify(free)

        busy = []
        ans = []
        current_time = 0

        for j in range(len(tasks)):

            # Time should never move backwards
            current_time = max(current_time, j)

            # Release all servers that have finished
            while busy and busy[0][0] <= current_time:
                end, weight, idx = heapq.heappop(busy)
                heapq.heappush(free, (weight, idx))

            # If no server is free, wait
            if not free:
                current_time = busy[0][0]

                # Release all servers free at this time
                while busy and busy[0][0] <= current_time:
                    end, weight, idx = heapq.heappop(busy)
                    heapq.heappush(free, (weight, idx))

            # Select the best available server
            weight, idx = heapq.heappop(free)

            ans.append(idx)

            # Calculate finishing time
            heapq.heappush(
                busy,
                (current_time + tasks[j], weight, idx)
            )

        return ans