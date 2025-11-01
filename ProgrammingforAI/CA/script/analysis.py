# Code developed by Renato Francisco Goedert
# Sutudent Number: x25115766

import pandas as pd
import numpy as np
from colorama import Fore
from . import util

def print_dataframe_info(df):
    """
    Print dataframe info, missing values and inconsistencies 

    Args:
        df (pd.DataFrame): The DataFrame info to be printed.

    """
    # # Print the info of the dataframe
    # print("\n Initial DataFrame Info: ")
    # df.info()

    # Print the missing values
    print(f"Missing values:\n{df.isnull().sum()}")

    # Print the inconsistencies
    print("\nOther Inconsistencies:")

    # Inconsistecies on Study Hours 
    if 'StudyHours' in df.columns:
        num_perf = pd.to_numeric(df['StudyHours'], errors='coerce')
        over_values = (num_perf > 40).sum()
        neg_values = (num_perf < 0).sum()

        if over_values > 0:
            print(f" - Found {over_values} over the limit on StudyHours")
        elif neg_values > 0:
            print(f" - Found {neg_values} negative values on StudyHours")
        else:
            print(f" - Found no Inconsistencies on StudyHours")

    # Inconsistecies on Quiz Participation 
    if 'QuizParticipation' in df.columns:
        num_perf = pd.to_numeric(df['QuizParticipation'], errors='coerce')
        over_values = (num_perf > 100).sum()
        neg_values = (num_perf < 0).sum()
        if over_values > 0:
            print(f" - Found {over_values} over the limit on QuizParticipation")
        elif neg_values > 0:
            print(f" - Found {neg_values} negative values on QuizParticipation")
        else:
            print(f" - Found no Inconsistencies on QuizParticipation")

    # Inconsistecies on Quiz Past Performance:
    if 'PastPerformance' in df.columns:
        num_perf = pd.to_numeric(df['PastPerformance'], errors='coerce')
        over_values = (num_perf > 100).sum()
        neg_values = (num_perf < 0).sum()
        if over_values > 0:
            print(f" - Found {over_values} over the limit on PastPerformance")
        elif neg_values > 0:
            print(f" - Found {neg_values} negative values on PastPerformance")
        else:
            print(f" - Found no Inconsistencies on PastPerformance")

    # Inconsistecies on Course Completition:
    if 'CourseCompletion' in df.columns:
        unique_values = df['CourseCompletion'].unique()

        set_uniques = {str(val) for val in unique_values
                    }
        if set_uniques != {'False', 'True'}:
            print(f" - Unique Values in CourseCompletion: {unique_values}")
        else:
            print(f" - Found no Inconsistencies on CourseCompletion")

