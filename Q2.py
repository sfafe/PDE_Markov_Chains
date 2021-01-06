# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 19:53:25 2020

@author: Soufiane
"""


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
#Global constant
L = 100
K = 10
eps = 1/L
gamma = L**0.5
alpha = (gamma/L**2)/(4+gamma/L**2)
X = np.linspace(0,1,L)
Y = np.linspace(0,1,L)

def marche_alea(x0,y0):
    x = x0
    y = y0
    if(np.abs(x+1)<=eps or np.abs(y+1)<=eps): return (-1,-1)
    while(np.abs(x)>eps and np.abs(x-1)>eps and np.abs(y)>eps and np.abs(y-1)>eps):
        r = np.random.random_sample()
        if (0<=r<alpha): return (-1,-1)
        elif(alpha<=r<(3*alpha+1)/4): y = y-1/L
        elif((3*alpha+1)/4<=r<(alpha+1)/2): y = y+1/L
        elif((alpha+1)/2<=r<(3-alpha)/4): x = x-1/L
        elif((3-alpha)/4<=r<1) : x = x+1/L
    return (x,y)

def f(x,y):
    if ((x,y)==(-1,-1)): return 0
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