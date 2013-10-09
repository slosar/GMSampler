#!/usr/bin/env python
from game import *
from scipy import *
import pylab, sys
import scipy.linalg as linalg

## This is a large N test

N=20
err2=array(range(1,N+1))**2

def like(x):
    return -(x*x/(2*err2)).sum()

def likemany(x):
    res=map(like,x)
    return res


st=array([random.uniform(-1,1) for i in range(N)])

mx=array(sqrt(err2))


ga=Game(likemany,st,mx)
ga.N1=1000
ga.N1f=0
ga.blow=1.1 ## unbeliveably sensitive to this
ga.fastpars=[1]
ga.mineffsamp=500
ga.maxiter=10000
ga.run()




m=zeros(N)
m2=zeros(N)
sw=0.0
for sa in ga.sample_list:
    m+=sa.pars*sa.we
    m2+=sa.pars**2*sa.we
    sw+=sa.we
    

m/=sw
m2/=sw
m2-=m*m
print m
print sqrt(m2)

