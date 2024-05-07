import pandas as pd

# Load the dataset
data_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data'
column_names = ['age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status', 
                'occupation', 'relationship', 'race', 'sex', 'capital-gain', 'capital-loss', 
                'hours-per-week', 'native-country', 'salary']
df = pd.read_csv(data_url, names=column_names, na_values=' ?')

# Question 1: How many people of each race are represented in this dataset?
race_counts = df['race'].value_counts()

# Question 2: What is the average age of men?
average_age_men = df[df['sex'] == ' Male']['age'].mean()

# Question 3: What is the percentage of people who have a Bachelor's degree?
percentage_bachelors = (df['education'] == ' Bachelors').mean() * 100

# Question 4: What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
higher_education = df[df['education'].isin([' Bachelors', ' Masters', ' Doctorate'])]
percentage_higher_education_rich = (higher_education['salary'] == ' >50K').mean() * 100

# Question 5: What percentage of people without advanced education make more than 50K?
lower_education = df[~df['education'].isin([' Bachelors', ' Masters', ' Doctorate'])]
percentage_lower_education_rich = (lower_education['salary'] == ' >50K').mean() * 100

# Question 6: What is the minimum number of hours a person works per week?
min_work_hours = df['hours-per-week'].min()

# Question 7: What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
num_min_workers = df[df['hours-per-week'] == min_work_hours]
rich_percentage = (num_min_workers['salary'] == ' >50K').mean() * 100

# Question 8: What country has the highest percentage of people that earn >50K and what is that percentage?
highest_earning_country = (df[df['salary'] == ' >50K']['native-country']
                           .value_counts(normalize=True).idxmax())
highest_earning_country_percentage = (df[df['native-country'] == highest_earning_country]
                                      ['salary'] == ' >50K').mean() * 100

# Question 9: Identify the most popular occupation for those who earn >50K in India
top_IN_occupation = (df[(df['native-country'] == ' India') & (df['salary'] == ' >50K')]
                     ['occupation'].value_counts().idxmax())

# Print results
print("Question 1: How many people of each race are represented in this dataset?\n", race_counts)
print("\nQuestion 2: What is the average age of men?\n", average_age_men)
print("\nQuestion 3: What is the percentage of people who have a Bachelor's degree?\n", percentage_bachelors)
print("\nQuestion 4: What percentage of people with advanced education make more than 50K?\n", percentage_higher_education_rich)
print("\nQuestion 5: What percentage of people without advanced education make more than 50K?\n", percentage_lower_education_rich)
print("\nQuestion 6: What is the minimum number of hours a person works per week?\n", min_work_hours)
print("\nQuestion 7: What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?\n", rich_percentage)
print("\nQuestion 8: What country has the highest percentage of people that earn >50K and what is that percentage?\n", highest_earning_country, highest_earning_country_percentage)
print("\nQuestion 9: Identify the most popular occupation for those who earn >50K in India\n", top_IN_occupation)
