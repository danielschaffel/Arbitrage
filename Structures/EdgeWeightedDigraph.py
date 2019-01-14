            
#actual graph api 
class Digraph:
    #V is the num of vertices in the graph
    #E is the number of edges in the graph
    #adj is the list holding list for each vertex of its adjacent vertices 
    V = None
    E = 0
    adj = None
    def __init__(self,V):
        self.V = V
        self.adj = []
        for i in range(self.V):
            self.adj.append([])

    def add_edge(self,edge):
        self.adj[edge.edge_from()].append(edge)
        self.E += 1

    def get_adj(self,v):
        return self.adj[v]
    
    def get_E(self):
        return self.E
    
    def get_V(self):
        return self.V
    


class DirectedEdge:
    #an edge representing from v to w (v -> w)
    #with "weight" of weight 
    v = None
    w = None
    weight = None
    
    def __init__(self,v,w,weight):
        self.v = v
        self.w = w
        self.weight = weight
    
    def get_weight(self):
        return self.weight
    
    def edge_from(self):
        return self.v
    
    def edge_to(self):
        return self.w
    
graph = Digraph(3)
edge1 = DirectedEdge(1,2,1.2)
edge2 = DirectedEdge(1,3,1.5)
edge3 = DirectedEdge(2,1,1.7)

graph.add_edge(edge1)
graph.add_edge(edge2)
graph.add_edge(edge3)
for i in range(len(graph.get_adj(1))):
    print(graph.get_adj(1)[i].edge_to())
    print(graph.get_adj(1)[i].get_weight()) 

print(graph.get_E())