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

The project was design for simplisity and reusability, as not a very complex with several diferent scirpts to organize, with that in mid a procedural/functional structure was used, with that in mind, but also taking into consideration the User Experience wehn using the program, intead of ordering the user to run several scripts a orchstrator was developed (main.py), this orchstrator script is responsable to run all modules in the right order, it also has a try,except in order to make shure that in case of keyinteruption it would close grafully, making easy to re use and to be run for any user, in order to run all from file creating to plot run:

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