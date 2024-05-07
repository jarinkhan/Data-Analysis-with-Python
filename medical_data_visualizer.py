import pandas as pd

# Import the data
df = pd.read_csv('medical_examination.csv')

# Calculate BMI and create overweight column
df['overweight'] = (df['weight'] / ((df['height'] / 100) ** 2) > 25).astype(int)

# Normalize cholesterol and gluc
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

import seaborn as sns
import matplotlib.pyplot as plt

def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using variables cholesterol, gluc, smoke, alco, active, and overweight
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature.
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')

    # Rename the 'value' column to 'variable'
    df_cat = df_cat.rename(columns={'value': 'variable'})

    # Draw the catplot with 'sns.catplot()'
    fig = sns.catplot(data=df_cat, x='variable', y='total', hue='value', kind='bar', col='cardio')
    fig.set_axis_labels("variable", "total")
    fig.set_xticklabels(rotation=90)

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig

def draw_heat_map():
    # Clean the data
    df_heat = df[
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = corr.where(np.triu(np.ones(corr.shape), k=1).astype(np.bool))

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 10))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, annot=True, fmt=".1f", linewidths=.5, mask=mask, vmax=.3, center=0.09, square=True, cbar_kws={"shrink": .5})

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
