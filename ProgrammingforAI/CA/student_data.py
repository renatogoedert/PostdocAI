# Code developed by Renato Francisco Goedert
# Sutudent Number: x25115766

import pandas as pd
import numpy as np
import os
from colorama import Fore, init
import util

# Initialising Colorama, I like Colors, dont judge me!
util.init_colors()

# Set the number of values, could have a input there
num_of_values = 500

# Variable(Dictionary) to store the data
data = {
    'StudentID': [],
    'StudyHours': [],
    'QuizParticipation': [],
    'PastPerformance': [],
    'CourseCompletion': [],
}

# Loop num_of_values time and add to data dictionary 
for  i in range(1, num_of_values+1):
    study_hours = np.random.uniform(1, 40)
    new_entry = {
        data['StudentID'].append(f'S{str(i).zfill(3)}'),
        data['StudyHours'].append(study_hours),
        data['QuizParticipation'].append(np.random.randint(0, 41) + 20 + study_hours),
        data['PastPerformance'].append(np.random.randint(0, 41) + 20 + study_hours),
        data['CourseCompletion'].append(np.random.choice([True, False]))
    }

# After values added, create DataFrame with data
df = pd.DataFrame(data)
print(f"{Fore.LIGHTGREEN_EX}!!! Clean DataFrame Created !!!")

# Row lenght test
print(f"{Fore.YELLOW}--- Running Row Lenght Checks ---")

# Chech right num of entries
assert len(df) == num_of_values, f"X X X ERROR: Expected {num_of_values} entries, got {len(df)} X X X"
print(f"{Fore.LIGHTGREEN_EX}!!! Row count correct - {len(df)} Rows !!!")

# Adding the missing values
print(f"{Fore.YELLOW}--- Adding missing Values ---")

# Choose 3% of the rows to have mising hours and 5% for missing quiz participation and past participation
missing_hours = df.sample(frac=0.03).index
missing_quiz = df.sample(frac=0.05).index
missing_past = df.sample(frac=0.05).index

# Changes the values on the Dataframe
df.loc[missing_hours, 'StudyHours'] = np.nan
df.loc[missing_quiz, 'QuizParticipation'] = np.nan
df.loc[missing_past, 'PastPerformance'] = np.nan

assert df['StudyHours'].isnull().sum() > 0, f"{Fore.RED}X X X ERROR: No NaN Values added X X X"
assert df['QuizParticipation'].isnull().sum() > 0, f"{Fore.RED}X X X ERROR: No NaN Values added X X X"
assert df['PastPerformance'].isnull().sum() > 0, f"{Fore.RED}X X X ERROR: No NaN Values added X X X"
print(f"{Fore.LIGHTGREEN_EX}!!! NaN Values Added !!!")

# Choose 1% of the rows of ID to have empty strings
missing_id = df.sample(frac=0.01).index

# Changes the values on the Dataframe
df.loc[missing_id, 'StudentID'] = ""

assert (df['StudentID'] == "").sum() > 0, f"{Fore.RED}X X X ERROR: No Empty Strings added X X X"
print(f"{Fore.LIGHTGREEN_EX}!!! Empty Strings Added !!!")

# Adding inconsistent values
print(f"{Fore.YELLOW}--- Adding inconsistet Values ---")

# Choose 3% of the rows to have inconsistent participation and 4% for inconsistent performance and 2% for course completion
inconsistent_participation = df.sample(frac=0.03).index
inconsistent_performance = df.sample(frac=0.04).index

# Changes the Value on the dataframe
df.loc[inconsistent_participation, 'QuizParticipation'] = 100 + np.random.randint(1,10, size=len(inconsistent_participation))
df.loc[inconsistent_performance, 'PastPerformance'] = np.random.randint(-40, -1, size=len(inconsistent_performance))

assert (df['QuizParticipation'] > 100).sum() > 0, f"{Fore.RED}X X X ERROR: No Inconsistent Values added X X X"
assert (df['PastPerformance'] < 0).sum() > 0, f"{Fore.RED}X X X ERROR: No Inconsistent Values added X X X"
print(f"{Fore.LIGHTGREEN_EX}!!! Inconsistent Values Added !!!")

# Chose 2% of completions to change type of value
inconsistent_completition = df.sample(frac=0.02).index

# Changes the values on the Dataframe
df.loc[inconsistent_completition, 'CourseCompletion'] = np.random.choice([0,1], size=len(inconsistent_completition))

assert df['CourseCompletion'].dtype == 'object', f"{Fore.RED}X X X ERROR: No Data Type Changed X X X"
print(f"{Fore.LIGHTGREEN_EX}!!! Inconsistent Data Type Added !!!")

# Save dataset on csv
print(f"{Fore.YELLOW}--- Exporting to CSV ---")
util.save_data(df, 'students_raw.csv')