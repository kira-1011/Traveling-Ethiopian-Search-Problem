from collections import defaultdict


class MiniMaxSearch:
    def __init__(self):
        self.graph = defaultdict(list)

        self.utilities = {}

    def add_state(self, state: str, utility: int):
        self.utilities[state] = utility

    def add_edge(self, from_state: str, to_state: str):
        self.graph[from_state].append(to_state)

    def minimax(self, state: str, depth: int, maximizing: bool) -> tuple[int, str]:
        if depth == 0 or state not in self.graph:
            return self.utilities.get(state, 0), state

        if maximizing:
            value = float('-inf')
            best_move = None
            for next_state in self.graph[state]:
                eval_score, _ = self.minimax(next_state, depth - 1, False)
                if eval_score > value:
                    value = eval_score
                    best_move = next_state
            return value, best_move
        else:
            value = float('inf')
            best_move = None
            for next_state in self.graph[state]:
                eval_score, _ = self.minimax(next_state, depth - 1, True)
                if eval_score < value:
                    value = eval_score
                    best_move = next_state
            return value, best_move
