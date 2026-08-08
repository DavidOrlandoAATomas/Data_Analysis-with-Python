import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit (using all data)
    res_all = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_all = pd.Series(range(df['Year'].min(), 2051))
    ax.plot(
        years_all,
        res_all.slope * years_all + res_all.intercept,
        'r',
        label='Best fit line (all data)'
    )

    # Create second line of best fit (using data from year 2000 onwards)
    df_recent = df[df['Year'] >= 2000]
    res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_recent = pd.Series(range(2000, 2051))
    ax.plot(
        years_recent,
        res_recent.slope * years_recent + res_recent.intercept,
        'g',
        label='Best fit line (2000-present)'
    )

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
