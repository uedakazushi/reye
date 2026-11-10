#!/usr/bin/env python3
"""Exact Q-linear rank of the two stationary-plane conditions for each position.
One fixed (U,K), five U' representatives and several complementary K' values.
This checks the generic residual ranks (not the full special-stratum table).
"""
import sympy as sp
from itertools import combinations_with_replacement
from random import Random
z=sp.symbols('z0:5'); t=sp.symbols('t0:3')
# U=e0,e1,e2; K=e3,e4
# original kernel condition: second U-degree-2 K-degree-1 summand must vanish
mons=[]
for i,j,k in combinations_with_replacement(range(5),3):
    ks=(i,j,k)
    nu=sum(a<3 for a in ks)
    if nu==2:
        continue
    mons.append(z[i]*z[j]*z[k])
assert len(mons)==23
std=[sp.eye(5)[:,i] for i in range(5)]
reps={
    '(1,0)': [std[0],std[1]+std[3],std[2]+std[4]],
    '(2,0)': [std[0],std[1],std[2]+std[3]],
    '(1,1)': [std[0],std[1]+std[3],std[4]],
    '(1,2)': [std[0],std[3],std[4]],
    '(2,1)': [std[0],std[1],std[3]],
}
sub2=[t[0]**2,t[1]**2,t[2]**2,t[0]*t[1],t[0]*t[2],t[1]*t[2]]
R=Random(275)
for name, uvecs in reps.items():
    U=sp.Matrix.hstack(*uvecs)
    comp=[std[i] for i in range(5) if sp.Matrix.hstack(U,*[std[j] for j in range(i)]).rank() < sp.Matrix.hstack(U,*[std[j] for j in range(i+1)]).rank()]
    # simple greedy rank extension
    bases=list(uvecs)
    for ei in std:
        if len(bases)==5:break
        if sp.Matrix.hstack(*(bases+[ei])).rank()>len(bases):bases.append(ei)
    V=sp.Matrix.hstack(*bases[3:])
    ranks=[]
    for sample in range(4):
        A=sp.Matrix(3,2,lambda i,j:R.randrange(-3,4))
        K=V+U*A
        assert sp.Matrix.hstack(U,K).det()!=0
        sub={z[i]:(U*sp.Matrix(t))[i] for i in range(5)}
        rows=[]
        for kidx in range(2):
            for quad in sub2:
                rows.append([])
        for m in mons:
            for kidx in range(2):
                g=sum(K[i,kidx]*sp.diff(m,z[i]) for i in range(5))
                poly=sp.Poly(sp.expand(g.subs(sub, simultaneous=True)),*t)
                for j,q in enumerate(sub2):
                    rows[kidx*6+j].append(poly.coeff_monomial(q))
        M=sp.Matrix(rows)
        ranks.append(M.rank())
    print(name, 'second constraint rank samples',ranks,'delta',[12-x for x in ranks])
print('All exact rational computations completed.')
