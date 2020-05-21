"""
build class-based graph and run test searches
"""


from graph import Graph


# exec executes dynamically constructed strings(to do the assignments)
for name in "ABCDEFG":
    exec(f"{name} = Graph('{name}')")

# define the graph
A.arcs = [B, E, G]
B.arcs = [C]
C.arcs = [D, E]
D.arcs = [F]
E.arcs = [C, F, G]
G.arcs = [A]

A.search(G)
for (start, stop) in [(E, D), (A, G), (G, F), (B, A), (D, A)]:
    print(start.search(stop))
