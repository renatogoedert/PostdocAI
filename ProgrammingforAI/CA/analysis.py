# Code developed by Renato Francisco Goedert
# Sutudent Number: x25115766

import pandas as pd
import numpy as np
from colorama import Fore, Style, init

# Initialising Colorama, I like Colors, dont judge me!
init(autoreset=True)

# Try to load the dataset
try:
    df = pd.read_csv('students_raw.csv')
    print(f"{"\033[38;5;46m"} Succesfully loaded students_raw.csv")
except FileNotFoundError:
    print(f"{Fore.RED} ERROR: file not found. Make sure you have run python \"student_data.py\" ")

# Print the info of the dataframe
print("\n--- Initial DataFrame Info ---")
df.info()

# Print the missing values
print("\n--- Handling Missing Values ---")
print(f"Initial missing values before cleaning:\n{df.isnull().sum()}")

# Print the inconsistencies
print("\nOther Inconsistencies:")

# Inconsistecies on Study Hours 
if 'StudyHours' in df.columns:
    num_perf = pd.to_numeric(df['StudyHours'], errors='coerce')
    over_values = (num_perf > 168).sum()
    if over_values > 0:
        print(f" - Found {over_values} over the limit on StudyHours")
        over_values = (num_perf > 100).sum()
    neg_values = (num_perf < 0).sum()
    if neg_values > 0:
        print(f" - Found {neg_values} negative values on StudyHours")

# Inconsistecies on Quiz Participation 
if 'QuizParticipation' in df.columns:
    num_perf = pd.to_numeric(df['QuizParticipation'], errors='coerce')
    over_values = (num_perf > 100).sum()
    if over_values > 0:
        print(f" - Found {over_values} over the limit on QuizParticipation")
        over_values = (num_perf > 100).sum()
    neg_values = (num_perf < 0).sum()
    if neg_values > 0:
        print(f" - Found {neg_values} negative values on QuizParticipation")

# Inconsistecies on Quiz Past Performance:
if 'PastPerformance' in df.columns:
    num_perf = pd.to_numeric(df['PastPerformance'], errors='coerce')
    over_values = (num_perf > 100).sum()
    if over_values > 0:
        print(f" - Found {over_values} over the limit on PastPerformance")
        over_values = (num_perf > 100).sum()
    neg_values = (num_perf < 0).sum()
    if neg_values > 0:
        print(f" - Found {neg_values} negative values on PastPerformance")

# Inconsistecies on Course Completition:
if 'CourseCompletition' in df.columns:
    unique_values = df['CourseCompletition'].unique()

    set_uniques = {str(val) for val in unique_values
                   }
    if set_uniques != {'False', 'True'}:
        print(f" - Unique Values in CourseCompletition: {unique_values}")

# Solving Missing ID

# Save the cleaned data to a new file
output_filename = 'students_clean.csv'
df.to_csv(output_filename, index=False)
print(f"\n✅ Cleaned data saved as '{output_filename}'.")

# Display final info to confirm the data is clean
print("\n--- Final Cleaned DataFrame Info ---")
df.info()
print("\nFirst 5 rows of the clean data:")
print(df.head())