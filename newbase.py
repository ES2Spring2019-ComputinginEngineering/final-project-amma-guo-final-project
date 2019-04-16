#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 16:09:17 2019

@author: ammaagyei
"""


import numpy as np
import csv

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
    index = 0

    for row in csv_reader:
        if line_count == 0:
            print('Column names are '+ str(row))
        elif line_count > 0:
            height[index] = (float(row[7]))                   #normalizing of data 
            age[index] = (float(row[6]))
            weight[index] = (float(row[8]))
            index += 1
        line_count += 1
        
    
     #Trimming
     height = height[:index]   
     age =                              #trimming data since last element in the arrays is 0
   # hemoglobin = hemoglobin[:index]
    #classification = classification[:index]
    
    print('Processed ' +str(line_count)+' lines.')
    print(str(index)+' lines meet conditions.')
    csv_file.close()     

    return height, weight, age

height,weight,age = readdatafile()

#def pot