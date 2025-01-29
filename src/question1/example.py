from question1 import Graph

# Example usage
ethiopia_graph = {
    "Kartum": ["Humera", "Metema"],
    "Humera": ["Kartum", "Shire", "Metema"],
    "Metema": ["Kartum", "Humera", "Azezo"],
    "Shire": ["Humera", "Axum", "Debarke"],
    "Debarke": ["Shire", "Gondar"],
    "Axum": ["Shire", "Adwa"],
    "Adwa": ["Axum", "Adigrat"],
    "Adigrat": ["Adwa", "Mekelle", "Asmara"],
    "Asmara": ["Adigrat"],
    "Mekelle": ["Adigrat", "Sekota", "Alamata"],
    "Sekota": ["Mekelle", "Lalibela"],
    "Alamata": ["Mekelle", "Woldia"],
    "Lalibela": ["Sekota", "Debre Tabor"],
    "Debre Tabor": ["Lalibela", "Bahir Dar"],
    "Bahir Dar": ["Debre Tabor", "Azezo", "Finote Selam"],
    "Azezo": ["Bahir Dar", "Metema"],
    "Finote Selam": ["Bahir Dar", "Debre Markos"],
    "Debre Markos": ["Finote Selam", "Debre Sina", "Injibara"],
    "Debre Sina": ["Debre Markos"],
    "Injibara": ["Debre Markos", "Metekel"],
    "Metekel": ["Injibara", "Assosa"],
    "Assosa": ["Metekel", "Gambela"],
    "Gambela": ["Assosa", "Tepi"],
    "Tepi": ["Gambela", "Bonga", "Mezan Teferi"],
    "Mezan Teferi": ["Tepi"],
    "Bonga": ["Tepi", "Jimma"],
    "Jimma": ["Bonga", "Bedele"],
    "Bedele": ["Jimma", "Nekemte"],
    "Nekemte": ["Bedele", "Gimbi", "Ambo"],
    "Gimbi": ["Nekemte"],
    "Ambo": ["Nekemte", "Addis Ababa"],
    "Addis Ababa": ["Ambo", "Debre Birhan", "Adama"],
    "Debre Birhan": ["Addis Ababa", "Kemise"],
    "Kemise": ["Debre Birhan", "Dessie"],
    "Dessie": ["Kemise", "Woldia"],
    "Woldia": ["Dessie", "Alamata", "Fanti Rasu"],
    "Fanti Rasu": ["Woldia", "Kilbet Rasu"],
    "Kilbet Rasu": ["Fanti Rasu", "Samarra"],
    "Samarra": ["Kilbet Rasu"],
    "Adama": ["Addis Ababa", "Matahara"],
    "Matahara": ["Adama", "Awash"],
    "Awash": ["Matahara", "Chiro"],
    "Chiro": ["Awash", "Dire Dawa"],
    "Dire Dawa": ["Chiro", "Harar"],
    "Harar": ["Dire Dawa", "Babile"],
    "Babile": ["Harar", "Jijiga"],
    "Jijiga": ["Babile", "Degehabur"],
    "Degehabur": ["Jijiga", "Kebri Dehar"],
    "Kebri Dehar": ["Degehabur", "Gode"],
    "Gode": ["Kebri Dehar", "Dollo", "Liben"],
    "Dollo": ["Gode", "Moyale"],
    "Moyale": ["Dollo", "Yabello"],
    "Yabello": ["Moyale", "Konso", "Bule Hora"],
    "Konso": ["Yabello", "Arba Minch"],
    "Arba Minch": ["Konso", "Wolaita Sodo"],
    "Wolaita Sodo": ["Arba Minch", "Hossana"],
    "Hossana": ["Wolaita Sodo", "Shashemene"],
    "Shashemene": ["Hossana", "Hawassa", "Assasa"],
    "Hawassa": ["Shashemene", "Dilla"],
    "Dilla": ["Hawassa", "Bule Hora"],
    "Bule Hora": ["Dilla", "Yabello"],
    "Assasa": ["Shashemene", "Dodola"],
    "Dodola": ["Assasa", "Goba"],
    "Goba": ["Dodola", "Bale", "Sof Oumer"],
    "Bale": ["Goba", "Liben", "Sof Oumer"],
    "Liben": ["Gode", "Bale", "Sof Oumer"],
    "Sof Oumer": ["Goba", "Bale", "Liben"],
    "Bench Maji": ["Basketo"],
    "Basketo": ["Bench Maji", "Juba"],
    "Juba": ["Basketo"],
    "Gondar": ["Debarke"]
}

graph = Graph()

for from_city, to_cities in ethiopia_graph.items():
    for to_city in to_cities:
        graph.add_edge(from_city, to_city)

start_city = "Addis Ababa"
end_city = "Lalibela"

print("BFS Path:", graph.bfs(start_city, end_city))
print("DFS Path:", graph.dfs(start_city, end_city))
