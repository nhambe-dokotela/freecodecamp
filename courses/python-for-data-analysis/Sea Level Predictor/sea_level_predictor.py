import pandas as pd 
import matplotlib.pyplot as plt 
from scipy.stats import linregress

def draw_plot():
    df = pd.read_csv('epa-sea-level.csv')
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Line of best fit 1
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_pred = pd.Series(range(1880, 2051))
    sea_level = slope * x_pred + intercept
    plt.plot(x_pred, sea_level)
    
    # Line of best fit 2
    df_2000 = df[df['Year'] >= 2000]
    slope, intercept, r_value, p_value, std_err = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    x_pred = pd.Series(range(2000, 2051))
    sea_level = slope * x_pred + intercept
    plt.plot(x_pred, sea_level)


    plt.ylabel('Sea Level (inches)')
    plt.xlabel('Year')
    plt.title('Rise in Sea Level')
    plt.savefig('sea_level_plot.png')
    return plt
