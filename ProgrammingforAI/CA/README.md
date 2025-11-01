# Introduction

This report is developed as part of the Continuous Assessment for Programming for Artificial Intelligence (PGDAI_SEP25), it oulines the design, implementation and analyse of a python program that simulates the analyses of student behaviors. This project is divided into four main stages:

1 - Data Generation: Creates a CSV file (students_raw.csv) containing both purely random and stochastic (procedurally generated) values. It also introduces noise (missing values, inconsistencies) to simulate a real-world dataset.

2 - Data Wrangling: Cleans and transforms the raw data by handling missing values and inconsistencies, creating a clean CSV file (students_clean.csv).

- 3 Data Analysis: Performs analysis by filtering and grouping the data, as well as creating new categorical columns using functional programming (lambda functions).

Data Visualisation: Creates plots from the analysis and saves them to PNG format.

The project ends with a reflection on the development process, including challenges, design choices, and key lessons learned.

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

