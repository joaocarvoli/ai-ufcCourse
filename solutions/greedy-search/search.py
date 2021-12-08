from Graph import Graph
from Built import createVertex, createEdges, getNumEdges


# This heuristic is about the smallest cost way from any city to Bucharest
heuristic = {'Arad': 366, 'Bucharest': 0, 'Craiova': 160, 'Drobeta': 242, 'Eforie': 161, 'Fagaras': 176, 'Giurgiu': 77,
             'Hirsova': 151, 'Iasi': 226, 'Lugoj': 244,
             'Mehadia': 241, 'Neamt': 234, 'Oradea': 380, 'Pitesti': 100, 'Rimnicu Vilcea': 193, 'Sibiu': 253,
             'Timisoara': 329, 'Urziceni': 80, 'Vaslui': 199, 'Zerind': 374}


def getHeuristic(city):
    return heuristic[city]


