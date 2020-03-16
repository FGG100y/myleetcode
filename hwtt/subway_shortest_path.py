#!/usr/bin/env python
# encoding: utf-8

# shortest path: Depth-First-Search & Breadth-First-Search


#  from optimization_graph import Digraph
from optimization_graph import Graph
from optimization_graph import Node
from optimization_graph import Edge


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
            if shortest is None or len(path) < len(shortest):
                new_path = DFS(graph, node, end, path, shortest, to_print)
                if new_path is not None:
                    shortest = new_path
    return shortest


def test_dfs(graph, start, end, path, shortest, to_print=False):
    """return a shortest path from start to end in graph

    :type graph: Graph
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

    # this is not always ture to find the shortest path,
    # when it takes the longer path to the end, it returns the result,
    # but this do not guaranteed to find the shortest one,
    # it needs to loop over all the children of the first start to find the
    # shortest path
    # NOTE: this proble may involed with the implementation with Edge and Node
    # classes
    # Sun 15 Mar 2020 22:16:00

    #  test = graph.children_of(start)
    #  print(test)
    # test has two children node, the code below went though the first node
    # and return the result, but it is not the shortest path
    #  __import__('pdb').set_trace()
    for node in graph.children_of(start):
        if node not in path:  # advoid stuck in cycle path
            if shortest is None or len(path) < len(shortest):
                new_path = DFS(graph, node, end, path, shortest, to_print)
                if new_path is not None:
                    shortest = new_path
    return shortest


# DFS did not work correctly
def dfs_shortest_path(graph, start, end, to_print=False):
    """return a shortest_path from start to end in graph"""
    # function called DFS to initialize the seaching progress
    # path=[] : the current path being explored is empty
    # shortest is None : no path from start to end has yet been found
    return test_dfs(graph, start, end, [], None, to_print)
# ----------------------------------------------------------------------------


# ----------------------------------------------------------------------------
def BFS(graph, start, end, to_print=False):
    init_path = [start]
    path_queue = [init_path]
    if to_print:
        cpath = print_path(init_path)
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


# ----------------------------------------------------------------------------
# build the graph to test the DFS and BFS algorithms | HuaWei tech-exam
def build_graph(Anodes, Bnodes, Tnodes):
    """return a graph
    :type Anodes: list of Nodes
    :type Bnodes: list of Nodes
    :type Tnodes: list of Nodes
    """
    g = Graph()
    for n in Anodes:
        g.add_node(n)
    for n in Bnodes:
        g.add_node(n)
    for n in Tnodes:
        g.add_node(n)
    # add Anodes' edges to graph
    for i in range(len(Anodes)):
        if i == 8:
            g.add_edge(Edge(Anodes[i], Tnodes[0]))
            g.add_edge(Edge(Tnodes[0], Anodes[i+1]))
        elif i == 12:
            g.add_edge(Edge(Anodes[i], Tnodes[1]))
            g.add_edge(Edge(Tnodes[1], Anodes[i+1]))
        elif i == len(Anodes)-1:
            g.add_edge(Edge(Anodes[-1], Anodes[0]))
        else:
            g.add_edge(Edge(Anodes[i], Anodes[i+1]))
    # add Bnodes' edges to graph
    for i in range(len(Bnodes)-1):
        if i == 4:
            g.add_edge(Edge(Bnodes[i], Tnodes[0]))
            g.add_edge(Edge(Tnodes[0], Bnodes[i+1]))
        elif i == 9:
            g.add_edge(Edge(Bnodes[i], Tnodes[1]))
            g.add_edge(Edge(Tnodes[1], Bnodes[i+1]))
        else:
            g.add_edge(Edge(Bnodes[i], Bnodes[i+1]))

    return g
# ----------------------------------------------------------------------------


if __name__ == "__main__":
    # subway stations' names
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
    g = build_graph(Anodes, Bnodes, Tnodes)
    #  __import__('pdb').set_trace()
    # test the DFS and BFS
    sp = dfs_shortest_path(g, Anodes[12], Anodes[1], to_print=True)
    #  sp = BFS(g, start=Anodes[13], end=Bnodes[5])
    sp = print_path(sp)
    print(f"The shortest path is {sp}")
