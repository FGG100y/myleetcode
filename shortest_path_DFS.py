#!/usr/bin/env python
# encoding: utf-8

# shortest path: Depth-First-Search


#  from .optimization_graph import Digraph
from .optimization_graph import Graph
from .optimization_graph import Node


def print_path(path):
    """
    :type path: list of Nodes
    :rtype str
    """
    res = ""
    for i in range(len(path)):
        res += str(path[i])
        if i != len(path) - 1:
            res += '->'
    return res


# ----------------------------------------------------------------------------
def DFS(graph, start, end, path, shortest, to_print=False):
    """return a shortest path from start to end in graph

    :type graph: Digraph
    :type start: Node
    :type end: Node
    :type path: list of Nodes
    :type shortest: list of Nodes
    :type to_print: boolean
    """
    path += [start]
    if to_print:
        cpath = print_path(path)
        print(f"Current DFS path: {cpath}")
    if start == end:
        return path
    for node in graph.children_of(start):
        if node not in path:  # advoid stuck in cycle path
            if shortest == None or len(path) < len(shortest):
                new_path = DFS(graph, node, end, path, shortest, to_print)
                if new_path != None:
                    shortest = new_path
    return shortest


def shortest_path(graph, start, end, to_print=False):
    """return a shortest_path from start to end in graph"""
    # function called DFS to initialize the seaching progress
    # path=[] : the current path being explored is empty
    # shortest is None : no path from start to end has yet been found
    return DFS(graph, start, end, [], None, to_print)


def test_sp_dfs():
    sp = shortest_path(g, Anodes[0], Anodes[18], to_print=True)
    print(f"The shortest path is {sp}")
# ----------------------------------------------------------------------------


# ----------------------------------------------------------------------------
def BFS(graph, start, end, to_print=False):
    init_path = [start]
    path_queue = [init_path]
    if to_print:
        cpath = print_path(path)
        print(f"Current BFS path: {cpath}")
    while len(path_queue) != 0:
        # get and rm oldest element in path_queue
        tmp_path = path_queue.pop(0)
        cpath = print_path(tmp_path)
        print(f"Current BFS path: {cpath}")
        last_node = tmp_path[-1]
        if last_node == end:
            return tmp_path
        for next_node in graph.children_of(last_node):
            if next_node not in tmp_path:
                new_path = tmp_path + [next_node]
                path_queue.append(new_path)
    return None


def test_sp_bfs():
    sp = BFS(g, start, end)
    print(f"The shortest path is {sp}")


# ----------------------------------------------------------------------------
# build the graph to test the DFS and BFS algorithms
def build_graph():
    Anodes, Bnodes, Tnodes = [], [], []
    # line A stations
    for name in range(1, 19):
        sname = 'A' + str(name)
        Anodes.append(Node(sname))
    # line B stations
    for name in range(1, 16):
        sname = 'B' + str(name)
        Bnodes.append(Node(sname))
    # Transfer stations
    for name in range(1, 3):
        sname = 'T' + str(name)
        Tnodes.append(Node(sname))

    # create a graph
    g = Graph()
    for n in Anodes:
        g.add_node(n)
    for n in Bnodes:
        g.add_node(n)
    for n in Tnodes:
        g.add_node(n)
    # add edges to graph's nodes
    #  g.add_edge(Edge(nodes[], nodes[]))
    #
# ----------------------------------------------------------------------------

if __name__ == "__main__":
    test_sp_dfs()
