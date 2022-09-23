# Pacific Atlantic Water Flow
import collections


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        pacific = set()
        atlantic = set()
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def bfs(i, j, visit):
            q = collections.deque([(i, j)])
            while q:
                i, j = q.popleft()
                if (i, j) in visit:
                    continue
                visit.add((i, j))
                for d in dirs:
                    di, dj = i + d[0], j + d[1]
                    if 0 <= di < rows and 0 <= dj < cols and heights[di][dj] >= heights[i][j] and (di, dj) not in q:
                        q.append((di, dj))

        for i in range(rows):
            bfs(i, 0, pacific)
            bfs(i, cols - 1, atlantic)
        for i in range(cols):
            bfs(0, i, pacific)
            bfs(rows - 1, i, atlantic)

        # print(pacific)
        # print(atlantic)
        return list(pacific.intersection(atlantic))


obj = Solution()
print(obj.pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))