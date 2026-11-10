#!/usr/bin/env python3
"""Exact witness pencils for kernel degrees e=0,1,2 in the split-discriminant lemma."""
import sympy as sp
s,t=sp.symbols("s t")
A=sp.Matrix([[s,0],[t,s],[0,t]])
M2=sp.zeros(5)
for i in range(3):
 for j in range(2):
  M2[i,3+j]=A[i,j]; M2[3+j,i]=A[i,j]
assert M2*sp.Matrix([t*t,-s*t,s*s,0,0])==sp.zeros(5,1)
assert [M2.subs({s:1,t:0}).rank(),M2.subs({s:0,t:1}).rank(),M2.subs({s:2,t:3}).rank()]==[4,4,4]
M1=sp.zeros(5)
M1[0,2]=M1[2,0]=-t;M1[1,2]=M1[2,1]=s
M1[3,3]=s;M1[3,4]=M1[4,3]=t
assert M1*sp.Matrix([s,t,0,0,0])==sp.zeros(5,1)
assert sp.factor(M1[3:5,3:5].det())==-t*t
assert all(M1[i,j]==0 for i in [0,1,4] for j in [0,1,4])
M0=sp.zeros(5)
M0[0,2]=M0[2,0]=s;M0[1,3]=M0[3,1]=t
assert sp.factor(M0[:4,:4].det())==s*s*t*t
assert M0*sp.Matrix([0,0,0,0,1])==sp.zeros(5,1)
assert all(M0[i,j]==0 for i in [0,1,4] for j in [0,1,4])
print("PASS: e=0,1,2 examples with split discriminant and common 3-plane")
