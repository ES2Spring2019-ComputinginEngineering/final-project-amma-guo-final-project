# Analyzing the Relationship between Parkinson's Disease and Walking Speed 
## By: Amma Agyei and Tina Guo

Parkinson’s Disease patients take shorter steps when they walk and have stiff muscles and have a decrease in their ability to blink, smile and perform other unconscious movements. Fitbits do not take into account whether a person has a disease which may hinder their ability to perform normal physical movements. The goal of our project was to analyze Parkinson’s Disease Data as well as other neurodegenerative disease to determine if there is a relationship between human characteristics such as age, weight, height, and gait speed and whether a person has Parkinson’s Disease or not.


## Instructions

**In order to run the script, certain modules have to download using the terminal on the user's computer, type *pip install matplotlib_venn* into your computer terminal.** 
- Download `Parkinsonsdiseaseonly.csv`, `functions.py` and `main.py` , making sure that they are all in the same folder.
- Open Spyder Anaconda and open `functions.py` and `main.py`.
- First run `functions.py`.
- Run `main.py`
             - In order to view the 3-D interactive plot and other figures, it is **necessary that the console be closed and reopened after running the script to open iPython.**

## File List
`functions.py` contains all the functions for running our project. Functions include: 
1. readdatafile
2. relationshipbetweenspeedandheightforCO    
3. relationshipbetweenspeedandheightforPD
4. relationshipbetweenspeedandageforPD
5. relationshipbetweenspeedandageforCO
6. relationshipbetweenspeedandweightforCO
7. relationshipbetweenspeedandweightforPD 
8. Parkinsons_speed_vs_Control_speed
9. ANOVA
10. ttest
11. graphing_3D
12. histogramforPD
13. histogramforControl
14. normaldistributionforPD
15. normaldistributionforCO
16. select
17. assign
18. Update
19. Iterate
19. graphingKMeans
20. Venn_diagrams
21. Statsmodelssummary.

`main.py` contains the script. It is the driver and must be run to generate the figures and graphs. 

`Parkinsondiseasedataonly.csv` is the csv file containing the data that is being analyzed in the project. Data from this file will be parsed in and organized into arrays.

You can also include useful links, like this one with information about [formatting markdown](https://help.github.com/en/articles/basic-writing-and-formatting-syntax)

You can 
- Also
- Make
- Lists
