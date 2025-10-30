import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
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

# Fixing plot area and legend out of chart
plt.xlim(left=0, right=1)
plt.ylim(bottom=0, top=100)
plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0.)
plt.tight_layout()

# Save file as PNG
print(f"{Fore.YELLOW}--- Saving Scatter plot to scatter_performance_hours.png ---")
plt.savefig('scatter_performance_hours.png')

# Chech file is created
assert os.path.exists('scatter_performance_hours.png'), f"{Fore.RED}X X X ERROR: File not Created! X X X"
print(f"{"\033[38;5;46m"}!!! Scatter Plot PNG Created !!!")
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

# Fixing plot area
plt.ylim(bottom=0, top=100)
plt.xlim(left=np.floor(min(df['QuizParticipation'])/10)*10, right=100)
plt.tight_layout()

# Save file as PNG
print(f"{Fore.YELLOW}--- Saving Histogram to histogram_quiz_participation.png ---")
plt.savefig('histogram_quiz_participation.png')

# Chech file is created
assert os.path.exists('histogram_quiz_participation.png'), f"{Fore.RED}X X X ERROR: File not Created! X X X"
print(f"{"\033[38;5;46m"}!!! Histogram PNG Created !!!")
plt.show()

# Make a Pie Chart (Performance Category Distribution)
print(f"{Fore.YELLOW}--- Generating Pie Chart (Performance Category Distribution) ---")

category_counts = df['PerformanceCategory'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(
    category_counts,
    labels=category_counts.index,
    autopct='%1.1f%%', # Adds percentage labels with one decimal place
    startangle=140,      # Rotates the chart for better label placement
    colors=['#4CAF50', '#FFC107', '#F44336'] # Green, Amber, Red colors
)

# 3. Add a title and ensure the pie is a circle
plt.title('Distribution of Student Performance Categories', fontsize=16)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# 4. Save and show the plot
plt.savefig('pie_chart_performance_category.png')
print(f"{Fore.GREEN}--- Pie chart saved to pie_chart_performance_category.png ---")
plt.show()