# Code developed by Renato Francisco Goedert
# Sutudent Number: x25115766

from script import student_data
from script import analysis
from script import part_3
from script import visualisation
from script.util import init_colors
from colorama import Fore
import time

def countdown(part_name, seconds=3):
    """
    Displays the countdown
    """
    # Add a line space
    print()
    time.sleep(1)
    for i in range(seconds, 0 , -1):
        #Adding /r to recursive printing
        print(f"Running {part_name} in {i} sec... (Press Ctrl+C to cancel)", end="\r")
        time.sleep(1)
    #Adding empty line with recursive to remove countdown
    print(" " * 100, end="\r")

def main():
    """
    Runs the complete data analysis pipeline from start to finish.
    """
    try:
        init_colors()
        print(f"{Fore.LIGHTBLUE_EX}{'='*51}")
        print(f"{Fore.LIGHTBLUE_EX}== NCI STUDENT x25115766 ANALYSIS PIPELINE START ==")
        print(f"{Fore.LIGHTBLUE_EX}{'='*51}")
        
        # Part 1: Data Generation
        print(f"\n{Fore.CYAN}--- Executing Part 1: Data Generation ---")
        student_data.main()
        countdown('Part 2')

        # Part 2: Data Wrangling
        print(f"\n{Fore.CYAN}--- Executing Part 2: Data Wrangling ---")
        analysis.main()
        countdown('Part 3')
        
        # Part 3: Data Analysis
        print(f"\n{Fore.CYAN}--- Executing Part 3: Data Analysis ---")
        part_3.main()
        countdown('Part 4')
        
        # Part 4: Data Visualisation
        print(f"\n{Fore.CYAN}--- Executing Part 4: Data Visualisation ---")
        visualisation.main()
        
        print(f"\n{Fore.LIGHTBLUE_EX}{'='*44}")
        print(f"{Fore.LIGHTBLUE_EX}== PIPELINE FINISHED SUCCESSFULLY (PLOTS) ==")
        print(f"{Fore.LIGHTBLUE_EX}{'='*44}")
    
    except KeyboardInterrupt:
        print(f"\n{Fore.LIGHTRED_EX}{'='*40}")
        print(f"{Fore.LIGHTRED_EX}===== PIPELINE INTERRUPTED BY USER =====")
        print(f"{Fore.LIGHTRED_EX}{'='*40}")


if __name__ == "__main__":
    main()