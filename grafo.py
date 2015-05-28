#-------------------------------------------------------------------------------
import networkx as nx
import matplotlib.pyplot as plt
g=nx.Graph()
g.add_edge(1,2)
g.add_edge(2,3)
g.add_edge(3,4)
g.add_edge(3,4)
g.add_edge(4,1)
g.add_edge(1,2,weigth=1)
g.add_edge(2,3,weigth=1)
g.add_edge(3,4,weigth=1)
g.add_edge(4,1,weigth=1)
nx.draw(g)
plt.show()
plt.show()
