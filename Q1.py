# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 12:25:01 2020

@author: Soufiane
"""
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
#Global constant
L = 100
K = 10
eps = 1/L
X = np.linspace(0,1,L)
Y = np.linspace(0,1,L)

def marche_alea(x0,y0):
    x = x0
    y = y0
    while(np.abs(x)>eps and np.abs(x-1)>eps and np.abs(y)>eps and np.abs(y-1)>eps):
        r = random.randint(1,4)
        if (r==1): y = y-1/L
        elif(r==3): y = y+1/L
        elif(r==2): x = x-1/L
        else: x = x+1/L
    return (x,y)

def f(x,y):
    if (np.abs(x)<=2/L or np.abs(x-1)<=2/L): return 1
    return 0

def monte_carlo(x,y):
    Points = []
    for i in range(K):
        point = marche_alea(x,y)
        Points.append(f(point[0],point[1]))
    return sum(Points)/K

X, Y = np.meshgrid(X, Y)
monte_carlo = np.vectorize(monte_carlo)
Z = monte_carlo(X,Y)
plt.contourf(X,Y,Z,cmap=cm.jet)
plt.colorbar()
plt.show()