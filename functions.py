

#1 --- PD
#0 --- control

import numpy as np
import csv
import matplotlib.pyplot as plt
from matplotlib_venn import venn2, venn2_circles
from sklearn.linear_model import LinearRegression
import scipy.stats as stats
from mpl_toolkits.mplot3d import Axes3D
from IPython import get_ipython
#from scipy.stats import norm
import pandas as pd
import statsmodels.formula.api as smf
ipython = get_ipython()
ipython.magic("matplotlib auto") #change to auto


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
    height = height[:index]                                                     #trimming data since last element in the arrays is 0
    age =   age[:index]
    weight = weight[:index]
    group = group[:index]
    speed = speed[:index]
    
    print('Processed ' +str(line_count)+' lines.')
    print(str(index)+' lines meet conditions.')
    csv_file.close()     

    return height, weight, age, group, speed

def relationshipbetweenspeedandheightforCO(speed,group,height):                 #Plots Speed vs Height for Control group
    plt.figure()
    plt.plot(height[group == 0], speed[group == 0], 'b.')
    x = height[group == 0]
    y = speed[group == 0]
    x = x[:, np.newaxis]
    y = y[:, np.newaxis]
    model = LinearRegression()                                                  #plotting line of best fit
    model.fit(x, y)
    y_pred = model.predict(x)
    plt.plot(x, y_pred, color = 'r')
    plt.title("Height vs Speed for CO")
    plt.ylabel("Walking Speed")
    plt.xlabel("Height")
    plt.show()

def relationshipbetweenspeedandheightforPD(speed,group,height):                 #Plots Speed vs Height for Parkinson's Disease Group
    plt.figure()
    plt.plot(height[group == 1], speed[group == 1], 'b.')
    x = height[group == 1]
    y = speed[group == 1]
    x = x[:, np.newaxis]
    y = y[:, np.newaxis]
    model = LinearRegression()                                                  #Plots line of best fit
    model.fit(x, y)
    y_pred = model.predict(x)
    plt.plot(x, y_pred, color = 'r')
    plt.title("Height vs Speed for PD")
    plt.ylabel("Walking Speed")
    plt.xlabel("Height")
    plt.show()
    
def relationshipbetweenspeedandageforPD(speed,age,group):                       #plot speed vs age for Parkinson's Disease group
    plt.figure()
    plt.plot(age[group == 1], speed[group == 1], 'b.')
    x = age[group == 1]
    y = speed[group == 1]
    x = x[:, np.newaxis]
    y = y[:, np.newaxis]
    model = LinearRegression()                                                  #plot line of best fit
    model.fit(x, y)
    y_pred = model.predict(x)
    plt.plot(x, y_pred, color = 'r')
    plt.title("Age vs Speed for PD")
    plt.ylabel("Walking Speed")
    plt.xlabel("Age")
    plt.show()

def relationshipbetweenspeedandageforCO(speed,age,group):                       #plot speed vs age for control group
    plt.figure()
    plt.plot(age[group == 0], speed[group == 0], 'b.')
    plt.title("Age vs Speed for CO")
    plt.ylabel("Walking Speed")
    plt.xlabel("Age")
    x = age[group == 0]
    y = speed[group == 0]
    x = x[:, np.newaxis]
    y = y[:, np.newaxis]
    model = LinearRegression()                                                  #plot line of best fit
    model.fit(x, y)
    y_pred = model.predict(x)
    plt.plot(x, y_pred, color = 'r')
    plt.show()

def relationshipbetweenspeedandweightforCO(speed,weight,group):                 #Plots Speed vs Weight for Parkinson's Disease group
    plt.figure()
    plt.plot(weight[group == 0], speed[group == 0], 'y.')
    plt.title("Weight vs Speed for CO")
    plt.ylabel("Walking Speed")
    plt.xlabel("Weight")
    x = weight[group == 0]
    y = speed[group == 0]
    x = x[:, np.newaxis]
    y = y[:, np.newaxis]
    model = LinearRegression()                                                  #Plots line of best fit
    model.fit(x, y)
    y_pred = model.predict(x)
    plt.plot(x, y_pred, color = 'r')
    plt.show()

def relationshipbetweenspeedandweightforPD(speed,weight,group):                 #Plots speed vs weight for Parkinson's Disease Group
    plt.figure()
    plt.plot(weight[group == 1], speed[group == 1], 'y.')
    plt.title("Weight vs Speed for PD")
    plt.ylabel("Walking Speed")
    plt.xlabel("Weight")
    x = weight[group == 1]
    y = speed[group == 1]
    x = x[:, np.newaxis]
    y = y[:, np.newaxis]
    model = LinearRegression()                                                  #Plots line of best fit
    model.fit(x, y)
    y_pred = model.predict(x)
    plt.plot(x, y_pred, color = 'r')
    plt.show()

def Parkinsons_speed_vs_Control_speed(speed):                                   #Plots Control group speed vs Parkinson's Disease group
    plt.figure()
    plt.plot(speed[group == 1], 'y.', label= 'PD')
    plt.plot(speed[group == 0], 'r.', label= 'CO')
    plt.xlabel("Walking Speed")
    plt.ylabel("Count")
    plt.legend()
    plt.title("Walking Speed of Control Group vs Parkinson's Disease Group")
    plt.show()

def ANOVA(speed,group):
    Fvalue, pvalue1 = stats.f_oneway(speed[group == 1],speed[group == 0])       #Runs an ANOVA and generates an Fvalue and p-value
    return Fvalue, pvalue1

def ttest(speed,group):
     t_statistic, pvalue2 = stats.ttest_ind(speed[group ==1], speed[group == 0]) #tests the null hypothesis for equal means for both groups and returns a t-statistic and p-value
     return t_statistic, pvalue2

