import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from colorama import Fore, init

# Initialising Colorama, I like Colors, dont judge me!
init(autoreset=True)

# Set a consistent style for the plots
sns.set_theme(style="whitegrid")

# Try to load the dataset
try:
    df = pd.read_csv('students_clean.csv')
    print(f"{"\033[38;5;46m"} Succesfully loaded students_clean.csv")
except FileNotFoundError:
    print(f"{Fore.RED} ERROR: file not found. Make sure you have run python \"analysis.py\" ")

# Start Plotting
print(f"\n{Fore.YELLOW}--- Start the Ploting Code ---\n")

# Make a Scatter Plot (Study Hours vs Past Performance)
print(f"\n{Fore.YELLOW}--- Generating Scatter Plot (Study Hours vs Past Performance) ---\n")

plt.figure(figsize=(10, 6))
scatter_graph = sns.scatterplot(
    data=df,
    x='StudyHours',
    y='PastPerformance',
    hue='CourseCompletion',  # Color-codes points based on course completion 
    style='CourseCompletion', # Uses different marker shapes 
    alpha=0.8
)

# Add labels and title
scatter_graph.set_title('Study Hours vs Past Performance', fontsize = 16)
scatter_graph.set_xlabel('Study Hours (Normalized)', fontsize=12)
scatter_graph.set_ylabel('Past Performance Score (%)', fontsize=12)

# Save file as PNG
plt.savefig('scatter_performance_hours.png')
print(f"{Fore.GREEN}--- Scatter plot saved to scatter_performance_hours.png ---")
plt.show()