import pandas as pd
import os
from colorama import Fore, init

def init_colors():
    """Initializes Colorama for cross-platform colored terminal text."""
    init(autoreset=True)
    print(f"{Fore.GREEN}Colorama initialized.")

def load_data(filename):
    """
    Loads a CSV file into a pandas DataFrame with error handling.
    
    Args:
        filename (str): The path to the CSV file.
        
    Returns:
        pd.DataFrame or None: The loaded DataFrame, or None if the file is not found.
    """
    try:
        df = pd.read_csv(filename)
        print(f"{"\033[38;5;46m"}Successfully loaded {filename}")
        return df
    except FileNotFoundError:
        print(f"{Fore.RED}ERROR: File not found. Make sure {filename} exists.")
        print(f"{Fore.RED}You may need to run the prerequisite Python script.")
        return None

def save_data(df, filename):
    """
    Saves a pandas DataFrame to a CSV file and verifies its creation.
    
    Args:
        df (pd.DataFrame): The DataFrame to save.
        filename (str): The desired output file path.
    """
    try:
        df.to_csv(filename, index=False)
        
        assert os.path.exists(filename), f"{Fore.RED}X X X ERROR: File {filename} not created! X X X"
        print(f"{"\033[38;5;46m"}!!! Successfully saved data to {filename} !!!")
        
    except Exception as e:
        print(f"{Fore.RED}An error occurred while saving {filename}: {e}")