# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 21:01:49 2020

@author: Steve
"""

import matplotlib.pyplot as plt
import numpy as np

"""
Enter points here Here
"""
x_axis = [0,1,2,3,4,5,6] 
y_axis = [0,1,2,3,4,5,6]
size = [0,6,0,6] #x to x, y to y
plt.xticks(np.arange(min(x_axis), max(x_axis)+1, 0.5))
plt.yticks(np.arange(min(y_axis), max(y_axis)+1, 0.5))

def plotter(x,y,s):
    plt.xlabel('X-Axis')
    plt.ylabel('Y-Axis')
    plt.plot(x,y,color = 'red', label='red line')
    plt.title('Title')
    plt.axis(s)
    plt.grid(axis='both')
    plt.legend()
    
    
def main():
    plotter(x_axis,y_axis,size)
    plt.show()
    

if __name__ == "__main__":
    main()
