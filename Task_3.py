### Q1
### Load the energy data from the file assets/Energy Indicators.xls, which is a list of indicators of energy supply and renewable electricity
### production from the United Nations for the year 2013, and should be put into a DataFrame with the variable name of Energy.
### Keep in mind that this is an Excel file, and not a comma separated values file. Also, make sure to exclude the footer and header
### information from the datafile. The first two columns are unneccessary, so you should get rid of them, and you should change the column labels so that the columns are:
### ['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable]
### Convert Energy Supply to gigajoules (Note: there are 1,000,000 gigajoules in a petajoule). For all countries which have missing data (e.g. data with "...") make
### sure this is reflected as np.NaN values.
### Rename the following list of countries (for use in later questions):
### "Republic of Korea": "South Korea",
### "United States of America": "United States",
### "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
### "China, Hong Kong Special Administrative Region": "Hong Kong"
### There are also several countries with numbers and/or parenthesis in their name. Be sure to remove these, e.g. 'Bolivia (Plurinational State of)' should be
### 'Bolivia'. 'Switzerland17' should be 'Switzerland'.
### Next, load the GDP data from the file assets/world_bank.csv, which is a csv containing countries' GDP from 1960 to 2015 from World Bank. Call this DataFrame GDP.
### Make sure to skip the header, and rename the following list of countries:
### "Korea, Rep.": "South Korea",
### "Iran, Islamic Rep.": "Iran",
### "Hong Kong SAR, China": "Hong Kong"
### Finally, load the Sciamgo Journal and Country Rank data for Energy Engineering and Power Technology from the file assets/scimagojr-3.xlsx, which ranks
### countries based on their journal contributions in the aforementioned area. Call this DataFrame ScimEn.
### Join the three datasets: GDP, Energy, and ScimEn into a new dataset (using the intersection of country names).
### Use only the last 10 years (2006-2015) of GDP data and only the top 15 countries by Scimagojr 'Rank' (Rank 1 through 15).
### The index of this DataFrame should be the name of the country, and the columns should be
### ['Rank', 'Documents', 'Citable documents', 'Citations', 'Self-citations', 'Citations per document', 'H index', 'Energy Supply', 'Energy Supply per Capita', '% Renewable', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015'].

