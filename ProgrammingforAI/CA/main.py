# Code developed by Renato Francisco Goedert
# Sutudent Number: x25115766

from script import student_data
from script import wrangling
from script import analysis
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

adding # Run pipeline on entry option
def run_pipeline(option):

    # Just Generation
    if option == "1":
        student_data.main()

    # Just Wrangling
    elif option == "2":
        wrangling.main()

    # Just Analysis
    elif option == "3":
        analysis.main()

    # Just Visualisation
    elif option == "4":
        visualisation.main()

    # Just Generation and Wrangling
    elif option == "5":
        student_data.main()
        countdown('Part 2')
        wrangling.main()

    # Just Analysis and Visualisation
    elif option == "6":
        analysis.main()
        countdown('Part 4')
        visualisation.main()

    # All parts
    elif option == "0":
        student_data.main()
        countdown('Part 2')
        wrangling.main()
        countdown('Part 3')
        analysis.main()
        countdown('Part 4')
        visualisation.main()
    
    else:
        print(f"{Fore.RED}Invalid option, please try again.")

def main():
    """
    Runs the complete data analysis pipeline from start to finish.
    """
    try:
        init_colors()
        print(f"{Fore.LIGHTBLUE_EX}{'='*51}")
        print(f"{Fore.LIGHTBLUE_EX}== NCI STUDENT x25115766 ANALYSIS PIPELINE START ==")
        print(f"{Fore.LIGHTBLUE_EX}{'='*51}")
        
        while True:
            print(f"{Fore.CYAN}Choose which part(s) to run:")
            print(f"{Fore.YELLOW}[1] Part 1: Data Generation")
            print(f"{Fore.YELLOW}[2] Part 2: Data Wrangling")
            print(f"{Fore.YELLOW}[3] Part 3: Data Analysis")
            print(f"{Fore.YELLOW}[4] Part 4: Data Visualisation")
            print(f"{Fore.YELLOW}[5] Run Parts 1 and 2")
            print(f"{Fore.YELLOW}[6] Run Parts 3 and 4")
            print(f"{Fore.YELLOW}[0] Run All Parts")
            print(f"{Fore.YELLOW}[exit] Exit Program\n")

            choice = input(f"{Fore.CYAN}Enter your choice: ").strip().lower()
            if choice == "exit":
                print(f"\n{Fore.LIGHTBLUE_EX}Exiting program. Goodbye!\n")
                break
            run_pipeline(choice)
        
        print(f"\n{Fore.LIGHTBLUE_EX}{'='*44}")
        print(f"{Fore.LIGHTBLUE_EX}== PIPELINE FINISHED SUCCESSFULLY (PLOTS) ==")
        print(f"{Fore.LIGHTBLUE_EX}{'='*44}")
    
    except KeyboardInterrupt:
        print(f"\n{Fore.LIGHTRED_EX}{'='*40}")
        print(f"{Fore.LIGHTRED_EX}===== PIPELINE INTERRUPTED BY USER =====")
        print(f"{Fore.LIGHTRED_EX}{'='*40}")


if __name__ == "__main__":
    main()