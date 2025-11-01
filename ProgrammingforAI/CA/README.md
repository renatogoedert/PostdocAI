# Introduction

This report is developed as part of the Continuous Assessment for Programming for Artificial Intelligence (PGDAI_SEP25), it oulines the design, implementation and analyse of a python program that simulates the analyses of student behaviors. The implementation of the project was divided into four main stages:

1. Data Generation: Task to create a CSV file (students_raw.csv) with 500 rows and noise.

2. Data Wrangling: Task to clean and transforms the raw data, creating a clean CSV file (students_clean.csv).

3. Data Analysis: Task to perform analysis by filtering and grouping the data, as well using functional programming.

4. Data Visualisation: Task to creates plots on PNG format.

This report focus on the Reflection and reporting part, where is descreptive show the processes strategies used to design the solution not forgoting the challenges and lessons learned during execution.

## Libraries used

- NUmpy
- pandas
- seaborn
- matplotlib.pyplot
- colorama
- time


# Project Structure

The project was designed to emphasize its simplicity, without overengineering, while also promoting principles like reusability, in addition to considering a user-friendly experience. With that in mind, a procedural/functional structure was chosen; however, instead of demanding for a user to run multiple Python scripts, a central orchestrator (main.py) was added to the system design. This orchestrator script abstracts the entire worflow on a single pipeline, ensuring that all functions and scripts run in the right sequece of exucation, from data/file creation through to plotting in PNG, furthermore it includes robust concepts like ```try/catch``` blocks to terminate the program gracefully in case of an interruption. This main orchestrator can be accessed by:

```
python main.py
```

to better organization a Package was created, the script package, in order to inform python thta a folder is a package the ```__init__.py``` empty file was created, this allows to the folder the read as a package. Thinking of the reusualibity and readability of the solution, an util module was developed, this contains the initiate colorama, as the read files and save csv and png to the right place, this approach aims to if any fix or alteration need to be made, there isnt a need to go to every script and change the same thing over and over again

A module for each stage of the CA was developed, this was made to keep an easy inspection as to separate pasts as good pratices, they all are organize in functions and have a ```main()``` function wich will run all respective functions in order, in all these main modules a ```if __name__ == "__main__":``` was added in order to avoid the scripts run when imported to the main.py orchstrator


```
CA/
│
├── main.py               <-- Orchestrator
│
├── script/               <-- Package
│   ├── __init__.py       <-- Makes 'script' a Python package
│   ├── student_data.py   <-- Part 1: Data Generation
│   ├── analysis.py       <-- Part 2: Data Wrangling
│   ├── part_3.py         <-- Part 3: Data Analysis
│   ├── visualisation.py  <-- Part 4: Data Visualisation
│   └── util.py           <-- Utility functions (load/save, etc.)
│
├── (generated files)
│   ├── students_raw.csv
│   ├── students_clean.csv
│   └── ... (plots as .png)
```

# Insights from Data Visualisation

# Reflection

several challenges were reaised during the creating of this project, and solved with creativity and knowledge, showing how important this caracteristics are for the scientsts and their academic/working life