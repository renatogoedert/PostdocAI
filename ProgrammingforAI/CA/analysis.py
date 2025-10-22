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
print("\n--- Initial DataFrame Info ---\n")
df.info()