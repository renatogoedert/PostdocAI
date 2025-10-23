# Code developed by Renato Francisco Goedert
# Sutudent Number: x25115766

import pandas as pd
import numpy as np
from colorama import Fore, Style, init
import os 

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

print("\n\n--- Solving Dataset Issues ---")

# Solving Missing ID
print("--- Adding missing IDs ---")
if df['StudentID'].isnull().sum() > 0:
    #Find the highest ID number
    last_id = df['StudentID'].dropna().str[1:].astype(int).max()

    # Rows with missing ID
    missing_id = df[df['StudentID'].isnull()].index

    #Loop to give the ID
    for i in range(len(missing_id)):

        index = missing_id[i]
        new = last_id + i + 1
        new_id = f"S{str(new).zfill(3)}"

        df.loc[index, 'StudentID'] = new_id
else:
    print("--- No Missing Value Found! ---")

# Test for missing ID solved
assert df['StudentID'].isnull().sum() == 0, f"{Fore.RED}X X X ERROR: StudentIDs missing values not solved! X X X"
print(f"{Fore.GREEN}!!! Missing IDS solved !!!")


# Save the cleaned data to a new file
output_filename = 'students_clean.csv'
df.to_csv(output_filename, index=False)

# Chech file is created
assert os.path.exists('students_clean.csv'), f"{Fore.RED}X X X ERROR: File not Created! X X X"
print(f"\n\n{"\033[38;5;46m"}!!! CSV File Created !!!")