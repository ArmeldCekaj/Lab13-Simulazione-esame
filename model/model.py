import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._graph = nx.DiGraph()
        self._idMap = {}
    def getYear(self):
        return DAO.getYear()

    def buildGraph(self, year):
        self._idMap = DAO.get_nodes(self._idMap, year)
        self._graph.add_nodes_from(list(self._idMap.values()))
        edges = DAO.getAllEdges(self._idMap, year)
        for e in edges:
            if e.node1 in self._graph and e.node2 in self._graph:
                self._graph.add_edge(e.node1, e.node2, weight=e.weight)

    def getGraphDetails(self):
        return self._graph.number_of_nodes(), self._graph.number_of_edges()

    def analyze(self):
        result = []
        for node1 in self._graph.nodes:
            score = self._graph.out_degree(node1) - self._graph.in_degree(node1)
            result.append((node1, score))
        result.sort(key=lambda x: x[1], reverse=True)
        return result[0]


