#!/usr/bin/env python3
"""Exact arithmetic certificates for the recovered Reye stationary-plane core.
This verifies only finite polynomial and intersection-number identities.
"""
import itertools
import sympy as sp
x,y,z,lam=sp.symbols('x y z lam')
r=[2*x,2*y,2*z,x+y,x+z,y+z]
C={i:sp.expand(sum(sp.prod(t) for t in itertools.combinations(r,i))) for i in [2,3,4]}
e1,e2,e3=x+y+z,x*y+x*z+y*z,x*y*z
assert sp.expand(C[2]-(5*e1**2+5*e2))==0
assert sp.expand(C[3]-(2*e1**3+11*e1*e2+7*e3))==0
assert sp.expand(C[4]-(6*e1**2*e2+4*e2**2+14*e1*e3))==0
D=(x-y)*(x-z)*(y-z)
def integral(p):
  return sp.Poly(sp.expand(p*D),x,y,z).coeff_monomial(x**4*y**3*z**2)
assert [integral(p) for p in [e1**6,e1**4*e2,e1**3*e3,e1**2*e2**2,e1*e2*e3,e2**3,e3**2]]==[5,3,1,2,1,1,1]
assert integral(C[3]**2-C[2]*C[4])==275
M=2*lam*sp.Matrix([[1,1,0],[1,0,1],[0,1,1]])
assert sp.simplify(M.det()**2-256*lam**6)==0
Dl=sp.Matrix([[0,1,0,1,0,0],[0,0,1,0,lam,0],[lam,0,0,0,0,1],[1,0,0,0,0,lam],[0,lam,0,1,0,0],[0,0,1,0,1,0]])
assert sp.factor(Dl.det())==(lam-1)**3*(lam+1)
assert Dl.subs(lam,-1).rank()==5
assert Dl.subs(lam,-1)*sp.Matrix([1,0,0,0,0,1])==sp.zeros(6,1)
a,b,c=sp.symbols('a b c')
H=sp.Matrix([[lam*a,c,b],[c,lam*b,a],[b,a,lam*c]])
assert sp.expand(H.det()-((lam**3+2)*a*b*c-lam*(a**3+b**3+c**3)))==0
assert sp.expand((lam**3+2)**3-27*lam**3-(lam**3-1)**2*(lam**3+8))==0
j=27*lam**3*(lam**3+8)**3/(lam**3-1)**3
assert sp.simplify(j.subs(lam,-1)-sp.Rational(9261,8))==0
assert sp.simplify(sp.diff(j,lam).subs(lam,-1)-sp.Rational(51597,16))==0
print('PASS: Chern polynomial identities, Schubert integral = 275, two linearized determinants, Hesse net, j(-1) and j\'(-1).')
