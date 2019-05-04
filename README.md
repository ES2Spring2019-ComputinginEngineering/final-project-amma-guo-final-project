# Analyzing the Relationship between Parkinson's Disease and Walking Speed 
## By: Amma Agyei and Tina Guo

Parkinson’s Disease patients take shorter steps when they walk and have stiff muscles and have a decrease in their ability to blink, smile and perform other unconscious movements. Fitbits do not take into account whether a person has a disease which may hinder their ability to perform normal physical movements. The goal of our project was to analyze Parkinson’s Disease Data as well as other neurodegenerative disease to determine if there is a relationship between human characteristics such as age, weight, height, and gait speed and whether a person has Parkinson’s Disease or not.


## Instructions

**In order to run the script, certain modules have to be downloaded using the terminal on the user's computer, type *pip install matplotlib_venn* into your computer terminal.** 
- After downloading this module, download `Parkinsonsdiseaseonly.csv`, `functions.py` and `main.py` , making sure that they are all in the same folder.
- Open Spyder Anaconda and open `functions.py` and `main.py`.
- First run `functions.py`.
- Run `main.py`
             - In order to view the 3-D interactive plot and other figures, it is **necessary that the console be closed and reopened after running the script to open iPython.**

## File List
`functions.py` contains all the functions for running our project. Functions include: 
readdatafile, relationshipbetweenspeedandheightforCO, relationshipbetweenspeedandheightforPD, relationshipbetweenspeedandageforPD, relationshipbetweenspeedandageforCO, relationshipbetweenspeedandweightforCO, relationshipbetweenspeedandweightforPD, Parkinsons_speed_vs_Control_speed, ANOVA, ttest, graphing_3D, histogramforPD, histogramforControl, normaldistributionforPD, normaldistributionforCO, select, assign, Update, Iterate, graphingKMeans, Venn_diagrams, Statsmodelssummary.

`main.py` contains the script. It is the driver and must be run to generate the figures and graphs. 

`Parkinsondiseasedataonly.csv` is the csv file containing the data that is being analyzed in the project. Data from this file will be parsed in and organized into arrays.

## Description of Functions
- `readdatafile()` takes in the data set from the csv file and organizes it into the arrays: speed, height, age, group and weight. This function also normalizes the data since speed, height, weight and age have different scales. The function returns height, speed, weight, age and group. 

- `relationshipbetweenspeedandheightforCO`, `relationshipbetweenspeedandheightforPD`, `relationshipbetweenspeedandageforPD`,  - `relationshipbetweenspeedandageforCO`, `relationshipbetweenspeedandweightforCO`,and `relationshipbetweenspeedandweightforPD` generate plots analyzing the relationship between walking speed and the human characteristics age, height, and weight for both the control group and the Parkinson's Disease group.

- `Parkinsons_speed_vs_Control_speed` plots the walking speed for individuals in the control group and Parkinson's group in different colors so they can be compared visually.

- `ANOVA` and `ttest` are functions that perform statistical tests to determine if there is a significant difference between the control group and the Parkinson's disease group by giving a p-value. If the p-value is less than 0.05, then the groups are significantly different.

- `graphing 3-D` generates a 3-D interactive plot of the data points on 3 axes: height, age and speed.
- `histogramforPD `, `histogramforControl`, `normaldistributionforPD` and `normaldistributionforCO` generates a plot of the histograms for both groups and fits a normal distribution curve over the histograms to determine if the data is normally distributed.

- The clustering algorithm consists of the `select`, `assign`, `update`, and `iterate` functions. A random (K,3) centroid is created, new classifications are assigned to the various centroids based on the three features(height, speed, age)taken in,and the locations of the centroids are updated by finding the mean of all the height points, speed points and age points assigned to a specific centroid. After iterating through the assign and update functions for a maximum number of iterations, the locations of the centroids are updated.

- `graphing KMeans` plots the height, speed and weight points in random colors based on which centroids they are assigned to.

-`Venn_diagrams` generates venn diagrams analyzing the speed of the control group and Parkinson's disease group.
- `Statsmodelssummary` generates a table containing useful statistics such as F-value, Log-likelihood, AIC, BIC, and so on.

