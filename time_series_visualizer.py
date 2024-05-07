import pandas as pd

# Import the data and set the index to the date column
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

# Filter out days with page views in top or bottom 2.5%
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]

import matplotlib.pyplot as plt

def draw_line_plot():
    # Copy the dataframe
    df_line = df.copy()

    # Create line plot
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(df_line.index, df_line['value'], color='red')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    
    # Save and return the image
    fig.savefig('line_plot.png')
    return fig
def draw_bar_plot():
    # Copy the dataframe and extract year and month
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month_name()

    # Create pivot table
    df_bar = df_bar.pivot_table(index='year', columns='month', values='value', aggfunc='mean')

    # Create bar plot
    fig = df_bar.plot(kind='bar', figsize=(10, 6)).figure
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.title('Average Page Views per Year')
    plt.legend(title='Months')
    plt.xticks(rotation=45)
    
    # Save and return the image
    fig.savefig('bar_plot.png')
    return fig
import seaborn as sns

def draw_box_plot():
    # Copy the dataframe and extract year and month
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Create box plot
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))
    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0])
    sns.boxplot(x='month', y='value', data=df_box, ax=axes[1], order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')
    
    # Save and return the image
    fig.savefig('box_plot.png')
    return fig
