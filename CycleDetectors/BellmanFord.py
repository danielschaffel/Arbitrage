from collections import debque
infinity  = 1000
class BellmanFord:
    distTo = []
    edgeTo = []
    onQ = []
    adj = None 
    que = deque()
    cost = 0                        #number of calls to relax 
    def __init__(self,graph,source):
        for i in range(graph.get_V()):
            distTo[i] = infinity
        self.distTo[source] = 0
        self.adj = graph.adj

        #add source to queue
        #set onQ for source to true
        #while que isnt empty and no negative cycle
        #(with bellman ford might be able to create a list of all negative cycles)
        #pop from que and set onQ false
        #relax that vertex
    
    def relax(v):
        for i in self.adj[v]:
            w = i.edge_to()
            if(distTo[w] > distTo[v] + i.get_weight()):
                distTo[w] = distTo[v] + i.get_weight()
                edgeTo[w] = i
                if(onQ[w] is False):
                    que.push(w)
                    onQ[w] = True
            if cost%len(adj) is 0:
                find_negative_cycle()
