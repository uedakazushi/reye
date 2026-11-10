#!/usr/bin/env python3
"""Exact finite checks for the Reye length-three cusp jet.
The analytic splitting and deformation functor theorem remain mathematical inputs.
"""
import sympy as sp
A, B, C, t, lam = sp.symbols("A B C t lam")
Q=sp.Matrix([[0,1,0,-1,0],[1,0,1,0,0],[0,1,0,1,0],[-1,0,1,0,0],[0,0,0,0,-1]])
v=sp.Matrix([2*A,-B,-A,2*B,3*C])
assert Q.det()==-4
assert sp.simplify(Q.inv()*v-sp.Matrix([-3*B/2,A/2,B/2,-3*A/2,-3*C]))==sp.zeros(5,1)
assert sp.expand((v.T*Q.inv()*v)[0])==-7*A*B-9*C*C
Delta=4+21*A*B+27*C*C
assert sp.simplify(sp.Rational(1,3)-(v.T*Q.inv()*v)[0]/4-Delta/12)==0
j=27*lam**3*(8-lam**3)**3/(1+lam**3)**3
assert j.subs(lam,1)==sp.Rational(9261,8)
kappa=sp.diff(j,lam).subs(lam,1)/3
assert sp.simplify(kappa+sp.Rational(17199,16))==0
assert sp.series((3+2*t**2)*(1+t**2)**(-sp.Rational(2,3)),t,0,6).removeO().expand()==3+t**4/3
assert sp.simplify(-2*kappa**2/(kappa*Delta/3)**2+18/Delta**2)==0
print("PASS: rational matrix identities, quartic Δ and cusp Jacobian")
x1,x2,x3,y1,y2,z=sp.symbols("x1 x2 x3 y1 y2 z")
coords=[x1,x2,x3,y1,y2]
F=x1**3+x2**3+x3**3+3*x1*x2*x3+x1*y1**2+2*x2*y1*y2+x3*y2**2
grad=[sp.diff(F,x) for x in coords]
for x in coords:
    G=sp.groebner(grad+[z*x-1],*coords,z,order="grevlex")
    assert G.contains(sp.Integer(1))
print("PASS: F0 has no projective singular point")
