#!/usr/bin/env python
# coding: utf-8

# # Binárna relácia
# <p>
#     Množinu R nazveme binárnou reláciou, ak jej jediné prvky sú usporiadané dvojice, t.j.
# </p>
# 
# <p>
# $$∀x ∈ R ∃y ∃z x = (y, z).$$
# </p>
# 
# <p>
# Príkladom takejto relácie je ľubovoľná podmnožina karteziánskeho súčinu A x B. V takomto prípade ju nazveme binárnou reláciou medzi prvkami  množín A a B (v tomto poradí) alebo tiež binárnou reláciou z množiny A do množiny B, tak hovoríme o relácii na množine A.
# </p>

# In[521]:


class BinaryRelation:
    
    def __init__(self,A=None,B=None,name="R"):
        self.name = name
        self.A = A
        self.B = B
        self.bRelation = set() #binarna relacia
        
    def setName(self, name):
        self.name = name
        
    def __repr__(self):
        dom = self.getSetA()
        rng = self.getSetB()
        r = f"{self.name} = {self.bRelation}\n"
        matrix = self.matrixRepresentation()
        r += f"   {str(rng)[1:-1]}\n"
        i = 0
        dom = list(dom)
        for elem in matrix:
            r += f"{dom[i]} {elem}\n"
            i += 1
        return r
    
    def getSetA(self):
        return self.A
    
    def getSetB(self):
        return self.B
        
    def dom(self):
        dom = set()
        a = list(self.bRelation)
        for elem in a:
            x,_ = elem
            dom.add(x)
        return dom
        
    def rng(self):
        rng = set()
        a = list(self.bRelation)
        for elem in a:
            _,x = elem
            rng.add(x)
        return rng
    
    def union(self, S):
        return self.bRelation.union(S)
        
    def intersection(self, S):
        return self.bRelation.intersection(S.bRelation)
    
    def composition(self, S):
        rng = self.rng()
        y = rng.intersection(S.dom())
        
        a = list(self.bRelation)
        b = list(S.bRelation)
        n = set()
        
        for e1 in a:
            i,j = e1
            if j in y:
                for e2 in b:
                    k,l = e2
                    if k == j:
                        n.add((i,l))
                        
        comp = BinaryRelation(self.A,self.B)
        comp.bRelation = n
        
        return comp
        
        
    def converse(self):
        n = set()
        
        for e in self.bRelation:
            i,j = e
            n.add((j,i))
        
        comp = BinaryRelation(self.A,self.B)
        comp.bRelation = n
        
        return comp
        
        
    def complement(self):
        n = set()
        
        for i in self.getSetA():
            for j in self.getSetB():
                if (i,j) not in self.bRelation:
                    n.add((i,j))
                    
        comp = BinaryRelation(self.A,self.B)
        comp.bRelation = n
        
        return comp
        
    def restriction(self, S):
        inter = self.getSetA().intersection(S)
        n = set()
        
        for elem in self.bRelation:
            i,j = elem
            if i in inter and j in inter:
                n.add(elem)
                
        res = BinaryRelation(self.A,self.A)
        res.bRelation = n
        
        return res
        
    def matrixRepresentation(self):
        dom = self.getSetA()
        rng = self.getSetB()
        matrix =  [[0 for col in range(len(rng))] for row in range(len(dom))]
        dom = list(dom)
        rng = list(rng)
        for elem in self.bRelation:
            i,j = elem
            matrix[dom.index(i)][rng.index(j)] = 1
        return matrix
    
    def isReflexive(self):
        for elem in self.bRelation:
            a,b = elem
            if (a,a) not in self.bRelation or (b,b) not in self.bRelation:
                return False
        return True
    
    def isSymetric(self):
        for elem in self.bRelation:
            a,b = elem
            if (b,a) not in self.bRelation:
                return False
        return True
        
    def isAntisymetric(self):
        for elem in self.bRelation:
            a,b = elem
            if (b,a) in self.bRelation and (a != b):
                return False
        return True
    
    def isTransitive(self):
        
        def relationWith():
            d = dict()
            for elem in self.bRelation:
                a,b = elem
                if a in d.keys():
                    d[a].add(b)
                else:
                    d[a] = {b}
                if b in d.keys():
                    pass
                else:
                    d[b] = set()
            return d
        
        d = relationWith()
        for elem in self.bRelation:
            a,b = elem
            for e in d[b]:
                if e not in d[a]:
                    return False
        return True
        


# In[522]:


from graphviz import Digraph
from IPython.display import IFrame, display

