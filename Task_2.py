### For this assignment you'll be looking at 2017 data on immunizations from the CDC. Your datafile for this assignment is in assets/NISPUF17.csv.
### A data users guide for this, which you'll need to map the variables in the data to the questions being asked, is available at assets/NIS-PUF17-DUG.pdf.
### Note: you may have to go to your Jupyter tree (click on the Coursera image) and navigate to the assignment 2 assets folder to see this PDF file).

### Q1
### Write a function called proportion_of_education which returns the proportion of children in the dataset who had a mother with the education levels equal to less
### than high school (<12), high school (12), more than high school but not a college graduate (>12) and college degree.

### This function should return a dictionary in the form of (use the correct numbers, do not round numbers):
###    {"less than high school":0.2,
###    "high school":0.4,
###    "more than high school but not college":0.2,
###    "college":0.2}

import pandas as pd


def proportion_of_education():
    df = pd.read_csv('assets/NISPUF17.csv')
    les = len(df[df['EDUC1'] == 1]) / 28465
    hig = len(df[df['EDUC1'] == 2]) / 28465
    mor = len(df[df['EDUC1'] == 3]) / 28465
    col = len(df[df['EDUC1'] == 4]) / 28465
    return {"less than high school": les, "high school": hig, "more than high school but not college": mor,
            "college": col}


proportion_of_education()

### Q2
### Let's explore the relationship between being fed breastmilk as a child and getting a seasonal influenza vaccine from a healthcare provider.
### Return a tuple of the average number of influenza vaccines for those children we know received breastmilk as a child and those who know did not.

### This function should return a tuple in the form (use the correct numbers:
### (2.5, 0.1)

import pandas as pd


def average_influenza_doses():
    df = pd.read_csv('assets/NISPUF17.csv', index_col=0)
    Bm = df[(df['CBF_01'] == 1) & (df['P_NUMFLU'] >= 0)]
    Dm = df[(df['CBF_01'] == 2) & (df['P_NUMFLU'] >= 0)]
    res_1 = (sum(Bm['P_NUMFLU'])) / len(Bm)
    res_2 = (sum(Dm['P_NUMFLU'])) / len(Dm)
    return (res_1, res_2)


average_influenza_doses()

### Q3
### It would be interesting to see if there is any evidence of a link between vaccine effectiveness and sex of the child.
### Calculate the ratio of the number of children who contracted chickenpox but were vaccinated against it (at least one varicella dose) versus
### those who were vaccinated but did not contract chicken pox. Return results by sex.
### This function should return a dictionary in the form of (use the correct numbers):
### {"male":0.2,
### "female":0.4}

import pandas as pd


def chickenpox_by_sex():
    df = pd.read_csv('assets/NISPUF17.csv', index_col=0)
    vac_male = df[(df['P_NUMVRC'] >= 1) & (df['HAD_CPOX'] == 2) & (df['SEX'] == 1)]
    vac_female = df[(df['P_NUMVRC'] >= 1) & (df['HAD_CPOX'] == 2) & (df['SEX'] == 2)]
    male = df[(df['HAD_CPOX'] == 1) & (df['SEX'] == 1) & (df['P_NUMVRC'] >= 1)]
    female = df[(df['HAD_CPOX'] == 1) & (df['SEX'] == 2) & (df['P_NUMVRC'] >= 1)]
    res_male = len(male) / len(vac_male)
    res_female = len(female) / len(vac_female)
    return {"male": res_male, "female": res_female}


chickenpox_by_sex()


### Q4
### A correlation is a statistical relationship between two variables. If we wanted to know if vaccines work, we might look at the correlation between
### the use of the vaccine and whether it results in prevention of the infection or disease [1].
### In this question, you are to see if there is a correlation between having had the chicken pox and the number of chickenpox vaccine doses given (varicella).
### Some notes on interpreting the answer. The had_chickenpox_column is either 1 (for yes) or 2 (for no), and the num_chickenpox_vaccine_column is the number of doses
### a child has been given of the varicella vaccine. A positive correlation (e.g., corr > 0) means that an increase in had_chickenpox_column (which means more no’s)
### would also increase the values of num_chickenpox_vaccine_column (which means more doses of vaccine). If there is a negative correlation (e.g., corr < 0), it indicates
### that having had chickenpox is related to an increase in the number of vaccine doses.
### Also, pval is the probability that we observe a correlation between had_chickenpox_column and num_chickenpox_vaccine_column which is greater than or equal to a particular value occurred by chance. A small pval means that the observed correlation is highly unlikely to occur by chance. In this case, pval should be very small (will end in e-18 indicating a very small number).

def corr_chickenpox():
    import scipy.stats as stats
    import numpy as np
    import pandas as pd

    # this is just an example dataframe
    df = pd.read_csv('assets/NISPUF17.csv', index_col=0)
    res = df[['P_NUMVRC', 'HAD_CPOX']]
    res = res[(res['HAD_CPOX'] == 1) | (res['HAD_CPOX'] == 2)]
    res.dropna(inplace=True)

    corr, pval = stats.pearsonr(res['HAD_CPOX'], res['P_NUMVRC'])
    return corr


corr_chickenpox()