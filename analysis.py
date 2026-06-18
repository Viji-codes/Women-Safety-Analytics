# Women Safety Analytics - India
# By Vijaya Lakshmi

import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('CrimesOnWomenData.csv')

# Basic information
print("Dataset Shape:", df.shape)
print("\nColumn Names:")
print(df.columns.tolist())

# Total crimes per state
state_crimes = df.groupby('State').sum().sum(axis=1)

# Top 10 Most Dangerous States
plt.figure(figsize=(12,6))
state_crimes.sort_values(ascending=False).head(10).plot(
    kind='bar',
    color='red'
)
plt.title('Top 10 States with Highest Crimes Against Women in India')
plt.xlabel('State')
plt.ylabel('Total Crimes')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('top_states.png')
plt.show()

print("\nTop 10 States:")
print(state_crimes.sort_values(ascending=False).head(10))
print("\nAnalysis Complete!")