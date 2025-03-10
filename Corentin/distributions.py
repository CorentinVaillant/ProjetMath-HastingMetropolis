import numpy as np

from math import factorial, comb

pi = np.pi
exp = np.exp



def poisson(l):
    return lambda k: ((l**k)/(factorial(k)))*np.exp(-l)

def binomial(n,p):
    return lambda k: comb(n,k) * p**k * (1-p)**(n-k)

def geo(p):
    return lambda k: p*((1-p)**(k-1))