def makeGraph(relation,name="graph",filename='cluster.gv'):
    g = Digraph(name=name, node_attr={'shape': 'plaintext'})
    g.body.append(f'\t label="{relation.name}"')
    g.body.append('\t rankdir=LR;')
    
    with g.subgraph(name='cluster_dom', node_attr={'shape' : 'circle'}) as a:
        a.body.append('\t label="A"')
        for elem in relation.getSetA():
            a.node(str(elem))
    
    with g.subgraph(name='cluster_rng', node_attr={'shape' : 'circle'}) as b:
        b.body.append('\t label="B"')
        for elem in relation.getSetB():
            b.node(str(elem)+"R",str(elem))
            #node(name, label=None, _attributes=None, **attrs)
           
    for elem in relation.bRelation:
        a,b = elem
        g.edge(str(a),str(b)+"R")
        
    return g


# In[523]:


A = {1,2,3,4,5} 
B = {1,2,3,4,5}
b = BinaryRelation(A,B,"R(A→B)")
b.bRelation = {(1,3),(2,3),(2,4),(3,5),(3,2),(3,4),(4,4)}
print(b)
print(f"reflexive: {b.isReflexive()}")
print(f"symetric: {b.isSymetric()}")
print(f"antisymetric: {b.isAntisymetric()}")
print(f"transitive: {b.isTransitive()}")


g = makeGraph(b,"graph_01")
#print(g.source)
g.view()

IFrame("graph_01.gv.pdf", width=400, height=800)


# ## Complement
# 
# <p>
# Ak R je binárna relácia z množiny A do množiny B potom:
# </p>
# 
# <p>
# $$ R = \{(x, y) | ¬ xRy\} $$
# </p>
# 
# <p>
# je complement R.
# </p>

# In[524]:


A = {1,2,3,4,5} 
B = {1,2,3,4,5}
b = BinaryRelation(A,B,"R(A->B)")
b.bRelation = {(1,3),(2,3),(2,4),(5,2),(3,5),(4,1)}

compl = b.complement()
compl.setName("R comlement")
print(compl)

g = makeGraph(compl,"graph_02")
g.view()
IFrame("graph_02.gv.pdf", width=400, height=800)


# In[525]:


A = {1,2,3,4,5} 
B = {1,2,3,4,5}
s = BinaryRelation(A,B,"S(A→B)")
s.bRelation = {(3,3),(2,5),(2,4),(3,2),(4,1)}

print(s)

g = makeGraph(s,"graph_03")
g.view()
IFrame("graph_03.gv.pdf", width=400, height=800)


# ## Composition
# 
# <p>
# Ak R je binárna relácia z množiny A do množiny B a S je binárna relácia z množiny B do množiny C, tak potom:
# </p>
# 
# <p>
# $$ S ∘ R = \{(a, c) |  ∃b∈B, aRb ∧ bSc\} $$
# </p>
# 
# <p>
# je composition binárnej relácie R a S.
# </p>

# In[526]:


A = {1,2,3,4,5} 
B = {1,2,3,4,5}

b = BinaryRelation(A,B,"R(A→B)")
b.bRelation = {(1,3),(2,3),(2,4),(3,5),(3,2),(3,4),(4,4)}

s = BinaryRelation(A,B,"S(A→B)")
s.bRelation = {(3,3),(2,5),(2,4),(3,2),(4,1)}

comp = b.composition(s)
comp.setName("R x S")
print(comp)

g = makeGraph(comp,"graph_04")
g.view()
IFrame("graph_04.gv.pdf", width=400, height=800)


# ## Restriction
# 
# <p>
# Ak R je binárna relácia nad množinou A a S je podmnožina A potom: 
# </p>
# 
# <p>
# $$ R_{|S} = \{(x, y) | xRy ∧ x ∈ S ∧ y ∈ S\} $$
# </p>
# 
# <p>
# je restriction R ku S nad A.
# </p>

# In[527]:


A = {1,2,3,4,5} 

b = BinaryRelation(A,A,"R(A->A)")
b.bRelation = {(1,3),(2,3),(2,4),(3,5),(3,2),(3,4),(4,4)}

s = {2,3,5}

res = b.restriction(s)
res.setName("restriction")
print(res)
g = makeGraph(res,"graph_05")
g.view()
IFrame("graph_05.gv.pdf", width=400, height=800)


# ## Converse
# <p>
# Ak R je binárna relácia z množiny A do množiny B potom:
# </p>
# 
# <p>
# $$ R^T = \{(b, a) | a R b\}  $$
# </p>
# 
# <p>
# je converse R.
# </p>

# In[528]:


A = {1,2,3,4,5} 
B = {1,2,3,4,5}

b = BinaryRelation(A,B,"R(A->B)")
b.bRelation = {(1,3),(2,3),(2,4),(5,2),(3,5),(4,1)}

conv = b.converse()
conv.setName("converse")

print(conv)
g = makeGraph(conv,"graph_06")
g.view()
IFrame("graph_06.gv.pdf", width=400, height=800)

