#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 16:09:17 2019

@author: ammaagyei
"""
#1 --- PD
#0 --- control

import numpy as np
import csv
<<<<<<< HEAD
import matplotlib as plt

=======
import matplotlib.pyplot as plt
#import researchpy as rp
#from scipy.interpolate import griddata
#import pandas as pd
>>>>>>> d1a88f5cbd663c567be24603ed36fed58773ff89

def readdatafile():
    csv_file = open('Parkinsonsdiseasedataonly.csv')
    total_row = sum(1 for row in csv_file)
    csv_file.seek(0)
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0

    #Data Parsing and creating variables
    height  = np.zeros((total_row - 1,))                                 #empty array of zeros
    age  = np.zeros((total_row - 1,))
    weight = np.zeros((total_row - 1,))
    group = np.zeros((total_row-1,))
    speed = np.zeros((total_row-1,))
    index = 0

    for row in csv_reader:
        if line_count == 0:
            print('Column names are '+ str(row))
        elif line_count > 0:
            height[index] = ((float(row[6])) - 1.5) / (1.9 - 1.5)                 #normalizing of data 
            age[index] = ((float(row[5])) - 36) /(86 - 36)
            weight[index] = ((float(row[7])) - 47) / (101 - 47)
            group[index] = (int(row[2]))
            speed[index] = ((float(row[12])) - 0.413) / (1.542 - 0.413)
            index += 1
        
        line_count += 1
        
<<<<<<< HEAD
    
     #Trimming
    height = height[:index]   
    # age =                              #trimming data since last element in the arrays is 0
   # hemoglobin = hemoglobin[:index]
    #classification = classification[:index]
=======
    #normalizing data     #Trimming
    height = height[:index]   
    age =   age[:index]
    weight = weight[:index]
    group = group[:index]
    speed = speed[:index]

>>>>>>> d1a88f5cbd663c567be24603ed36fed58773ff89
    
    print('Processed ' +str(line_count)+' lines.')
    print(str(index)+' lines meet conditions.')
    csv_file.close()     

    return height, weight, age, group, speed

height,weight,age, group, speed = readdatafile()

#new_height = pd.Series(height)
#new_weight = pd.Series(weight)
#new_age = pd.Series(age)
#new_speed = pd.Series(speed)



#rp.summary_cont(readDataafile())


#x = np.corrcoef(speed,group)
#y = np.cov(age,group)
#def plotting(height,group, weight):
#    plt.figure()
#    plt.plot(weight[group == 1], height[group == 1],'r.',label = "Class 1")          #plots points with class 1 in red
#    plt.plot(weight[group == 0], height[group == 0], 'y.', label = "Class 0")        #plots points with class 0 in yellow
#    plt.xlabel("Height")
#    plt.ylabel("Weight")
#    plt.legend()
#    plt.show()
#

#plt.plot(speed[group == 1], height[group == 1], 'r.')
#plt.plot(speed[group == 0],height[group == 0], 'y.')
#plt.show()

plt.plot(speed[group == 1],'r.')
plt.plot(speed[group == 0], 'y.')
plt.show()

<<<<<<< HEAD
height,weight,age = readdatafile()
=======

>>>>>>> d1a88f5cbd663c567be24603ed36fed58773ff89
