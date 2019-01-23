#BASIC IDEA
#Do the Bellman Ford (VE) by relaxing every vertex and every edge
#any edge that changes on the Vth relaxation means there is a negative cycle
#use modified pathTo method to find the negative cycle and return
#Possibly continue with the Vth relaxation to find all negative cycles and 
#find the best of all of them
import sys
sys.path.append('/home/daniel/Desktop/Arbitrage/Structures')
from collections import deque
import EdgeWeightedDigraph

infinity = 100000
class BellmanFord:
    distTo = []
    edgeTo = []
    onQ = []
    queue = deque()
    #cost = 0 only if checking after every V relaxes for the cycle
    cycle = None
    graph = None

    def __init__(self,graph,source):
        self.graph = graph

        #initialize diff arrays
        for i in range(graph.get_V()):
            self.distTo.append(infinity)
            self.edgeTo.append(None)
            self.onQ.append(False)

        self.queue.append(source)
        self.onQ[source] = True
        self.distTo[source] = 0.0

        while len(self.queue) is not 0:
            v = self.queue.popleft()
            self.onQ[v] = False
            self.relax(v)
        
    def relax(self,v):
        for e in self.graph.get_adj(v):
            w = e.edge_to()
            #print(type(e.get_weight()), e.get_weight())
            #print(type(self.distTo[v]))
            if self.distTo[w] > self.distTo[v] + float(e.get_weight()):
                self.distTo[w] = self.distTo[v] + float(e.get_weight())
                self.edgeTo[w] = e
                if self.onQ[w] is False:
                    self.queue.append(w)
                    self.onQ[w] = True
    
    def printDistTo(self):
        for a in self.distTo:
            print(a)

edge0 = EdgeWeightedDigraph.DirectedEdge(0,1,10)
edge1 = EdgeWeightedDigraph.DirectedEdge(1,2,1)
edge2 = EdgeWeightedDigraph.DirectedEdge(1,3,2)
edge3 = EdgeWeightedDigraph.DirectedEdge(2,4,9)
edge4 = EdgeWeightedDigraph.DirectedEdge(3,4,4)
edge5 = EdgeWeightedDigraph.DirectedEdge(3,2,-10)

graph = EdgeWeightedDigraph.Digraph(6)
graph.add_edge(edge0)
graph.add_edge(edge1)
graph.add_edge(edge2)
graph.add_edge(edge3)
graph.add_edge(edge4)
graph.add_edge(edge5)

bf = BellmanFord(graph,1)
print("hello`")
bf.printDistTo()

 