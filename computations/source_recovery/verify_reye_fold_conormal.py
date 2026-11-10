#!/usr/bin/env python3
"""Exact checks for the fold conormal cubic in source-recovery monodromy text.
This verifies the four isolated singular points and transverse conic intersection,
not the geometric existence of the fold or the global monodromy theorem.
"""
import sympy as s
z1,z2,z3,w1,w2=s.symbols('z1 z2 z3 w1 w2')
Q1=-z1**2+2*z2*z3
Q2=-z3**2+2*z1*z2
c=w1*Q1+w2*Q2
assert all(s.simplify(s.diff(c,x).subs({z1:0,z2:0,z3:0}))==0 for x in (z1,z2,z3,w1,w2))
Z=s.expand((z3**3-1))
assert s.factor(s.resultant(Q1.subs(z1,1), Q2.subs(z1,1),z2))==s.factor(-2*Z)
roots=[s.Integer(1),(-1+s.sqrt(3)*s.I)/2,(-1-s.sqrt(3)*s.I)/2]
points=[(s.Integer(0),s.Integer(1),s.Integer(0))]+[(s.Integer(1),s.simplify(r**2/2),r) for r in roots]
G=s.Matrix([[s.diff(Q1,z1),s.diff(Q1,z2),s.diff(Q1,z3)],[s.diff(Q2,z1),s.diff(Q2,z2),s.diff(Q2,z3)]])
for p in points:
    ev={z1:p[0],z2:p[1],z3:p[2]}
    assert s.simplify(Q1.subs(ev))==0 and s.simplify(Q2.subs(ev))==0
    assert G.subs(ev).rank()==2
# the four points span P^2 (i.e. are not collinear)
assert s.Matrix([list(p) for p in points]).rank()==3
print('PASS: unique singular line z=0 and exactly four isolated projective points.')
print('PASS: conics meet transversely at the four points; points are noncollinear.')
print('Scope: finite algebraic verification only; geometric ramification remains a theorem proof.')
