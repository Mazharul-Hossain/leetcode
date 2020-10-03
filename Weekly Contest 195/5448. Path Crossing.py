class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited, pos = set(), (0,0)

        for p in path:
            visited.add(pos)
            x, y = pos
            if p == 'N':
                y += 1
            elif p == 'S':
                y -= 1
            elif p == 'E':
                x += 1
            elif p == 'W':
                x -= 1

            pos = (x, y)
            if pos in visited:
                return True
        return False