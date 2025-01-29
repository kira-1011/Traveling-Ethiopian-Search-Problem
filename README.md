# Traveling Ethiopian Problem

This project implements various path-finding and search algorithms using Ethiopian cities as nodes. Each algorithm solves a different routing problem across Ethiopian cities.

## Project Structure

- `src/question1/question1.py`: Implement the Breadth-First Search (BFS) algorithm.
- `src/question2/question2.py`: Implement the Depth-First Search (DFS) algorithm.
- `src/question3/question3.py`: Implement the A\* Search algorithm.
- `src/question4/question4.py`: Implement the MiniMax Search algorithm.

## Requirements

- Python 3.6+
- No external dependencies required

## Questions and Solutions

### Question 1: Basic Graph Search

**Problem:** Find paths between Ethiopian cities using basic graph traversal algorithms.

**Solution:** Implements both Breadth-First Search (BFS) and Depth-First Search (DFS) to find paths between cities in an unweighted graph.

**Usage:**

Create graph and add edges

```
graph = Graph()
graph.add_edge("Addis Ababa", "Adama")
graph.add_edge("Adama", "Dire Dawa")
```

Find paths

```
bfs_path = graph.bfs("Addis Ababa", "Dire Dawa")
dfs_path = graph.dfs("Addis Ababa", "Dire Dawa")
print("BFS Path:", bfs_path)
print("DFS Path:", dfs_path)
```

### Question 2: Uniform Cost Search

**Problem:** Find the shortest path between cities considering actual road distances.

**Solution:** Implements Uniform Cost Search using a priority queue to find the optimal path based on cumulative edge costs.

**Usage:**
Create weighted graph

```
graph = Graph()
graph.add_edge("Addis Ababa", "Adama", 100) # 100 km distance
graph.add_edge("Adama", "Dire Dawa", 350) # 350 km distance
```

Find shortest path

```
path = graph.uniform_cost_search("Addis Ababa", "Dire Dawa")
print("Shortest path:", path)
```

### Question 3: A\* Search

**Problem:** Implement A\* search algorithm using straight-line distances to Moyale as heuristics.

**Solution:** Uses A\* search algorithm with admissible heuristics to find optimal paths. The heuristic values represent straight-line distances to the goal city.

**Usage:**

Create graph with heuristics

```
graph = Graph()
graph.add_edge("Addis Ababa", "Adama", 100)
graph.set_heuristic("Addis Ababa", 500) # Straight line distance to Moyale
graph.set_heuristic("Adama", 400) # Straight line distance to Moyale
```

Find optimal path

```
path = graph.a_star_search("Addis Ababa", "Moyale")
print("A Path:", path)
```

### Question 4: MiniMax Search for Coffee Quality

**Problem:** Find optimal coffee sourcing paths considering competing buyers using game theory.

**Solution:** Implements MiniMax algorithm to find the best path to high-quality coffee regions while considering an opposing player.

**Usage:**

Create game instance

```
game = MiniMaxSearch()
```

Add cities and coffee quality scores

```
game.add_edge("Addis Ababa", "Jimma")
game.add_state("Jimma", 8) # Coffee quality score
```

Find best path

```
score, path = game.minimax("Addis Ababa", depth=10, maximizing=True)
print(f"Best coffee quality score: {score}")
print(f"Best move from Addis Ababa: {path}")
```

## Running Examples

Each question has an example file demonstrating usage with Ethiopian cities data:

- `src/question1/example.py`
- `src/question2/example.py`
- `src/question3/example.py`
- `src/question4/example.py`
