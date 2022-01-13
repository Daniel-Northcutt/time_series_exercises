import pandas as pd
from datetime import timedelta, datetime
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

import warnings
warnings.filterwarnings("ignore")

from acquire import get_store_data

# plotting defaults
plt.rc('figure', figsize=(13, 7))
plt.style.use('seaborn-whitegrid')
plt.rc('font', size=16)


############
def prep_store_data(df):
    #Reassign the sale_date column to be a datetime type
    df.sale_date = pd.to_datetime(df.sale_date)
    
    # Set index to datetime intervals
    df = df.set_index('sale_date').sort_index()
    
    #Creating new features from our data
    df['month'] = df.index.month_name()
    df['day_of_week'] = df.index.day_name()
    df['sales_total'] = df['sale_amount'] * df['item_price']
    
    return df
################
def prepare_ops_data(df):
    # read it
    df= pd.read_csv("https://raw.githubusercontent.com/jenfly/df/master/df_germany_daily.csv")
    
    # convert to datetime format for date column
    df.Date = pd.to_datetime(df.Date)
    
    #set the index
    df= df.set_index('Date').sort_index()
    
    # Creating new features from our data
    df['year'] = pd.DatetimeIndex(df.index).year
    df['month'] = pd.DatetimeIndex(df.index).month_name()
    
    #should be no-nas but in case
    df= df.fillna(0)
    
    return df