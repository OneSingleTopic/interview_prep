import collections

def count_islands(ocean_map: list[list[int]], n_rows, n_columns) -> int:
    n_islands = 0
    visited = set()

    def bfs(row, column):
        queue = collections.deque()
        queue.append((row, column))
        while queue:
            row, column = queue.popleft() # to do depth first search just popright()
            visited.add((row, column))
            if row < n_rows and column < n_columns:
                if ocean_map[row][column]:
                    queue.append((row, column+1))
                    queue.append((row+1, column))

    for row in range(n_rows):
        for column in range(n_columns):
            if (row, column) not in visited:
                bfs(row, column)
                n_islands+=ocean_map[row][column]

    return n_islands
        