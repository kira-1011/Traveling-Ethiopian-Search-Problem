from collections import deque, defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, from_city: str, to_city: str):
        self.graph[from_city].append(to_city)

    def bfs(self, start, goal):
        queue = deque([(start, [start])])
        visited = set()
        while queue:
            node, path = queue.popleft()
            if node == goal:
                return path
            if node not in visited:
                visited.add(node)
                for neighbor in self.graph.get(node, []):
                    queue.append((neighbor, path + [neighbor]))
        return None

    def dfs(self, start, goal):
        stack = [(start, [start])]
        visited = set()
        while stack:
            node, path = stack.pop()
            if node == goal:
                return path
            if node not in visited:
                visited.add(node)
                for neighbor in self.graph.get(node, []):
                    stack.append((neighbor, path + [neighbor]))
        return None
