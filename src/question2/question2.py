from collections import defaultdict
from queue import PriorityQueue
from typing import Optional, List


class Graph:
    def __init__(self):
        # Change to store edges as a list of tuples
        self.graph = defaultdict(list)

    def add_edge(self, from_city: str, to_city: str, cost: int):
        # Append (destination, cost) tuple to the list
        self.graph[from_city].append((to_city, cost))

    def uniform_cost_search(self, start: str, goal: str) -> Optional[List[str]]:
        frontier = PriorityQueue()
        frontier.put((0, start, [start]))  # (cost, city, path)
        explored = set()

        while not frontier.empty():
            cost, current_city, path = frontier.get()

            if current_city == goal:
                return path

            if current_city not in explored:
                explored.add(current_city)

                # Iterate through the list of (neighbor, cost) tuples
                for neighbor, edge_cost in self.graph[current_city]:
                    if neighbor not in explored:
                        new_cost = cost + edge_cost
                        new_path = path + [neighbor]
                        frontier.put((new_cost, neighbor, new_path))

        return None
