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
x_axis = [0.01,
          0.02,
          0.04,
          0.07,
          0.13,
          0.20,
          0.27,
          0.35,
          0.40,
          0.50,
          0.60,
          0.70,
          0.80,
          0.90,
          1.00,
          ] 
y_axis = [.01,
          .02,
          .04,
          .07,
          .13,
          .20,
          .27,
          .35,
          .40,
          .50,
          .60,
          .70,
          .80,
          .90,
          1.00,
          ]

size = [0,1.1,0,1.1] #xmin, xmax, ymin, ymax
plt.figure(1, figsize=(15, 15)) #size of the generated image
plt.xticks(np.arange(min(x_axis), max(x_axis)+1, 0.1)) #change intervals X
plt.yticks(np.arange(min(y_axis), max(y_axis)+1, 0.1)) #change intervals Y

"""
Main Prog
"""
def plotter(x,y,s):
    plt.xlabel('Voltage (V)') #X axis title
    plt.ylabel('Current (1x10^-7 mA)') #Y axis title
    plt.plot(x,y,color = 'red', label='1N4148') #Color and Label of the plot
    plt.title('Table 1') #Title of the plot 
    plt.axis(s) #Size 
    plt.grid(axis='both') #Show Grid
    plt.legend()
    
    
def main():
    plotter(x_axis,y_axis,size)
    plt.show()
    

if __name__ == "__main__":
    main()
