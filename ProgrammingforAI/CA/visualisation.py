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
print(f"{Fore.YELLOW}--- Generating Scatter Plot (Study Hours vs Past Performance) ---")

plt.figure(figsize=(10, 6))
scatter_graph = sns.scatterplot(
    data=df,
    x='StudyHours',
    y='PastPerformance',
    hue='Completed',  # Color-codes points based on course completion 
    style='Completed', # Uses different marker shapes 
    alpha=0.8
)

# Add labels and title
scatter_graph.set_title('Study Hours vs Past Performance', fontsize = 16)
scatter_graph.set_xlabel('Study Hours (Normalized)', fontsize=12)
scatter_graph.set_ylabel('Past Performance Score (%)', fontsize=12)
plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0.)
plt.tight_layout()

# Save file as PNG
plt.savefig('scatter_performance_hours.png')
print(f"{Fore.GREEN}--- Scatter plot saved to scatter_performance_hours.png ---")
plt.show()

# Make a Histogram (Distribution of Quiz Participation)
print(f"{Fore.YELLOW}--- Generating Scatter Plot (Distribution of Quiz Participation) ---")

plt.figure(figsize=(10, 6))
hist_graph = sns.histplot(
    data=df,
    x='QuizParticipation',
    bins=20, # Divides the data into 20 bins for a clear distribution
    kde=True # Adds a smooth line to show the distribution curve
)

# Add labels and title
hist_graph.set_title('Distribution of Quiz Participation', fontsize=16)
hist_graph.set_xlabel('Quiz Participation Score (%)', fontsize=12)
hist_graph.set_ylabel('Number of Students', fontsize=12)

# Fixing plot to start in (0,0)
plt.xlim(left=0)
plt.ylim(bottom=0)
plt.tight_layout()

# Save file as PNG
plt.savefig('histogram_quiz_participation.png')
print(f"{Fore.GREEN}--- Histogram saved to histogram_quiz_participation.png ---")
plt.show()