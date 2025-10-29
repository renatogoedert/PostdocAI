import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from colorama import Fore, init

# Initialising Colorama, I like Colors, dont judge me!
init(autoreset=True)

# Try to load the dataset
try:
    df = pd.read_csv('students_clean.csv')
    print(f"{"\033[38;5;46m"} Succesfully loaded students_clean.csv")
except FileNotFoundError:
    print(f"{Fore.RED} ERROR: file not found. Make sure you have run python \"analysis.py\" ")

# Descriptive Statistics
print(f"\n{Fore.YELLOW}--- Getting Descriptive Statistics ---\n")
stats = df[['StudyHours', 'QuizParticipation']].describe().loc[['mean', '50%', 'std']]
print("Descriptive Statistics for Study Hours and Quiz Participation:")
print(stats)

# Grouping students
print(f"\n{Fore.YELLOW}--- Getting Grouped Analysis ---\n")
group_stats = df.groupby('CourseCompletion').agg(NumberOfStudents=('StudentID', 'count'), AverageEngagement=('Engagement', 'mean')).reset_index()
print("Descriptive Statistics for Average Engagement by Course Completion:")
print(group_stats)

# Filtering Operations
print(f"\n{Fore.YELLOW}---Filtering Data ---\n")

# Filtering By high Score
print(f"{Fore.YELLOW}--- Filtering Students with High Score (Score > 0.7) ---\n")

# Filtering Completed Course
high_score_c = df[((df['QuizParticipation'] + df['PastPerformance'])/2 > 75) & (df['CourseCompletion'] == True)]
print(f"Found {len(high_score_c)} students who ended course with an Score above 75.")

# Filtering Incompleted Course
high_score_i = df[((df['QuizParticipation'] + df['PastPerformance'])/2 > 75) & (df['CourseCompletion'] == False)]
print(f"Found {len(high_score_i)} students who still on course with an Score above 75.")

# Functional Programming
print(f"\n{Fore.YELLOW}--- Classifying using Functional Programming ---")

# Classification using a lambda function
performance_classifier = lambda score: 'High' if score >= 70 else ('Medium' if 40 <= score < 70 else 'Low')

# Apply the lambda function
df['PerformanceCategory'] = df['PastPerformance'].apply(performance_classifier)

print("New 'PerformanceCategory' column created. Showing value counts:")
print(df['PerformanceCategory'].value_counts())
print("\nDataFrame head with the new category:")
print(df.head())