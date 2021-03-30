#!/usr/bin/env python
# coding: utf-8

# <b>Binárna relácia</b>
# <p>Množinu R nazveme binárnou reláciou, ak jej jediné prvky sú usporiadané dvojice, t.j.</p>
# <b>∀x ∈ R ∃y ∃z x = (y, z).</b>
# <div>Príkladom takejto relácie je ľubovoľná podmnožina karteziánskeho súčinu A x B. V takomto prípade ju nazveme binárnou reláciou medzi prvkami  množín A a B (v tomto poradí) alebo tiež binárnou reláciou z množiny A do množiny B, tak hovoríme o relácii na množine A.</div>

# In[148]:


class BinaryRelation:
    
    def __init__(self, name="R"):
        self.name = name
        self.bRelation = set() #binarna relacia
        
    def setName(self, name):
        self.name = name
        
    def __repr__(self):
        dom = self.dom()
        rng = self.rng()
        r = f"{self.name} = {self.bRelation}\n"
        matrix = self.matrixRepresentation()
        r += f"   {str(rng)[1:-1]}\n"
        i = 0
        dom = list(dom)
        for elem in matrix:
            r += f"{dom[i]} {elem}\n"
            i += 1
        return r
        
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
                        
        comp = BinaryRelation()
        comp.bRelation = n
        
        return comp
        
    def converse(self):
        n = set()
        
        for e in self.bRelation:
            i,j = e
            n.add((j,i))
        
        comp = BinaryRelation()
        comp.bRelation = n
        
        return comp
        
        
    def complement(self):
        n = set()
        
        for i in self.dom():
            for j in self.rng():
                if (i,j) not in self.bRelation:
                    n.add((i,j))
                    
        comp = BinaryRelation()
        comp.bRelation = n
        
        return comp
        
    def restriction(self, S):
        inter = self.intersection(S)
        n = set()
        
        for elem in self.bRelation:
            if elem not in inter:
                n.add(elem)
                
        res = BinaryRelation()
        res.bRelation = n
        
        return res
        
    def matrixRepresentation(self):
        dom = self.dom()
        rng = self.rng()
        matrix =  [[0 for col in range(len(rng))] for row in range(len(dom))]
        dom = list(dom)
        rng = list(rng)
        for elem in self.bRelation:
            i,j = elem
            matrix[dom.index(i)][rng.index(j)] = 1
        return matrix
        


# In[149]:


b = BinaryRelation("R")
b.bRelation = {(1,4),(1,7),(2,5),(3,4)}
print(b)


# In[151]:


bb = BinaryRelation("Rs")
bb.bRelation = {(1,4),(3,4)}
print(b.restriction(bb))


# In[138]:


compl = b.complement()
compl.setName("R comlement")
print(compl)


# In[125]:


s = BinaryRelation("S")
s.bRelation = {(4,8),(3,7),(5,7),(3,2)}
print(s)


# In[126]:


comp = b.composition(s)
comp.setName("R x S")
print(comp)


# In[127]:


conv = b.converse()
conv.setName("RT")
print(conv)

