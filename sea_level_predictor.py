import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    fig = plt.figure(0)
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])
    plt.xlabel("Year")
    plt.ylabel("CSIRO Adjusted Sea Level")

    # Create first line of best fit
    slope_all, intercept_all, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_all = pd.Series(range(df['Year'].min(), 2051))
    y_all = slope_all * x_all + intercept_all
    plt.plot(x_all, y_all, 'r', label='Best Fit Line (1880-2050)')

    # Create second line of best fit
    df_recent = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, _, _, _ = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    x_recent = pd.Series(range(2000, 2051))
    y_recent = slope_recent * x_recent + intercept_recent
    plt.plot(x_recent, y_recent, 'green', label='Best Fit Line (2000-2050)')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    handles, labels = plt.gca().get_legend_handles_labels()
    by_label = dict(zip(labels, handles))
    plt.legend(by_label.values(), by_label.keys())

    plt.grid(True)
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()