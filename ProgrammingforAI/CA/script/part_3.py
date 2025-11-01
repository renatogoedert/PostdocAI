# Code developed by Renato Francisco Goedert
# Sutudent Number: x25115766

from colorama import Fore
from . import util

def make_descriptive_stats(df):
    """
    Runs the function to make the descriptive statistcs

    Args:
        df (pd.DataFrame): The DataFrame to be manipulated.
    
    Returns:
        pd.DataFrame or None: The manipulated DataFrame.
    """
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
    high_score_c = df[((df['QuizParticipation'] + df['PastPerformance'])/2 > 70) & (df['CourseCompletion'] == True)]
    print(f"Found {len(high_score_c)} students who ended course with an Score above 70.")

    # Filtering Incompleted Course
    high_score_i = df[((df['QuizParticipation'] + df['PastPerformance'])/2 > 70) & (df['CourseCompletion'] == False)]
    print(f"Found {len(high_score_i)} students who still on course with an Score above 70.")

    return df

def make_func_programin(df):
    """
    Runs the function to add functional proframming

    Args:
        df (pd.DataFrame): The DataFrame to be manipulated.
    
    Returns:
        pd.DataFrame or None: The manipulated DataFrame.
    """
    # Functional Programming
    print(f"\n{Fore.YELLOW}--- Classifying using Functional Programming ---")

    # Classification using a lambda function
    performance_classifier = lambda score: 'High' if score >= 0.7 else ('Medium' if 0.4 <= score else 'Low')

    # Apply the lambda function
    df['PerformanceCategory'] = df['Engagement'].apply(performance_classifier)

    print("New 'PerformanceCategory' column created. Showing value counts:")
    print(df['PerformanceCategory'].value_counts())
    print("\nDataFrame head with the new category:")
    print(df.head())

    # Creating the Completed Column
    print(f"\n{Fore.YELLOW}--- Creating Completed Category ---")

    # Classification using a lambda function
    completed = lambda c: 'Completed' if c else 'Not Completed'

    # Apply the lambda function
    df['Completed'] = df['CourseCompletion'].apply(completed)

    print("New 'Completed' column created.")
    print(df['Completed'].value_counts())
    print("\nDataFrame head with the new category:")
    print(df.head())

    return df

def main():
    # Initialising Colorama, I like Colors, dont judge me!
    util.init_colors()

    # Try to load the dataset
    df = util.load_data('students_clean.csv')

    df = make_descriptive_stats(df)
    df = make_func_programin(df)

    # Save the cleaned data to a new file
    util.save_data(df, 'students_clean.csv')

if __name__ == "__main__":
    main()
