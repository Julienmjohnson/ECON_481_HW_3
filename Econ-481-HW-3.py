# Exercise 0
import pandas as pd
import numpy as np
def github() -> str:
    """
    Returns a string for the github link for this assignment.
    """

    return "https://github.com/Julienmjohnson/ECON_481_HW_3/blob/main/Econ-481-HW-3.py" 
 
# Exercise 1
def import_yearly_data(years: list) -> pd.DataFrame:
    """
    Returns a single data frame of all the year specified's EPA's direct emitter data
    """
    Data_Series = []
    for i in years:
        New_Series = pd.read_excel(f"https://lukashager.netlify.app/econ-481/data/ghgp_data_{i}.xlsx", sheet_name = "Direct Emitters", header = 3)
        New_Series["year"] = i
        Data_Series.append(New_Series)
    
    return pd.concat(Data_Series)

#Exercise 2
def import_parent_companies(years: list) -> pd.DataFrame:
    """
    Returns a data frame of all the years specified's parent company data of each facility
    """
    url = 'https://lukashager.netlify.app/econ-481/data/ghgp_data_parent_company_09_2023.xlsb'
    Data_Series = []
    for i in years:
        New_Series = pd.read_excel(url, sheet_name = str(i))
        pd.DataFrame.dropna(New_Series, how = 'all')
        
        New_Series["year"] = i
        Data_Series.append(New_Series)
    
    return pd.concat(Data_Series)

#Exercise 3
def n_null(df: pd.DataFrame, col: str) -> int:
    """
    Returns a integer of the number of null values in the data frame along a specified column
    """
    obj = pd.isna(df[col])
    n = 0
    for i in np.arange(len(obj)):
        if obj[i]:
            n += 1
    
    return n

# Exercise 4
def clean_data(emissions_data: pd.DataFrame, parent_data: pd.DataFrame) -> pd.DataFrame:
    """
    Returns a data frame of the emissions data merged with which facilities produced those emissions and data about their parent company.
    """
    obj = parent_data.rename(columns={"GHGRP FACILITY ID":"Facility Id"})
    obj1 = pd.merge(emissions_data, obj, on = ['year',"Facility Id"], how='left')
    obj2 = obj1[["Facility Id","year", "State","Industry Type (sectors)","Total reported direct emissions","PARENT CO. STATE","PARENT CO. PERCENT OWNERSHIP"]]
    obj3 = obj2.rename(str.lower, axis='columns')
    
    return obj3

#Exercise 5
def aggregate_emissions(df: pd.DataFrame, group_vars: list) -> pd.DataFrame:
    """
    Returns a data frame of the aggregation of the emissions data along a choice of specified variables, grouping up each term by the same variable name, then finding and reporting the minimum, median, mean and max for total reported direct emissions and percentage of ownership by the parent company 
    """
    
    return df.groupby(group_vars)[["total reported direct emissions", "parent co. percent ownership"]].agg(["min", "median", "mean", "max"]).sort_values(('total reported direct emissions','mean'), ascending=False)