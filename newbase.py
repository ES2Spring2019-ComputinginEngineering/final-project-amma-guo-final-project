
Created on Tue Apr 16 16:09:17 2019

@author: ammaagyei
"""
#1 --- PD
#0 --- control

import numpy as np
import csv
import matplotlib.pyplot as plt
#import researchpy as rp

import scipy.stats as stats
from mpl_toolkits.mplot3d import Axes3D
from IPython import get_ipython
from scipy.stats import norm
import pandas as pd
ipython = get_ipython()
ipython.magic("matplotlib auto")


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
    
     #Trimming

    height = height[:index]   
    age =   age[:index]
    weight = weight[:index]
    group = group[:index]
    speed = speed[:index]
    
    print('Processed ' +str(line_count)+' lines.')
    print(str(index)+' lines meet conditions.')
    csv_file.close()     

    return height, weight, age, group, speed

def relationshipbetweenspeedandheight(speed,group,height):
    plt.figure()
    plt.plot(speed[group == 1], height[group == 1], 'r.')
    plt.plot(speed[group == 0], height[group == 0], 'y.')
    plt.title("Speed vs Height")
    plt.xlabel("Walking Speed")
    plt.ylabel("Height")
    plt.show()

def relationshipbetweenspeedandage(speed,age,group):
    plt.figure()
    plt.plot(speed[group == 1], age[group == 1], 'r.')
    plt.plot(speed[group == 0], age[group == 0], 'y.')
    plt.title("Speed vs Age")
    plt.xlabel("Walking Speed")
    plt.ylabel("Age")
    plt.show()

def relationshipbetweenspeedandweight(speed,weight,group):
    plt.figure()
    plt.plot(speed[group == 1], weight[group == 1], 'r.')
    plt.plot(speed[group == 0], weight[group == 0], 'y.')
    plt.title("Speed vs Weight")
    plt.xlabel("Walking Speed")
    plt.ylabel("Weight")
    plt.show()

def Parkinsons_speed_vs_Control_speed(speed):
    plt.figure()
    plt.plot(speed[group == 1], 'k.')
    plt.plot(speed[group == 0], 'r.')
    plt.xlabel("Walking Speed")
    plt.ylabel("Count")
    plt.show()

def ANOVA(speed,group):
    Fvalue, pvalue1 = stats.f_oneway(speed[group == 1],speed[group == 0])
    return Fvalue, pvalue1

def ttest(speed,group):
     t_statistic, pvalue2 = stats.ttest_ind(speed[group ==1], speed[group == 0])
     return t_statistic, pvalue2

def graphing_3D(speed,height,age,group):
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.scatter(speed[group == 1], height[group == 1], age[group == 1],c ='r', marker = 'o', label = "PD")
    ax.scatter(speed[group == 0], height[group == 0], age[group == 0],c = 'y', marker = 'o', label = "CO")
    plt.xlabel("Speed")
    plt.ylabel("Height")
    plt.show()

def histogramforPD(speed,group):
    plt.figure()
    plt.hist(speed[group == 1],rwidth = 0.95)
    plt.title("Speed vs Count for Parkinson's Disease")
    plt.xlabel("Walking Speed")
    plt.ylabel("Count") 
    plt.show()

def histogramforControl(speed,group):
    plt.figure()
    plt.hist(speed[group == 0], rwidth = 0.95)
    plt.title("Speed vs Count for Control Group")
    plt.xlabel("Walking Speed")
    plt.ylabel("Count") 
    plt.show()

def normaldistributionforPD(speed,group):
    plt.figure()
    plt.hist(speed[group == 1], normed = True)
    xt = plt.xticks()[0]
    xmin, xmax = min(xt), max(xt)
    lnspc = np.linspace(xmin, xmax, len(speed[group == 1]))
    mean, std = stats.norm.fit(speed[group == 1])   
    pdf_g = stats.norm.pdf(lnspc, mean, std) # now get theoretical values in our interval  
    plt.plot(lnspc, pdf_g, label="Norm") # plot it
    plt.title("Normal distribution for Parkinson's Disease")
    
def normaldistributionforCO(speed,group):
    plt.figure()
    plt.hist(speed[group == 0], normed = True)
    xt = plt.xticks()[0]
    xmin, xmax = min(xt), max(xt)
    lnspc = np.linspace(xmin, xmax, len(speed[group == 0]))
    mean, std = stats.norm.fit(speed[group == 0])   
    pdf_g = stats.norm.pdf(lnspc, mean, std) # now get theoretical values in our interval  
    plt.plot(lnspc, pdf_g, label="Norm") # plot it
    plt.title("Normal Distribution for Control Group")
    






    
    
height,weight,age, group, speed = readdatafile()
Parkinsons_speed_vs_Control_speed(speed)
relationshipbetweenspeedandage(speed,age,group)
relationshipbetweenspeedandweight(speed,weight,group)
relationshipbetweenspeedandheight(speed,group,height)
graphing_3D(speed,height,age,group)
Fvalue, pvalue1 = ANOVA(speed,group)
histogramforPD(speed,group)
histogramforControl(speed,group)
normaldistributionforPD(speed,group)
normaldistributionforCO(speed,group)
t_statistic, pvalue2 = ttest(speed,group)








#mean, std = norm.fit(speed[group == 1])
#
## Plot the histogram.
#plt.figure()
#plt.hist(speed[group == 1], bins=25, density=True, alpha=0.6, color='g')
## Plot the PDF.
#xmin, xmax = plt.xlim()
#x = np.linspace(xmin, xmax, 100)
#p = norm.pdf(x, mean, std)
#plt.plot(x, p, 'k', linewidth=2)
#title = "Fit results: mu = %.2f,  std = %.2f" % (mean, std)
#plt.title(title)
#plt.show()
#
#
#plt.figure()
#plt.hist(speed[group == 0], bins=25, density=True, alpha=0.6, color='g')
## Plot the PDF.
#xmin, xmax = plt.xlim()
#x = np.linspace(xmin, xmax, 100)
#p = norm.pdf(x, mean, std)
#plt.plot(x, p, 'k', linewidth=2)
#title = "Fit results: mu = %.2f,  std = %.2f" % (mean, std)
#plt.title(title)
#
#plt.show()
#
#data = speed[group==1]
#plt.figure()
#plt.hist(data, 
#         bins = np.arange(data.min(),data.max())+.5,  #dividers at half way point, rwidth-- customizes how it was drawn
#         rwidth = .75)
#plt.xlabel("Roll Total")
#plt.ylabel("Count") 
#plt.show()
#
#myTable = pd.crosstab(index = data, columns = "count")
#print(myTable)



#plt.figure()
#plt.hist(speed[group == 1], normed = True)
#xt = plt.xticks()[0]
#xmin, xmax = min(xt), max(xt)
#lnspc = np.linspace(xmin, xmax, len(speed[group == 1]))
#mean, std = stats.norm.fit(speed[group == 1])   
#pdf_g = stats.norm.pdf(lnspc, mean, std) # now get theoretical values in our interval  
#plt.plot(lnspc, pdf_g, label="Norm") # plot it
#
## exactly same as above
#ag,bg,cg = stats.gamma.fit(speed[group == 1])  
#pdf_gamma = stats.gamma.pdf(lnspc, ag, bg,cg)  
#plt.plot(lnspc, pdf_gamma, label="Gamma")
#
## guess what :) 
#ab,bb,cb,db = stats.beta.fit(speed[group == 1])  
#pdf_beta = stats.beta.pdf(lnspc, ab, bb,cb, db)  
#plt.plot(lnspc, pdf_beta, label="Beta")
#plt.show()  
#
#
#bins = np.linspace(-5, 5, 30)
#histogram, bins = np.histogram(speed[group == 1], bins=bins, normed=True)
#
#bin_centers = 0.5*(bins[1:] + bins[:-1])
#
## Compute the PDF on the bin centers from scipy distribution object
#pdf = stats.norm.pdf(bin_centers)
#
#from matplotlib import pyplot as plt
#plt.figure(figsize=(6, 4))
#plt.plot(bin_centers, histogram, label="Histogram of samples")
#plt.plot(bin_centers, pdf, label="PDF")
#plt.legend()
#plt.show()


