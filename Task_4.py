### Q1
### For this question, calculate the win/loss ratio's correlation with the population of the city it is in for the NHL using 2018 data.

import pandas as pd
import numpy as np
import scipy.stats as stats
import re


def nhl_correlation():
    nhl_df = pd.read_csv("assets/nhl.csv", index_col=0)
    cities = pd.read_html("assets/wikipedia_data.html")[1]
    cities = cities.iloc[:-1, [0, 3, 5, 6, 7, 8]]

    cities.rename(columns={'Metropolitan area': 'metro'}, inplace=True)
    cities = cities.rename(columns={'Population (2016 est.)[8]': 'Population'})
    cities['NHL'] = cities['NHL'].str.replace(r"\[.*\]", "")
    cities['NHL'] = cities['NHL'].str.replace(r"[^\w ]", "")
    cities = cities[cities['NHL'] != '']
    cities = cities[['metro', 'Population']]

    nhl_df = nhl_df[nhl_df['year'] == 2018]
    nhl_df = nhl_df.drop(['Atlantic Division', 'Metropolitan Division', 'Central Division', 'Pacific Division'], axis=0)
    nhl_df = nhl_df.reset_index()
    nhl_df['team'] = nhl_df['team'].str.replace(r"[^\w ]", "")
    nhl_df['W'] = pd.to_numeric(nhl_df['W'])
    nhl_df['L'] = pd.to_numeric(nhl_df['L'])
    nhl_df['W/L ratio'] = nhl_df['W'] / (nhl_df['W'] + nhl_df['L'])

    metrolist = cities.metro.unique().tolist()
    nhl_df['metro'] = nhl_df['team'].apply(lambda x: ''.join([city for city in metrolist if city in x]))
    nhl_df = nhl_df.sort_values(by=['team'])
    nhl_df['metro'].replace(r'^\s*$', np.nan, regex=True, inplace=True)
    citydict = {0: 'Tampa Bay Area', 3: 'Miami–Fort Lauderdale', 8: 'Washington, D.C.', 12: 'New York City',
                13: 'Raleigh', 14: 'New York City', 15: 'New York City', 18: 'Minneapolis–Saint Paul', 19: 'Denver',
                20: 'St. Louis', 21: 'Dallas–Fort Worth', 23: 'Las Vegas', 24: 'Los Angeles',
                25: 'San Francisco Bay Area', 30: 'Phoenix'}
    nhl_df['metro'].fillna(citydict, inplace=True)
    nhl_df = nhl_df.reset_index()
    nhl_df = nhl_df[['team', 'year', 'W/L ratio', 'metro']]
    nhl_df['avgWL'] = nhl_df.groupby('metro')['W/L ratio'].transform('mean')

    res = pd.merge(nhl_df, cities, how='inner', left_on='metro', right_on='metro')
    res = res[['metro', 'avgWL', 'Population']]
    res = res.drop_duplicates(subset=['metro'])
    res = res.sort_values(by=['metro'])
    res = res.set_index('metro', drop=True)
    res['Population'] = pd.to_numeric(res['Population'])

    population_by_region = res['Population']
    win_loss_by_region = res['avgWL']

    assert len(population_by_region) == len(win_loss_by_region), "Q1: Your lists must be the same length"
    assert len(population_by_region) == 28, "Q1: There should be 28 teams being analysed for NHL"

    return stats.pearsonr(population_by_region, win_loss_by_region)[0]


nhl_correlation()

### Q2
### For this question, calculate the win/loss ratio's correlation with the population of the city it is in for the NBA using 2018 data.

import pandas as pd
import numpy as np
import scipy.stats as stats
import re


