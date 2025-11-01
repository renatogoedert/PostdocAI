# Introduction


# Project Structure

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

