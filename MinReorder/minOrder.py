from collections import deque
import time
from typing import List


# class Solution:

#     def minReorder(self, n: int, connections: List[List[int]]) -> int:
#         is_checked = [False] * n
#         graph = [[] for _ in range(n)]

#         for from_city, to_city in connections:
#             graph[from_city].append((to_city, 1))
#             graph.append([to_city, 0])
            

#         for from_city, to_city in connections:
#             if to_city == 0:
#                 self.city_could_reach_zero.append(from_city)
#                 self.city_pair_checked.append([from_city, to_city])
#             elif from_city == 0:
#                 self.city_could_reach_zero.append(to_city)
#                 change_number += 1
#                 self.city_pair_checked.append([from_city, to_city])
#             else:
#                 if to_city in self.city_could_reach_zero:
#                     self.city_could_reach_zero.append(from_city)
#                     self.city_pair_checked.append([from_city, to_city])
#                 elif from_city in self.city_could_reach_zero:
#                     self.city_could_reach_zero.append(to_city)
#                     change_number += 1
#                     self.city_pair_checked.append([from_city, to_city])
#                 else:
#                     continue
        
#         print(f'number is {n} city_pair num is {len(self.city_pair_checked)}')

#         for city_pair in self.city_pair_checked:
#             n -= 1
#             connections.remove(city_pair)

#         self.city_pair_checked.clear()

#         end = time.time()
#         print(f'time is {end - start}')

#         if len(connections) != 0:
#             change_number += self.minReorder(n, connections)
#             return change_number
#         else:
#             return change_number

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # 将道路存储成邻接表的形式
        graph = [[] for _ in range(n)]
        for u, v in connections:
            graph[u].append((v, 1))  # 方向为 u -> v
            graph[v].append((u, 0))  # 方向为 v -> u（需要修改方向）
        
        visited = [False] * n
        visited[0] = True
        queue = [0]
        count = 0
        
        # 广度优先搜索
        while queue:
            u = queue.pop(0)
            for v, d in graph[u]:
                if not visited[v]:
                    visited[v] = True
                    count += d
                    queue.append(v)
        
        return count
        

if __name__ == "__main__":
    solution = Solution()
    start = time.time()
    result = solution.minReorder(6, [[0,1],[1,3],[2,3],[4,0],[4,5]])
    end = time.time()
    print(end - start)
    print(result)
