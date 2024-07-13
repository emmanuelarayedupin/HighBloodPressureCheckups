# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load the data
data = {
    "Day": ["08/04/2024", "09/04/2024", "10/04/2024", "11/04/2024", "12/04/2024"],
    "Total Number Seen": [25, 290, 292, 319, 285],
    "<15": [2, 5, 12, 13, 14],
    "15-19": [9, 64, 63, 81, 74],
    "20-24": [5, 65, 74, 77, 84],
    "25-29": [4, 49, 52, 57, 35],
    "30-34": [1, 44, 41, 37, 35],
    "35-40": [1, 33, 20, 38, 26],
    ">40": [3, 34, 30, 13, 16],
    "Male": [17, 159, 155, 170, 140],
    "Female": [8, 131, 131, 149, 145]
}

# Convert the data into a pandas DataFrame
df = pd.DataFrame(data)

# Convert 'Day' to datetime format
df['Day'] = pd.to_datetime(df['Day'], format='%d/%m/%Y')

# Data validation: Ensure totals match
df['Total Calculated'] = df['<15'] + df['15-19'] + df['20-24'] + df['25-29'] + df['30-34'] + df['35-40'] + df['>40']
if not np.all(df['Total Number Seen'] == df['Total Calculated']):
    print("Warning: Discrepancy between total number seen and calculated total from age groups!")

# Summary statistics
summary_stats = df.describe()
print("Summary Statistics:")
print(summary_stats)

# Save summary statistics to a CSV file
summary_stats.to_csv('summary_statistics.csv')

# Gender distribution plot
plt.figure(figsize=(10, 6))
sns.barplot(x='Day', y='value', hue='variable', data=pd.melt(df, ['Day'], ['Male', 'Female']))
plt.title('Gender Distribution Over Days')
plt.xlabel('Day')
plt.ylabel('Count')
plt.legend(title='Gender')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('gender_distribution.png')
plt.show()

# Age group distribution plot
age_groups = ['<15', '15-19', '20-24', '25-29', '30-34', '35-40', '>40']
plt.figure(figsize=(10, 6))
sns.lineplot(data=df[age_groups])
plt.title('Age Group Distribution Over Days')
plt.xlabel('Day')
plt.ylabel('Count')
plt.legend(title='Age Group', labels=age_groups)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('age_group_distribution.png')
plt.show()

# Correlation analysis
correlation_matrix = df.corr()
print("Correlation Matrix:")
print(correlation_matrix)

# Heatmap of the correlation matrix
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Matrix Heatmap')
plt.tight_layout()
plt.savefig('correlation_matrix_heatmap.png')
plt.show()

# Attendance trend plot
plt.figure(figsize=(10, 6))
sns.lineplot(x='Day', y='Total Number Seen', data=df, marker='o')
plt.title('Attendance Trend Over Days')
plt.xlabel('Day')
plt.ylabel('Total Number Seen')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('attendance_trend.png')
plt.show()
