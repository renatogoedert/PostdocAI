# main.py
# Main execution script for the Programming for AI CA.
# This script runs all parts of the project in sequence.

from script import student_data
from script import analysis
from script import part_3
from script import visualisation
from script.util import init_colors
from colorama import Fore
import time

def main():
    """
    Runs the complete data analysis pipeline from start to finish.
    """
    init_colors()
    print(f"{Fore.CYAN}{'='*40}")
    print(f"{Fore.CYAN}== NCI STUDENT ANALYSIS PIPELINE START ==")
    print(f"{Fore.CYAN}{'='*40}")
    
    # Part 1: Data Generation
    print(f"\n{Fore.GREEN}--- Executing Part 1: Data Generation ---")
    student_data.run_part1_generation()
    time.sleep(1) # Small pause
    
    # Part 2: Data Wrangling
    print(f"\n{Fore.GREEN}--- Executing Part 2: Data Wrangling ---")
    analysis.run_part2_wrangling()
    time.sleep(1)
    
    # Part 3: Data Analysis
    print(f"\n{Fore.GREEN}--- Executing Part 3: Data Analysis ---")
    part_3.run_part3_analysis()
    time.sleep(1)
    
    # Part 4: Data Visualisation
    print(f"\n{Fore.GREEN}--- Executing Part 4: Data Visualisation ---")
    visualisation.run_part4_visualisation()
    
    print(f"\n{Fore.CYAN}{'='*42}")
    print(f"{Fore.CYAN}== PIPELINE FINISHED SUCCESSFULLY (PLOTS) ==")
    print(f"{Fore.CYAN}{'='*42}")

if __name__ == "__main__":
    main()