def solve_incosistencies(df):
    """
    Runs the function to solve inconsistents values

    Args:
        df (pd.DataFrame): The DataFrame to be manipulated.
    
    Returns:
        pd.DataFrame or None: The manipulated DataFrame.
    """

    # Solving Inconsistecies on Study Hours
    print(f"{Fore.YELLOW}--- Solving Inconsistecies on Study Hours ---")
    if 'StudyHours' in df.columns:
        # Ensuring Numeric Study Hours
        df['StudyHours'] = pd.to_numeric(df['StudyHours'], errors='coerce')

        # Finding Neg StudyHours
        neg_index = df['StudyHours'] < 0

        # If negative StudyHours change it to nan
        if neg_index.sum() > 0 :
            df.loc[neg_index, 'StudyHours'] = np.nan

        # Finding StudyHours over the limit
        over_index = df['StudyHours'] > 40

        # IF over the limit values, change them to limit
        if over_index.sum() > 0:
            df.loc[over_index, 'StudyHours'] = 40

    # Test for Inconsistecies StudyHours solved
    assert (df['StudyHours'] < 0).sum() == 0 or (df['StudyHours'] > 40).sum() == 0, f"{Fore.RED}X X X ERROR: StudyHours Inconsistecies not solved! X X X"
    print(f"{Fore.GREEN}!!! Inconsistecies StudyHours solved !!!")

    # Solving Inconsistecies on QuizParticipation
    print(f"{Fore.YELLOW}--- Solving Inconsistecies on Quiz Participation ---")
    if 'QuizParticipation' in df.columns:
        # Ensuring Numeric QuizParticipation
        df['QuizParticipation'] = pd.to_numeric(df['QuizParticipation'], errors='coerce')

        # Finding Neg QuizParticipation
        neg_index = df['QuizParticipation'] < 0

        # If negative QuizParticipation change it to nan
        if neg_index.sum() > 0 :
            df.loc[neg_index, 'QuizParticipation'] = np.nan

        # Finding QuizParticipation over the limit
        over_index = df['QuizParticipation'] > 100

        # IF over the limit values, change them to limit
        if over_index.sum() > 0:
            df.loc[over_index, 'QuizParticipation'] = 100

    # Test for Inconsistecies QuizParticipation solved
    assert (df['QuizParticipation'] < 0).sum() == 0 or (df['QuizParticipation'] > 100).sum() == 0, f"{Fore.RED}X X X ERROR: QuizParticipation Inconsistecies not solved! X X X"
    print(f"{Fore.GREEN}!!! Inconsistecies QuizParticipation solved !!!")

    # Solving Inconsistecies on PastPerformance
    print(f"{Fore.YELLOW}--- Solving Inconsistecies on Past Performance ---")
    if 'PastPerformance' in df.columns:
        # Ensuring Numeric PastPerformance
        df['PastPerformance'] = pd.to_numeric(df['PastPerformance'], errors='coerce')

        # Finding Neg PastPerformance
        neg_index = df['PastPerformance'] < 0

        # If negative PastPerformance change it to nan
        if neg_index.sum() > 0 :
            df.loc[neg_index, 'PastPerformance'] = np.nan

        # Finding PastPerformance over the limit
        over_index = df['PastPerformance'] > 100

        # IF over the limit values, change them to limit
        if over_index.sum() > 0:
            df.loc[over_index, 'PastPerformance'] = 100

    # Test for Inconsistecies PastPerformance solved
    assert (df['PastPerformance'] < 0).sum() == 0 or (df['PastPerformance'] > 100).sum() == 0, f"{Fore.RED}X X X ERROR: PastPerformance Inconsistecies not solved! X X X"
    print(f"{Fore.GREEN}!!! Inconsistecies PastPerformance solved !!!")

    # Solving Inconsistecies on CourseCompletion
    print(f"{Fore.YELLOW}--- Solving Inconsistecies on Course Completition ---")

    mapping = {
        'Yes': True, 'yes': True, 1: True, '1': True, True: True, 'true': True,'True': True,
        'No': False, 'no': False, 0: False, '0': False, False: False, 'false': False, 'False': False
    }

    df['CourseCompletion'] = df['CourseCompletion'].map(mapping)

    if df['CourseCompletion'].isnull().sum() > 0:
        index_to_drop = df[df['CourseCompletion'].isnull()].index

        #Check if there is any values to be deelted and print the info
        if not index_to_drop.empty:
            df.drop(index_to_drop, inplace=True)
            print(f"{Fore.GREEN}!!! Deleted {len(index_to_drop)} Values missing Course Completition !!!")

    # Test for Inconsistecies CourseCompletion solved
    assert set(df['CourseCompletion'].unique()) == {False, True}, f"{Fore.RED}X X X ERROR: CourseCompletion Inconsistecies not solved! X X X"
    print(f"{Fore.GREEN}!!! Inconsistecies Course Completion solved !!!")

    return df

def solve_missing(df):
    """
    Runs the function to solve missing values

    Args:
        df (pd.DataFrame): The DataFrame to be manipulated.
    
    Returns:
        pd.DataFrame or None: The manipulated DataFrame.
    """

    # Solving Missing ID
    print(f"{Fore.YELLOW}--- Adding missing IDs ---")
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

    # Solving Missing StudyHours
    print(f"{Fore.YELLOW}--- Adding mean to Study Hours ---")
    if df['StudyHours'].isnull().sum() > 0:

        missing_index = df[df['StudyHours'].isnull()].index
        df.loc[missing_index, 'StudyHours'] = df['StudyHours'].mean()
    else:
        print("--- No Missing Value Found! ---")

    # Test for missing StudyHours solved
    assert df['StudyHours'].isnull().sum() == 0, f"{Fore.RED}X X X ERROR: StudyHours missing values not solved! X X X"
    print(f"{Fore.GREEN}!!! Missing StudyHours solved !!!")

    # Solving Missing QuizParticipation and PastPerformance
    print(f"{Fore.YELLOW}--- Solving Past Performance and Quiz Participation ---")
    if df['QuizParticipation'].isnull().sum() > 0 or df['PastPerformance'].isnull().sum() > 0 :

        # Delete rows missing both past participaiton and quiz participation
        index_to_drop = df[ df['QuizParticipation'].isnull() & df['PastPerformance'].isnull()].index

        #Check if there is any values to be deelted and print the info
        if not index_to_drop.empty:
            df.drop(index_to_drop, inplace=True)
            print(f"{Fore.GREEN}!!! Deleted {len(index_to_drop)} Values missing Quiz Participation and Past Performance !!!")
        else:
            print(f"{Fore.YELLOW}--- No values deleted for missing Quiz Participation and Past Performance ---")

        # Now calculate a value based on Quiz Participation/Past Performance and replace it
        missing_participation_index = df[df['QuizParticipation'].isnull()].index

        participation_mean = df['QuizParticipation'].mean()

        missing_performance_index = df[df['PastPerformance'].isnull()].index
        
        performance_mean = df['PastPerformance'].mean()

        #Check is there is Quiz Participation values to be added and calculate them
        if not missing_participation_index.empty:
            result = df.loc[missing_participation_index, 'PastPerformance'] * participation_mean / performance_mean
            #Make sure doesnt go over the limit
            df.loc[missing_participation_index, 'QuizParticipation'] = result.clip(upper=100)
        
        #Check is there is PastPerformance values to be added and calculate them
        if not missing_performance_index.empty:
            result = df.loc[missing_performance_index, 'QuizParticipation'] * performance_mean / participation_mean
            #Make sure doesnt go over the limit
            df.loc[missing_performance_index, 'PastPerformance'] = result.clip(upper=100)    
    else:
        print("--- No Missing Values Found! ---")

    # Test for missing QuizParticipation and PastPerformance solved
    assert df['QuizParticipation'].isnull().sum() == 0, f"{Fore.RED}X X X ERROR: Quiz Participation missing values not solved! X X X"
    assert df['PastPerformance'].isnull().sum() == 0, f"{Fore.RED}X X X ERROR: Past Performance missing values not solved! X X X"
    print(f"{Fore.GREEN}!!! Missing Past Performance and Quiz Participation solved !!!")

    return df

