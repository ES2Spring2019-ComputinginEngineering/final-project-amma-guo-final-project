# Analyzing the Relationship between Parkinson's Disease and Walking Speed by Amma Agyei and Tina Guo



You should include in your final project readme a description of the project, a list of all the files that you have created and instructions for use.

This readme is written in a language called markdown. This is not a programming language but a formatting langauge. There are symbols (syntax) used to indicate how to format the text. For example the pound symbol (i.e. the hashtag) is used to format a title; two of the same symbol format a heading, and three format a sub-heading.

Below is some example text in markdown however this alone is not suffiecent for the final project. **Make sure you follow the directions on Canvas.**

Delete the instructions above this line and the line:

---------------------------------------------

# Analyzing the Relationship between Parkinson's Disease and Walking Speed 

Parkinson’s Disease patients take shorter steps when they walk and have stiff muscles and have a decrease in their ability to blink, smile and perform other unconscious movements. Fitbits do not take into account whether a person has a disease which may hinder their ability to perform normal physical movements. The goal of our project was to analyze Parkinson’s Disease Data as well as other neurodegenerative disease to determine if there is a relationship between human characteristics such as age, weight, height, and gait speed and whether a person has Parkinson’s Disease or not.


## Instructions

** In order to run the script, certain modules have to download using the terminal on the user's computer, type *pip install matplotlib_venn* into your computer terminal. ** 
- Download `Parkinsonsdiseaseonly.csv`, `functions.py` and `main.py` , making sure that they are all in the same folder.
- Open Spyder Anaconda and open `functions.py` and `main.py`.
- First run `functions.py`.
- Run `main.py`
             - In order to view the 3-D interactive plot and other figures, it is **necessary** that the console be closed and reopened after running the script to open iPython.

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

`main.py` contains the script. It is the driver and will run the code. 

`Parkinsondiseasedataonly.csv` is the csv file containing the data that is being analyzed in the project. Data from this file will be parsed in and organized into arrays.


## How to format your readme

In your readme, you can:
```
Give code examples
```

You can also include useful links, like this one with information about [formatting markdown](https://help.github.com/en/articles/basic-writing-and-formatting-syntax)

You can 
- Also
- Make
- Lists
