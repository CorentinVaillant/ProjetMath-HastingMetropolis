import numpy as np

pi = np.pi
exp = np.exp

def norm_dist(mean,variance):
    return lambda x: (1/(np.sqrt(2*pi*variance))) * exp(- ((x-mean)**2)/(2*variance) )