# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

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

df = pd.DataFrame(data)

# Basic analysis
summary = df.describe()
print("Summary of the data:")
print(summary)

# Plotting total number seen each day
plt.figure(figsize=(10, 6))
plt.plot(df['Day'], df['Total Number Seen'], marker='o', label='Total Number Seen')
plt.xlabel('Day')
plt.ylabel('Total Number Seen')
plt.title('High Blood Pressure Checkup Attendance')
plt.legend()
plt.grid(True)
plt.savefig('attendance_plot.png')
plt.show()

# Plotting number of patients by age group
age_groups = ['<15', '15-19', '20-24', '25-29', '30-34', '35-40', '>40']
df[age_groups].sum().plot(kind='bar', figsize=(10, 6))
plt.xlabel('Age Group')
plt.ylabel('Number of Patients')
plt.title('Patients by Age Group')
plt.savefig('age_group_plot.png')
plt.show()

# Plotting number of patients by gender
gender_groups = ['Male', 'Female']
df[gender_groups].sum().plot(kind='bar', figsize=(10, 6))
plt.xlabel('Gender')
plt.ylabel('Number of Patients')
plt.title('Patients by Gender')
plt.savefig('gender_plot.png')
plt.show()
