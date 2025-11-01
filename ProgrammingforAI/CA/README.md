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

The project was designed to emphasize its simplicity, without overengineering, while also promoting principles like reusability, in addition to considering a user-friendly experience. With that in mind, a procedural/functional structure was chosen; however, instead of demanding for a user to run multiple Python scripts, a central orchestrator (main.py) was added to the system design. This orchestrator script abstracts the entire worflow on a single pipeline, ensuring that all functions and scripts run in the right sequece of exucation, from data/file creation through to plotting in PNG, furthermore it includes robust concepts like ```try/catch``` blocks to terminate the program gracefully in case of an interruption. This main orchestrator can be accessed by:

```
python main.py
```

In order to secure the project's proper reliability, a dedicated Python package housing all core modules for the implementation of the solution was designed. This package, by the name "scripts," contained the core modules, the ```__init__.py``` empty file (as required by Python packaging conventions) and also a ```util.py``` module. This Utilities module embodies the functions that were otherwise repeated multiple times across the core modules, such as initiating colorama and reading or saving files. In addition, it aligns with the DRY (Don't Repeat Yourself) principle, which states, "Every piece of knowledge must have a single, unambiguous, authoritative representation within a system." [1]

Following the designed architecture, there are the core modules that cover each stage of the CA implementation. These modules were organized by multiple private functions and a ```main()``` function that abstracts the execution of the module by coordinating each “step function”. At the very bottom of the module is the name-main idiom (```if __name__ == "__main__":```) to avoid the main() function being run when the module is imported. Moreover, the “Step Functions” were made private (prefixed by an underscore), thereby respecting the principle of encapsulation. The modules also include multiple ```print()``` statements to inform the user about the stages and ```asserts``` statements to make sure that the script is running smoothly. 


![main() function example](./images/main%20func.png)


# Insights from Data Visualisation

# Reflection

several challenges were reaised during the creating of this project, and solved with creativity and knowledge, showing how important this caracteristics are for the scientsts and their academic/working life