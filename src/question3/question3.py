from collections import defaultdict
from queue import PriorityQueue
from typing import Optional, List


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.heuristics = {}

    def add_edge(self, from_city: str, to_city: str, cost: int):
        self.graph[from_city].append((to_city, cost))

    def set_heuristic(self, city: str, value: int):
        self.heuristics[city] = value

    def a_star_search(self, start: str, goal: str) -> Optional[List[str]]:
        frontier = PriorityQueue()
        # (f_score, g_score, city, path)
        frontier.put((self.heuristics[start], 0, start, [start]))
        explored = set()

        while not frontier.empty():
            f_score, g_score, current_city, path = frontier.get()

            if current_city == goal:
                return path

            if current_city not in explored:
                explored.add(current_city)

                for neighbor, cost in self.graph[current_city]:
                    if neighbor not in explored:
                        new_g_score = g_score + cost
                        new_f_score = new_g_score + self.heuristics[neighbor]
                        new_path = path + [neighbor]
                        frontier.put(
                            (new_f_score, new_g_score, neighbor, new_path))

        return None
