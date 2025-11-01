# Code developed by Renato Francisco Goedert
# Sutudent Number: x25115766

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from colorama import Fore
from . import util

def make_scatter_graph(df):
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

    # Save file as PNG
    util.save_plot('scatter_performance_hours.png')

def make_histogram_graph(df):
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

    # Save file as PNG
    util.save_plot('histogram_quiz_participation.png')

def make_bar_graph(df):
    # Make a Bar Chart (Performance Category Distribution)
    print(f"{Fore.YELLOW}--- Generating Bar Chart (Average Engagement by Course Completion ---")

    group_stats = df.groupby('Completed')['Engagement'].mean().reset_index()
    plt.figure(figsize=(8, 6))
    bar_graph = sns.barplot(
        data=group_stats,
        x='Completed',
        y='Engagement'
    )

    # Add labels and title
    bar_graph.set_title('Average Engagement by Course Completion Status', fontsize=16)
    bar_graph.set_xlabel('Course Completion Status', fontsize=12)
    bar_graph.set_ylabel('Average Engagement Score', fontsize=12)

    plt.ylim(0, 1) 

    # Save file as PNG
    util.save_plot('bar_chart_avg_engagement.png')

def make_pie_graph(df):
    # Make a Pie Chart (Performance Category Distribution)
    print(f"{Fore.YELLOW}--- Generating Pie Chart (Performance Category Distribution) ---")

    category_counts = df['PerformanceCategory'].value_counts()
    plt.figure(figsize=(8, 8))
    plt.pie(
        category_counts,
        labels=category_counts.index,
        autopct='%1.1f%%', # Adds percentage labels with one decimal place
        startangle=140,      # Rotates the chart for better label placement
        colors=['#4CAF50', '#FFC107', '#F44336'] 
    )

    # Add labels and title
    plt.title('Distribution of Student Performance Categories', fontsize=16)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    # Save file as PNG
    util.save_plot('pie_chart_performance_category.png')

def main():
    # Initialising Colorama, I like Colors, dont judge me!
    util.init_colors

    # Set a consistent style for the plots
    sns.set_theme(style="whitegrid")

    # Try to load the dataset
    df = util.load_data('students_clean.csv')
    make_scatter_graph(df)
    make_histogram_graph(df)
    make_bar_graph(df)
    make_pie_graph(df)


if __name__ == "__main__":
    main()