def graphing_3D(speed,height,age,group):                                        #3-D interactive plot in iPython that has 3 axes: speed, weight, age for both groups
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.scatter(speed[group == 1], height[group == 1], age[group == 1],c ='r', marker = 'o', label = "PD")
    ax.scatter(speed[group == 0], height[group == 0], age[group == 0],c = 'y', marker = 'o', label = "CO")
    plt.xlabel("Speed")
    plt.ylabel("Height")
    ax.set_zlabel("Age")
    plt.legend()
    plt.show()

def histogramforPD(speed,group):                                                #generates Histogram for Parkinson's Disease group
    plt.figure()
    plt.hist(speed[group == 1],rwidth = 0.95)
    plt.title("Speed vs Count for Parkinson's Disease")
    plt.xlabel("Walking Speed")
    plt.ylabel("Count") 
    plt.show()

def histogramforControl(speed,group):                                           #generates Histogram for Control Group
    plt.figure()
    plt.hist(speed[group == 0], rwidth = 0.95)
    plt.title("Speed vs Count for Control Group")
    plt.xlabel("Walking Speed")
    plt.ylabel("Count") 
    plt.show()

def normaldistributionforPD(speed,group):
    plt.figure()
    plt.hist(speed[group == 1], normed = True)                                  #plot histogram for Parkinson's group
    xt = plt.xticks()[0]
    xmin, xmax = min(xt), max(xt)
    lnspc = np.linspace(xmin, xmax, len(speed[group == 1]))
    mean, std = stats.norm.fit(speed[group == 1])                               #fit normal distribution curve over histogram
    pdf_g = stats.norm.pdf(lnspc, mean, std)                                    #get theoretical values in the interval  
    plt.plot(lnspc, pdf_g, label="Norm") 
    plt.title("Normal distribution for Parkinson's Disease")
    
def normaldistributionforCO(speed,group):                                       
    plt.figure()
    plt.hist(speed[group == 0], normed = True)                                  #plot histogram for Control group
    xt = plt.xticks()[0]
    xmin, xmax = min(xt), max(xt)
    lnspc = np.linspace(xmin, xmax, len(speed[group == 0]))
    mean, std = stats.norm.fit(speed[group == 0])                               #fit normal distribution curve over histogram
    pdf_g = stats.norm.pdf(lnspc, mean, std)                                    #get theoretical values in the interval  
    plt.plot(lnspc, pdf_g, label="Norm") 
    plt.title("Normal Distribution for Control Group")
    


def select(K):
    centroids = np.random.random((K,3))                                         #generate random centroid with size(K,3)
    return centroids

def assign(centroids,height,speed,age):
    K = centroids.shape[0] 
    distances = np.zeros((K,len(height)))
    for i in range(K):
        s = centroids[i,1]                                                      #to get speed data from centroid                                    
        h = centroids[i,0]                                                      #to get height data from centroid
        a = centroids[i,2]                                                      #to get age data from centroid
        distances[i] = np.sqrt((height - h)**2 + (speed - s)**2 + (age - a)**2) #find distance between speed,height and age data of centroid and the data points from the parsed in file.
    assignments = np.argmin(distances, axis = 0)                                ##generates an array of the indices of the minimum element in the array
    return assignments


def Update(group,height,speed,centroids):
    K = centroids.shape[0]
    new_centroids = np.zeros((K,3))                                             #generates an empty centroid of size (K,3) made up of zeros.
    for i in range(K):
        if not len(height[group == i]) == 0  or len(speed[group == i ]) == 0:   #the function loops through this if condition if the length of speed is not 0  for a specific centroid and if the length of height is not 0 for a specific centroid.
            new_centroids[i,1] = np.mean(speed[group == i]) 
            new_centroids[i,0] = np.mean(height[group == i])
            new_centroids[i,2] = np.mean(age[group == i])
        else:
            new_centroids[i,1] == 0                                             #moves it far away to 100
            new_centroids[i,0] == 0                                             #moves it far away to 100
            new_centroids[i,2] == 0                                             #moves it far away to 100
    return new_centroids
        
    
def Iterate(group,height,speed,centroids, new_centroids):
    x = 0                                                                       #initializing
    while x < 400:                                                              #for a maximum number of 400 iterations loop through the assign and update functions.
            assignments = assign(centroids,height,speed,age)
            new_centroids = Update(group,height,speed,centroids)
            x += 1
    return new_centroids,assignments
        


def graphingKMeans(speed,height,assignments,group, new_centroids):
    fig = plt.figure()
    ax = Axes3D(fig)
    for i in range(assignments.max()+1):
        rcolor = np.random.rand(3,)
        ax.scatter(speed[group==i],height[group==i], age[group == i], ".", label = "Class " + str(i), color = rcolor)
        ax.scatter(new_centroids[i, 0], new_centroids[i, 1], new_centroids[i,2], "D", label = "Centroid " + str(i), color = rcolor)
    plt.xlabel("Height")
    plt.ylabel("Speed")
    ax.set_zlabel("Age")
    plt.legend()
    plt.show()


def Venn_diagrams(speed,group):                                                 #Generate Venn Diagram comparing Control Group Speed to Parkinson's Disease Group Speed
    plt.figure()
    plt.title("Speed Venn Diagram")
    venn2([set(speed[group == 0]),set(speed[group ==1])], set_labels = ("Control", "PD"))


def Statsmodelssummary():                                                       #Generates table with statistical values such as the AIC, BIC, F-value, Log-likelihood
    my_data = pd.read_csv('Parkinsonsdiseasedataonly.csv')
    results = smf.ols('speed ~ group + height + age + weight', data = my_data).fit()
    print(results.summary())
    
    
height,weight,age, group, speed = readdatafile()

#




