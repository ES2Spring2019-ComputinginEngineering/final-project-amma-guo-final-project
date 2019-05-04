# This files should not contain any function defitions
#By: Amma Agyei and Tina Guo

# IMPORT STATEMENTS
from functions import readdatafile,relationshipbetweenspeedandheightforCO, relationshipbetweenspeedandheightforPD, relationshipbetweenspeedandageforPD, relationshipbetweenspeedandageforCO, relationshipbetweenspeedandweightforCO,relationshipbetweenspeedandweightforPD, Parkinsons_speed_vs_Control_speed, ANOVA, ttest, graphing_3D, histogramforPD,histogramforControl,normaldistributionforPD, normaldistributionforCO, select, assign, Update, Iterate, graphingKMeans, Venn_diagrams, Statsmodelssummary
import matplotlib.pyplot as plt
plt.rcParams.update({'figure.max_open_warning': 0})     #gets rid of runtime warning preventing my code from plotting more than 20 figures


# DEMONSTRATION CODE
height,weight,age, group, speed = readdatafile()                                #parses in data and organizes it into arrays
Parkinsons_speed_vs_Control_speed(speed)                                        #graph Parkinson's disease speed vs Control Group speed
relationshipbetweenspeedandageforCO(speed,age,group)                            #Graph Speed vs Age for Control
relationshipbetweenspeedandageforPD(speed,age,group)                            #Graph Speed vs Age for Parkinson's Disease
relationshipbetweenspeedandweightforCO(speed,weight,group)                      #Graph Speed vs Weight for Control
relationshipbetweenspeedandweightforPD(speed,weight,group)                      #Graph Speed vs Weight for Parkinson's Disease
relationshipbetweenspeedandheightforCO(speed,group,height)                      #Graph Speed vs Height for Control
relationshipbetweenspeedandheightforPD(speed,group,height)                      #Graph Speed vs Height for Parkinson's Disease
graphing_3D(speed,height,age,group)                                             #Generate 3-D interactive plot
Fvalue, pvalue1 = ANOVA(speed,group)                                            #Give the p-value and Fvalue from ANOVA test
histogramforPD(speed,group)                                                     #Plot histogram for Parkinson's Disease Group
histogramforControl(speed,group)                                                #Plot histogram for Control Group
normaldistributionforPD(speed,group)                                            #Graph normal distribution for Parkinson's Disease group
normaldistributionforCO(speed,group)                                            #Graph normal distribution for Control group
t_statistic, pvalue2 = ttest(speed,group)                                       #Generate t-statistic and pvalue from ttest  
centroids = select(2)                                                           #Generate two random centroids
assignments = assign(centroids,height,speed,age)                                #assign new assignments to data points
new_centroids = Update(group,height,speed,centroids)                            #update location of centroids
new_centroids,assignments  = Iterate(group,height,speed,centroids,new_centroids)          #iterate through a maximum number and update new location of centroids
graphingKMeans(speed,height,assignments,group,centroids)                                    #graph clusters on 3-D graph
Venn_diagrams(speed,group)                                                      #Generate Venn Diagrams
Statsmodelssummary()                                                            #Generate summary of results from Statsmodels



