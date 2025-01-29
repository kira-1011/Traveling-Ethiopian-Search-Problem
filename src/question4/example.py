from question4 import MiniMaxSearch

game = MiniMaxSearch()

# Add edges based on Figure 4
edges = {
    "Addis Ababa": ["Ambo", "Adama", "Buta Jira"],
    "Ambo": ["Gedo", "Nekemte"],
    "Gedo": ["Shambu", "Fincha"],
    "Nekemte": ["Gimbi", "Limu"],
    "Adama": ["Dire Dawa", "Mojo"],
    "Mojo": ["Kaffa", "Dilla"],
    "Dire Dawa": ["Harar", "Chiro"],
    "Buta Jira": ["Worabe", "Wolkite"],
    "Worabe": ["Hossana", "Durame"],
    "Wolkite": ["Bench Naji", "Tepi"]
}

# Add edges to the graph
for from_city, to_cities in edges.items():
    for to_city in to_cities:
        game.add_edge(from_city, to_city)

# Set coffee quality values for terminal states based on Figure 4
coffee_qualities = {
    "Shambu": 4,     # Lower quality
    "Fincha": 5,     # Lower quality
    "Gimbi": 8,      # High-quality coffee region
    "Limu": 8,       # Known for excellent coffee
    "Harar": 10,     # Premium coffee region
    "Chiro": 6,      # Moderate quality
    "Kaffa": 7,      # Birthplace of coffee
    "Dilla": 9,      # High-quality coffee region
    "Bench Naji": 5,  # Lower quality
    "Tepi": 6,       # Moderate quality
    "Durame": 5,     # Lower quality
    "Hossana": 6     # Moderate quality
}

# Set utility values
for city, quality in coffee_qualities.items():
    game.add_state(city, quality)

start_state = "Addis Ababa"
depth = 10
score, best_path = game.minimax(start_state, depth, True)

print(f"Best coffee quality score: {score}")
print(f"Best move from {start_state}: {best_path}")