def nba_correlation():
    nba_df = pd.read_csv("assets/nba.csv")
    cities = pd.read_html("assets/wikipedia_data.html")[1]
    cities = cities.iloc[:-1, [0, 3, 5, 6, 7, 8]]

    cities.rename(columns={'Metropolitan area': 'metro'}, inplace=True)
    cities = cities.rename(columns={'Population (2016 est.)[8]': 'Population'})
    cities['NBA'] = cities['NBA'].str.replace(r"\[.*\]", "")
    cities['NBA'] = cities['NBA'].str.replace(r"[^\w ]", "")
    cities = cities[cities['NBA'] != '']
    cities = cities[['metro', 'Population', 'NBA']]

    nba_df = nba_df[nba_df['year'] == 2018]
    nba_df['team'] = nba_df['team'].str.replace(r"\S\s\(.*\)", "")
    nba_df['W'] = pd.to_numeric(nba_df['W'])
    nba_df['L'] = pd.to_numeric(nba_df['L'])
    nba_df['W/L ratio'] = nba_df['W'] / (nba_df['W'] + nba_df['L'])

    metrolist = cities.metro.unique().tolist()
    nba_df['metro'] = nba_df['team'].apply(lambda x: ''.join([city for city in metrolist if city in x]))
    nba_df = nba_df.sort_values(by=['team'])
    nba_df = nba_df.reset_index()
    nba_df = nba_df[['team', 'year', 'W/L ratio', 'metro']]
    nba_df['metro'].replace(r'^\s*$', np.nan, regex=True, inplace=True)
    citydict = {2: 'New York City', 6: 'Dallas–Fort Worth', 9: 'San Francisco Bay Area', 11: 'Indianapolis',
                15: 'Miami–Fort Lauderdale', 17: 'Minneapolis–Saint Paul', 19: 'New York City', 28: 'Salt Lake City',
                29: 'Washington, D.C.'}
    nba_df['metro'].fillna(citydict, inplace=True)
    nba_df['avgWL'] = nba_df.groupby('metro')['W/L ratio'].transform('mean')

    res = pd.merge(nba_df, cities, how='inner', left_on='metro', right_on='metro')
    res = res[['metro', 'avgWL', 'Population']]
    res = res.drop_duplicates(subset=['metro'])
    res = res.sort_values(by=['metro'])
    res = res.set_index('metro', drop=True)
    res['Population'] = pd.to_numeric(res['Population'])

    population_by_region = res['Population']  # pass in metropolitan area population from cities
    win_loss_by_region = res[
        'avgWL']  # pass in win/loss ratio from nba_df in the same order as cities["Metropolitan area"]

    assert len(population_by_region) == len(win_loss_by_region), "Q2: Your lists must be the same length"
    assert len(population_by_region) == 28, "Q2: There should be 28 teams being analysed for NBA"

    return stats.pearsonr(population_by_region, win_loss_by_region)[0]


nba_correlation()

### Q3
### For this question, calculate the win/loss ratio's correlation with the population of the city it is in for the MLB using 2018 data.

import pandas as pd
import numpy as np
import scipy.stats as stats
import re


def mlb_correlation():
    mlb_df = pd.read_csv("assets/mlb.csv")
    cities = pd.read_html("assets/wikipedia_data.html")[1]
    cities = cities.iloc[:-1, [0, 3, 5, 6, 7, 8]]

    cities.rename(columns={'Metropolitan area': 'metro'}, inplace=True)
    cities = cities.rename(columns={'Population (2016 est.)[8]': 'Population'})
    cities['MLB'] = cities['MLB'].str.replace(r"\[.*\]", "")
    cities['MLB'] = cities['MLB'].str.replace(r"[^\w ]", "")
    cities = cities[['metro', 'Population', 'MLB']]

    mlb_df = mlb_df[mlb_df['year'] == 2018]
    mlb_df = mlb_df.rename(columns={'W-L%': 'W/L ratio'})

    metrolist = cities.metro.unique().tolist()
    mlb_df['metro'] = mlb_df['team'].apply(lambda x: ''.join([city for city in metrolist if city in x]))
    mlb_df = mlb_df[['team', 'year', 'W/L ratio', 'metro']]
    mlb_df['metro'].replace(r'^\s*$', np.nan, regex=True, inplace=True)
    citydict = {1: 'New York City', 2: 'Tampa Bay Area', 6: 'Minneapolis–Saint Paul', 11: 'San Francisco Bay Area',
                14: 'Dallas–Fort Worth', 16: 'Washington, D.C.', 18: 'New York City', 19: 'Miami–Fort Lauderdale',
                26: 'Denver', 27: 'Phoenix', 28: 'San Francisco Bay Area'}
    mlb_df['metro'].fillna(citydict, inplace=True)
    mlb_df['avgWL'] = mlb_df.groupby('metro')['W/L ratio'].transform('mean')

    res = pd.merge(mlb_df, cities, how='inner', left_on='metro', right_on='metro')
    res = res[['metro', 'avgWL', 'Population']]
    res = res.drop_duplicates(subset=['metro'])
    res = res.sort_values(by=['metro'])
    res = res.set_index('metro', drop=True)
    res['Population'] = pd.to_numeric(res['Population'])
    population_by_region = res['Population']  # pass in metropolitan area population from cities
    win_loss_by_region = res[
        'avgWL']  # pass in win/loss ratio from nba_df in the same order as cities["Metropolitan area"]

    assert len(population_by_region) == len(win_loss_by_region), "Q3: Your lists must be the same length"
    assert len(population_by_region) == 26, "Q3: There should be 26 teams being analysed for MLB"

    return stats.pearsonr(population_by_region, win_loss_by_region)[0]


