import networkx as nx 

def crearGrafo(numGrafo):
    city = nx.Graph()
    if numGrafo == 0:
        city.add_node("Frankfurt", pos=(2,5))
        city.add_node("Bamberg", pos=(4,3))
        city.add_node("Culmbach", pos=(2,0))
        city.add_node("Hof", pos=(6,5))
        city.add_node("Gera", pos=(6,0))

        city.add_edge("Frankfurt", "Bamberg", weight=23)
        city.add_edge("Frankfurt", "Culmbach", weight=40)
        city.add_edge("Bamberg", "Hof", weight=38)
        city.add_edge("Bamberg", "Culmbach", weight=40)
        city.add_edge("Hof", "Gera", weight=12)
        city.add_edge("Gera", "Bamberg", weight=95)
    else:
        city.add_node("A", pos=(2,5))
        city.add_node("B", pos=(2,0))
        city.add_node("C", pos=(4,5))
        city.add_node("D", pos=(6,5))
        city.add_node("E", pos=(4,3))

        city.add_edge("A", "C", weight=23)
        city.add_edge("A", "E", weight=40)
        city.add_edge("C", "D", weight=38)
        city.add_edge("D", "E", weight=40)
        city.add_edge("B", "A", weight=12)
        city.add_edge("B", "E", weight=95)
    return city 