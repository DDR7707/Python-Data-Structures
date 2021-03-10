'''   Implementation of Adjacency list    '''

class Vertex:
    def __init__(self,key):
        self.key = key
        self.connectedTo = {}

    def addNeighbor(self , nbr , weight = 0):
        self.connectedTo[nbr] = weight

    def getconnections(self):
        return self.connectedTo.keys()

    def getid(self):
        return self.key
    
    def getweight(self , nbr):
        return self.connectedTo[nbr]

class Graph:
    def __init__(self):
        self.vertexlist = {}
        self.count = 0

    def addvertex(self,key):
        new = Vertex(key)
        self.vertexlist[key] = new.connectedTo   
        self.count += 1

    def getvertex(self,key):
        if key in self.vertexlist:
            return self.vertexlist[key]
        else:
            self.addvertex(key)
        return self.vertexlist[key]

    def addedge(self,start,end,weight=0):
        if start in self.vertexlist:
            self.vertexlist[start][end] = weight
            return self
        else:
            self.addvertex(start)
            self.addedge(start,end,weight=0)

    def printing(self):
        print(self.vertexlist)

    def getvetrices(self):
        return [i for i in self.vertexlist]    

    def getedges(self,key):
        return self.vertexlist[key]

g = Graph()
g.addvertex(1)
g.addvertex(2)
g.addvertex(3)
g.printing()
g.addedge(1,3)
g.printing()
print(g.getvetrices())
print(g.getedges(1))

'''    BFS when given adjacency list    '''

def bfslist(sam,start):
    visited = []
    refer = []
    visited.append(start)
    refer.extend(sam[start])
    while len(refer) > 0:
        temp = refer.pop(0)
        if temp in visited:
            continue
        else:
            visited.append(temp)
            refer.extend(sam[temp])
    return visited           
    


graph = {0: [1, 2 ,3],
         1: [0,2],
         2: [0,1,4],
         3: [0],
         4: [2]}

print(bfslist(graph,0))


'''    BFS when given adjacency matrics    '''

sam = [[0,1,1,1,0],
       [1,0,1,0,0],
       [1,1,0,0,1],
       [1,0,0,0,0],
       [0,0,1,0,0]]

jam = [[0,1,0,1],
       [1,0,1,0],
       [0,1,0,1],
       [1,1,1,0]]       

def bfsmatrics(sam , start):
    visited = [start]
    refer = []
    i = start
    refer.extend(j for j,k in enumerate(sam[i]) if k == 1 )
    while len(refer) > 0:
        temp = refer.pop(0)
        if temp in visited:
            continue
        else:
            visited.append(temp)
            refer.extend(j for j,k in enumerate(sam[temp]) if k == 1)

    return visited            

print(bfsmatrics(sam , 0)) 
print(bfsmatrics(jam , 0)) 


'''    DFS when given adjacency list    '''

def dfslist(sam , start , visited = []):
    visited.append(start)
    refer = []
    refer.extend(sam[start])
    while len(refer) > 0 :
        temp = refer.pop(0)
        if temp in visited:
            continue

        else:
            dfslist(sam , temp , visited)    
    
    return visited

    
graph = {0: [1,2,3],
         1: [0,2],
         2: [0,1,4],
         3: [0],
         4: [2]}

print(dfslist(graph , 1))


'''    DFS when given adjacency matrics    '''

def dfsmatrics(sam , start , visited = []):
    visited.append(start)
    refer = []
    refer.extend(j for j,k in enumerate(sam[start]) if k == 1)
    while len(refer) > 0 :
        temp = refer.pop(0)
        if temp in visited:
            continue

        else:
            dfsmatrics(sam , temp , visited)

    return visited  

jam = [[0,1,1,1,0],
       [1,0,1,0,0],
       [1,1,0,0,1],
       [1,0,0,0,0],
       [0,0,1,0,0]]              

print(dfsmatrics(jam , 1))