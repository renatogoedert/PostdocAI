# Code developed by Renato Francisco Goedert
# Sutudent Number: x25115766

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
    student_data.main()
    time.sleep(1)
    print(f"\nPart 2 Running in 3 sec, press Ctrl+D to stop")
    time.sleep(1)
    print(f"Part 2 Running in 2 sec, press Ctrl+D to stop")
    time.sleep(1)
    print(f"Part 2 Running in 1 sec, press Ctrl+D to stop")
    time.sleep(1)

    # Part 2: Data Wrangling
    print(f"\n{Fore.GREEN}--- Executing Part 2: Data Wrangling ---")
    analysis.main()
    time.sleep(1)
    print(f"\nPart 3 Running in 3 sec, press Ctrl+D to stop")
    time.sleep(1)
    print(f"Part 3 Running in 2 sec, press Ctrl+D to stop")
    time.sleep(1)
    print(f"Part 3 Running in 1 sec, press Ctrl+D to stop")
    time.sleep(1)
    
    # Part 3: Data Analysis
    print(f"\n{Fore.GREEN}--- Executing Part 3: Data Analysis ---")
    part_3.main()
    time.sleep(1)
    print(f"\nPart 4 Running in 3 sec, press Ctrl+D to stop")
    time.sleep(1)
    print(f"Part 4 Running in 2 sec, press Ctrl+D to stop")
    time.sleep(1)
    print(f"Part 4 Running in 1 sec, press Ctrl+D to stop")
    time.sleep(1)
    
    # Part 4: Data Visualisation
    print(f"\n{Fore.GREEN}--- Executing Part 4: Data Visualisation ---")
    visualisation.main()
    
    print(f"\n{Fore.CYAN}{'='*42}")
    print(f"{Fore.CYAN}== PIPELINE FINISHED SUCCESSFULLY (PLOTS) ==")
    print(f"{Fore.CYAN}{'='*42}")

if __name__ == "__main__":
    main()