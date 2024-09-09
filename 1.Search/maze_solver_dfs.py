class MazeSolver():
    def __init__(self, maze):
        self.rows = len(maze)
        self.cols = len(maze[0])

        self.maze = [list(row) for row in maze] #converting the maze to 2D list of characters

        self.start = self.find_position('A')
        self.end = self.find_position('B')

    def find_position(self, char):

        for r in range(self.rows):
            for c in range(self.cols):
                if self.maze[r][c] == char:
                    return (r, c)
        return None
    
    def print_maze(self):
        for row in self.maze:
            print("".join(row))
        print()
    
    def is_valid_move(self, r, c, visited):
        if 0<=r<self.rows and 0<=c<self.cols and self.maze[r][c] != '#' and (r, c) not in visited:
            return True
        return False
    
    def dfs(self):

        stack = [(self.start, [])]
        visited = set()

        while stack:
            (current, path) = stack.pop()
            r, c = current

            if current == self.end:
                for pr, pc in path:
                    self.maze[pr][pc] = '*'
                self.maze[self.start[0]][self.start[1]] = 'A'
                self.maze[self.end[0]][self.end[0]] = 'B'
                return True
            
            visited.add((r, c))

            moves = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]

            for nr, nc in moves:
                if self.is_valid_move(nr, nc, visited):
                    stack.append(((nr, nc), path + [(r, c)]))
        return False

maze = [
    "######",
    "##B  ##",
    "#  #  ##",
    "#  ###",
    "#    A"
]

solver = MazeSolver(maze)
if solver.dfs():
    solver.print_maze()
else:
    print("No path found!")