def answer_one():
    import numpy as np
    import pandas as pd

    df = pd.read_excel('assets/Energy Indicators.xls', index_col=2)
    df.drop(df.columns[[0]], axis=1, inplace=True)
    df = df.dropna()
    df.columns = ['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable']
    df.index = ['' for _ in range(len(df))]
    df.loc[(df['Energy Supply'] != '...'), 'Energy Supply'] *= 1000000
    df.loc[(df['Energy Supply'] == '...'), 'Energy Supply'] = np.NaN
    df.loc[(df['Country'] == 'Republic of Korea'), 'Country'] = 'South Korea'
    df.loc[(df['Country'] == 'United States of America'), 'Country'] = 'United States'
    df.loc[(df['Country'] == 'United Kingdom of Great Britain and Northern Ireland'), 'Country'] = 'United Kingdom'
    df.loc[(df['Country'] == 'China, Hong Kong Special Administrative Region'), 'Country'] = 'Hong Kong'
    df_1 = df['Country'].str.replace(r' \(.*\)', '')
    df['Country'] = df_1

    ###########################

    vvp = pd.read_csv('assets/world_bank.csv', skiprows=4)
    vvp['Country Name'] = vvp['Country Name'].replace(
        {'Korea, Rep.': 'South Korea', 'Iran, Islamic Rep.': 'Iran', 'Hong Kong SAR, China': 'Hong Kong'})
    vvp = vvp[['Country Name', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']]
    vvp = vvp.rename(columns={'Country Name': 'Country'})

    ###########################

    Scim = pd.read_excel('assets/scimagojr-3.xlsx')

    ###########################

    res = pd.merge(Scim, df, how='inner', left_on='Country', right_on='Country')
    res_al = pd.merge(res, vvp, how='inner', left_on='Country', right_on='Country')
    res_al = res_al.set_index('Country')
    return res_al[:15]


answer_one()


### Q2
### The previous question joined three datasets then reduced this to just the top 15 entries. When you joined the datasets, but before you reduced
### this to the top 15 items, how many entries did you lose?

def answer_two():
    import numpy as np
    import pandas as pd
    # YOUR CODE HERE
    # raise NotImplementedError()
    df = pd.read_excel('assets/Energy Indicators.xls', index_col=2)
    df.drop(df.columns[[0]], axis=1, inplace=True)
    df = df.dropna()
    df.columns = ['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable']
    df.index = ['' for _ in range(len(df))]
    df.loc[(df['Energy Supply'] != '...'), 'Energy Supply'] *= 1000000
    df.loc[(df['Energy Supply'] == '...'), 'Energy Supply'] = np.NaN
    df.loc[(df['Country'] == 'Republic of Korea'), 'Country'] = 'South Korea'
    df.loc[(df['Country'] == 'United States of America'), 'Country'] = 'United States'
    df.loc[(df['Country'] == 'United Kingdom of Great Britain and Northern Ireland'), 'Country'] = 'United Kingdom'
    df.loc[(df['Country'] == 'China, Hong Kong Special Administrative Region'), 'Country'] = 'Hong Kong'
    df_1 = df['Country'].str.replace(r' \(.*\)', '')
    df['Country'] = df_1

    ###########################

    vvp = pd.read_csv('assets/world_bank.csv', skiprows=4)
    vvp['Country Name'] = vvp['Country Name'].replace(
        {'Korea, Rep.': 'South Korea', 'Iran, Islamic Rep.': 'Iran', 'Hong Kong SAR, China': 'Hong Kong'})
    vvp = vvp[['Country Name', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']]
    vvp = vvp.rename(columns={'Country Name': 'Country'})

    ###########################

    Scim = pd.read_excel('assets/scimagojr-3.xlsx')

    ###########################

    res = pd.merge(Scim, df, how='inner', left_on='Country', right_on='Country')
    res_al = pd.merge(res, vvp, how='inner', left_on='Country', right_on='Country')
    res_al = res_al.set_index('Country')
    answer_one = len(res_al)
    res = pd.merge(Scim, df, how='outer', left_on='Country', right_on='Country')
    res_al = pd.merge(res, vvp, how='outer', left_on='Country', right_on='Country')
    res_al = res_al.set_index('Country')
    answer_two = len(res_al) - answer_one
    return answer_two


answer_two()

### Q3
### What are the top 15 countries for average GDP over the last 10 years?

import pandas as pd


def answer_three():
    import numpy as np
    vvp = answer_one()
    vvp = vvp[['2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']]
    vvp = vvp.mean(axis=1).rename('aveGDP')
    vvp = vvp.sort_values(ascending=False)
    return vvp


answer_three()

### Q4
### By how much had the GDP changed over the 10 year span for the country with the 6th largest average GDP?

import pandas as pd
import numpy as np


def answer_four():
    vvp = answer_one()
    vvp = vvp[['2006', '2015']]
    vvp = vvp.diff(axis=1)
    vvp = vvp.loc['United Kingdom']['2015']
    return vvp


answer_four()

### Q5
### What is the mean energy supply per capita?

import pandas as pd
import numpy as np


def answer_five():
    vvp = answer_one()
    vvp = vvp['Energy Supply per Capita'].mean(axis=0)
    return vvp


answer_five()

### Q6
### What country has the maximum % Renewable and what is the percentage?

import pandas as pd
import numpy as np


def answer_six():
    vvp = answer_one()
    digit = vvp['% Renewable'].max(axis=0)
    Country = vvp.loc[vvp['% Renewable'] == digit].index[0]
    res = (Country, digit)
    return res


answer_six()

### Q7
### Create a new column that is the ratio of Self-Citations to Total Citations. What is the maximum value for this new column, and what country has the highest ratio?

import pandas as pd
import numpy as np


def answer_seven():
    vvp = answer_one()
    vvp['Ratio'] = vvp['Self-citations'] / vvp['Citations']
    rat = vvp['Ratio'].max(axis=0)
    Country = vvp.loc[vvp['Ratio'] == rat].index[0]
    res = (Country, rat)
    return res


answer_seven()

### Q8
### Create a column that estimates the population using Energy Supply and Energy Supply per capita. What is the third most populous country according to this estimate?

import pandas as pd
import numpy as np


def answer_eight():
    vvp = answer_one()
    vvp['Citizens'] = vvp['Energy Supply'] / vvp['Energy Supply per Capita']
    res = vvp.Citizens.sort_values(ascending=False)
    return res.index[2]


answer_eight()

### Q9
### Create a column that estimates the number of citable documents per person.
### What is the correlation between the number of citable documents per capita and the energy supply per capita? Use the .corr() method, (Pearson's correlation).

import pandas as pd
import numpy as np


def answer_nine():
    Top15 = answer_one()
    Top15['PopEstimate'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    Top15['Citable docs per Capita'] = Top15['Citable documents'] / Top15['PopEstimate']
    Top15['Citable docs per Capita'] = pd.to_numeric(Top15['Citable docs per Capita'])
    Top15['Energy Supply per Capita'] = pd.to_numeric(Top15['Energy Supply per Capita'])
    correlation = Top15['Citable docs per Capita'].corr(Top15['Energy Supply per Capita'])
    return correlation


answer_nine()

### Q10
### Create a new column with a 1 if the country's % Renewable value is at or above the median for all countries in the
### top 15, and a 0 if the country's % Renewable value is below the median.

import pandas as pd
import numpy as np


def answer_ten():
    vvp = answer_one()
    val = vvp['% Renewable'].median()
    vvp['HighRenew'] = [1 if x >= val else 0 for x in vvp['% Renewable']]
    return vvp['HighRenew']


answer_ten()

### Q11
### Use the following dictionary to group the Countries by Continent, then create a DataFrame that displays the sample
### size (the number of countries in each continent bin), and the sum, mean, and std deviation for the estimated population of each country.
### ContinentDict  = {'China':'Asia',
###                  'United States':'North America',
###                  'Japan':'Asia',
###                  'United Kingdom':'Europe',
###                  'Russian Federation':'Europe',
###                  'Canada':'North America',
###                  'Germany':'Europe',
###                  'India':'Asia',
###                  'France':'Europe',
###                  'South Korea':'Asia',
###                  'Italy':'Europe',
###                  'Spain':'Europe',
###                  'Iran':'Asia',
###                  'Australia':'Australia',
###                  'Brazil':'South America'}

import pandas as pd
import numpy as np


def answer_eleven():
    df = answer_one()
    ContinentDict = {'China': 'Asia',
                     'United States': 'North America',
                     'Japan': 'Asia',
                     'United Kingdom': 'Europe',
                     'Russian Federation': 'Europe',
                     'Canada': 'North America',
                     'Germany': 'Europe',
                     'India': 'Asia',
                     'France': 'Europe',
                     'South Korea': 'Asia',
                     'Italy': 'Europe',
                     'Spain': 'Europe',
                     'Iran': 'Asia',
                     'Australia': 'Australia',
                     'Brazil': 'South America'}

    df['Population'] = df['Energy Supply'] / df['Energy Supply per Capita']
    df = df.reset_index()
    df['Continent'] = [ContinentDict[country] for country in df['Country']]
    df.set_index('Continent', inplace=True)
    df['Population'] = pd.to_numeric(df['Population'])
    ans = df.groupby(level=0)['Population'].agg({'size': np.size, 'sum': np.sum, 'mean': np.mean, 'std': np.std})
    return ans


answer_eleven()
