class dfs():
    def __init__(self, graph, target):
       self.graph = graph
       self.target = target
       self.start = 1

    def solve_dfs(self):

        stack = [(self.start, [self.start])]
        visited = set()

        while stack:
            current, path = stack.pop()

            if current == self.target:
                print(f"Path found: {' -> '.join(map(str, path))}")
                return path
            
            if current not in visited:
                visited.add(current)

                for neighbor in self.graph.get(current, []):
                    if neighbor not in visited:
                        stack.append((neighbor, path+[neighbor]))
            
        print("Path not found!")
        return 0


graph = {
    1: [2, 3],
    2: [4, 5],
    3: [6],
    4: [],
    5: [6],
    6: []
}

target = int(input("Enter the target you want: "))
solve = dfs(graph, target)
solve.solve_dfs()
