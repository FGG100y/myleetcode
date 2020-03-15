#!/usr/bin/env python
# encoding: utf-8

# Graph and Digraph


class Node(object):
    """Docstring for Node. """

    def __init__(self, name):
        """TODO: to be defined. """
        self.name = name

    def get_name(self):
        return self.name

    def __str__(self):
        return self.name


class Edge(object):
    """description"""
    def __init__(self, src, dest):
        """
        :type src: Node
        :type dest: Node
        """
        self.src = src
        self.dest = dest

    def get_source(self):
        return self.src

    def get_destination(self):
        return self.dest

    def __str__(self):
        return f"{self.src.get_name()} -> {self.dest.get_name()}"


class WeightedEdge(Edge):
    """Docstring for WeightedEdge. """

    def __init__(self, weight=1.0):
        """TODO: to be defined. """
        Edge.__init__(self)
        self.weight = weight

    def get_weight(self):
        return self.weight

    def __str__(self):
        return f"{self.src.get_name()} ->({self.weight}) {self.dest.get_name()}"


class Digraph(object):
    """Directional graph
    """

    def __init__(self):
        """
        nodes is a list of the Nodes in the graph
        edegs is a mapping each node to a list of its children
        """
        self.nodes = []
        self.edges = {}

    def add_node(self, node):
        if node in self.nodes:
            raise ValueError("Duplicate node")
        else:
            self.nodes.append(node)
            self.edges[node] = []

    def add_edge(self, edge):
        src = edge.get_source()
        dest = edge.get_destination()
        if not (src in self.nodes and dest in self.nodes):
            raise ValueError("Node not in graph")
        self.edges[src].append(dest)

    def children_of(self, node):
        return self.edges[node]

    def has_node(self, node):
        return node in self.nodes

    def __str__(self):
        res = ""
        for src in self.nodes:
            for dest in self.edges[src]:
                res = res + src.get_name() + '->' + dest.get_name() + '\n'
        return res[:-1]


class Graph(Digraph):
    """description"""
    def add_edge(self, edge):
        Digraph.add_edge(self, edge)
        rev = Edge(edge.get_destination(), edge.get_source())
        Digraph.add_edge(self, rev)