def normalize_study_hours(df):
    """
    Runs the function to normilize study hours

    Args:
        df (pd.DataFrame): The DataFrame to be manipulated.
    
    Returns:
        pd.DataFrame or None: The manipulated DataFrame.
    """
        
    #Normalising StudyHours
    print(f"{Fore.YELLOW}--- Normalising Study Hours ---")
    if 'StudyHours' in df.columns:
        a=0
        df['StudyHours'] = df['StudyHours']/40

    # Test for Normalised StudyHours
    assert (df['StudyHours']>1).sum() == 0, f"{Fore.RED}X X X ERROR: Study Hours values not Normalised! X X X"
    print(f"{Fore.GREEN}!!! Study Hours values Normalised !!!")

    return df

# # Print the missing values
# print(f"\nMissing values after cleaning:\n{df.isnull().sum()}")

# # Print the inconsistencies
# print("Other Inconsistencies:")

# # Inconsistecies on Study Hours 
# if 'StudyHours' in df.columns:
#     num_perf = pd.to_numeric(df['StudyHours'], errors='coerce')
#     over_values = (num_perf > 40).sum()
#     if over_values > 0:
#         print(f" - Found {over_values} over the limit on StudyHours")
#     neg_values = (num_perf < 0).sum()
#     if neg_values > 0:
#         print(f" - Found {neg_values} negative values on StudyHours")

# # Inconsistecies on Quiz Participation 
# if 'QuizParticipation' in df.columns:
#     num_perf = pd.to_numeric(df['QuizParticipation'], errors='coerce')
#     over_values = (num_perf > 100).sum()
#     if over_values > 0:
#         print(f" - Found {over_values} over the limit on QuizParticipation")
#     neg_values = (num_perf < 0).sum()
#     if neg_values > 0:
#         print(f" - Found {neg_values} negative values on QuizParticipation")

# # Inconsistecies on Quiz Past Performance:
# if 'PastPerformance' in df.columns:
#     num_perf = pd.to_numeric(df['PastPerformance'], errors='coerce')
#     over_values = (num_perf > 100).sum()
#     if over_values > 0:
#         print(f" - Found {over_values} over the limit on PastPerformance")
#     neg_values = (num_perf < 0).sum()
#     if neg_values > 0:
#         print(f" - Found {neg_values} negative values on PastPerformance")

# # Inconsistecies on Course Completition:
# if 'CourseCompletion' in df.columns:
#     unique_values = df['CourseCompletion'].unique()

#     set_uniques = {str(val) for val in unique_values
#                    }
#     if set_uniques != {'False', 'True'}:
#         print(f" - Unique Values in CourseCompletion: {unique_values}")

def create_engagment_column(df):
    """
    Runs the function to create engagment column
    Args:
        df (pd.DataFrame): The DataFrame to be manipulated.
    
    Returns:
        pd.DataFrame or None: The manipulated DataFrame.
    """
    #Creating The Engagement Column
    print(f"{Fore.YELLOW}\n--- Creating Engagement Derived Column ---")

    #Define weights
    weight_study = 0.3
    weight_quiz = 0.7

    df['Engagement'] = (weight_study * df['StudyHours']) + (weight_quiz * df['QuizParticipation']/100)
    assert 'Engagement' in df.columns, f"{Fore.RED}X X X ERROR: Engagement Derived Column not Created! X X X"
    print(f"{Fore.GREEN}!!! Created Engagement Derived Column !!!")

    return df

def main():
    # Initialising Colorama, I like Colors, dont judge me!
    util.init_colors()

    # Try to load the dataset
    df = util.load_data('students_raw.csv')
    print_dataframe_info(df)
    solve_incosistencies(df)
    solve_missing(df)
    print_dataframe_info(df)
    normalize_study_hours(df)
    create_engagment_column(df)

    print(f"\n\n{Fore.YELLOW}--- Solving Dataset Issues ---")
    df = solve_incosistencies(df)


    # Save the cleaned data to a new file
    util.save_data(df,'students_clean.csv')

if __name__ == '__main__':
    main()