mlb_correlation()

### Q4
### For this question, calculate the win/loss ratio's correlation with the population of the city it is in for the NFL using 2018 data.

import pandas as pd
import numpy as np
import scipy.stats as stats
import re


def nfl_correlation():
    nfl_df = pd.read_csv("assets/nfl.csv", index_col=0)
    cities = pd.read_html("assets/wikipedia_data.html")[1]
    cities = cities.iloc[:-1, [0, 3, 5, 6, 7, 8]]

    cities.rename(columns={'Metropolitan area': 'metro'}, inplace=True)
    cities = cities.rename(columns={'Population (2016 est.)[8]': 'Population'})
    cities['NFL'] = cities['NFL'].str.replace(r"\[.*\]", "")
    cities['NFL'] = cities['NFL'].str.replace(r"[^\w ]", "")
    cities = cities[['metro', 'Population', 'NFL']]

    nfl_df = nfl_df[nfl_df['year'] == 2018]
    nfl_df = nfl_df.drop(
        ['AFC East', 'AFC North', 'AFC South', 'AFC West', 'NFC East', 'NFC North', 'NFC South', 'NFC West'], axis=0)
    nfl_df = nfl_df.reset_index()
    nfl_df['team'] = nfl_df['team'].str.replace(r"[?*?+]", "")
    nfl_df['W'] = pd.to_numeric(nfl_df['W'])
    nfl_df['L'] = pd.to_numeric(nfl_df['L'])
    nfl_df['W/L ratio'] = nfl_df['W'] / (nfl_df['W'] + nfl_df['L'])

    metrolist = cities.metro.unique().tolist()
    nfl_df['metro'] = nfl_df['team'].apply(lambda x: ''.join([city for city in metrolist if city in x]))
    nfl_df = nfl_df[['team', 'year', 'W/L ratio', 'metro']]
    nfl_df['metro'].replace(r'^\s*$', np.nan, regex=True, inplace=True)
    citydict = {0: 'Boston', 1: 'Miami–Fort Lauderdale', 3: 'New York City', 10: 'Nashville',
                15: 'San Francisco Bay Area', 16: 'Dallas–Fort Worth', 18: 'Washington, D.C.', 19: 'New York City',
                21: 'Minneapolis–Saint Paul', 25: 'Charlotte', 27: 'Tampa Bay Area', 30: 'San Francisco Bay Area',
                31: 'Phoenix'}
    nfl_df['metro'].fillna(citydict, inplace=True)
    nfl_df['avgWL'] = nfl_df.groupby('metro')['W/L ratio'].transform('mean')

    res = pd.merge(nfl_df, cities, how='inner', left_on='metro', right_on='metro')
    res = res[['metro', 'avgWL', 'Population']]
    res = res.drop_duplicates(subset=['metro'])
    res = res.sort_values(by=['metro'])
    res = res.set_index('metro', drop=True)
    res['Population'] = pd.to_numeric(res['Population'])

    population_by_region = res['Population']  # pass in metropolitan area population from cities
    win_loss_by_region = res[
        'avgWL']  # pass in win/loss ratio from nfl_df in the same order as cities["Metropolitan area"]

    assert len(population_by_region) == len(win_loss_by_region), "Q4: Your lists must be the same length"
    assert len(population_by_region) == 29, "Q4: There should be 29 teams being analysed for NFL"

    return stats.pearsonr(population_by_region, win_loss_by_region)[0]


nfl_correlation()
