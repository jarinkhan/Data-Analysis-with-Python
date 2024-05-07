import pandas as pd

# Import the data
df = pd.read_csv('epa-sea-level.csv')
import matplotlib.pyplot as plt

# Create scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue')

# Labeling the axes and title
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sea Level')
from scipy.stats import linregress

# Perform linear regression
slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

# Plot the line of best fit
plt.plot(df['Year'], intercept + slope*df['Year'], 'r', label='fitted line')

# Predict sea level rise in 2050
plt.axvline(x=2050, color='green', linestyle='--')

# Show legend
plt.legend()

# Save and return the image
plt.savefig('sea_level_plot.png')
plt.show()
# Filter the data from year 2000 onwards
df_recent = df[df['Year'] >= 2000]

# Perform linear regression on recent data
slope_recent, intercept_recent, _, _, _ = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])

# Plot the line of best fit for recent data
plt.plot(df_recent['Year'], intercept_recent + slope_recent*df_recent['Year'], 'g', label='fitted line (2000 onwards)')

# Predict sea level rise in 2050 based on recent data
plt.axvline(x=2050, color='orange', linestyle='--')

# Show legend
plt.legend()

# Save and return the image
plt.savefig('sea_level_plot_recent.png')
plt.show()
