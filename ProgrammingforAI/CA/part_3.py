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