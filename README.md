# ISM3232 Midterm: Harvest Table Catering

- **Name:** Alyxandria Gibson
- **Version:** 1.0.0
- **Date:** 10/25/2026

## What This Program Does
This program acts as an automated business and logic reporting engine for Harvest Table Catering. It calculates food costs, applies tiered guest discounts, determines service fees, and checks management and second-chef requirements. Finally, it processes event logs to create a clean and formatted terminal summary report.

## Business Rules
Rule 1. Food cost is calculated by multiplying the price per guest by the number of guests.

Rule 2. Events with fewer than 25 guests receive no discount. Events with 25-99 guests receive a 5% discount. Events with 100 guests or more receive a 5% discount.

Rule 3. Events with 100 or more guests only receive a 12% discount if they are nonprofit events, they receive a 5% discount if not.

Rule 4. A $75 service fee is added when the discounted food costs $500 or less.

Rule 5. Events with a total cost greater than $2,500 requires a manager sign-off.

Rule 6. A second chef is required when an event has more than 80 guests or a total cost of at least $3,000.

## How to Run
```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 main.py
```

## How to Test
```
ruff format . && ruff check . && pytest -v
```
There are 25 tests written in tests/test_business_rules.py which covers all eight functions and boundary conditions.

## Files in This Repository
business_rules.py : Contains the eight functions used to calculate costs, apply rules, summarize events, and format event information.

main.py : Runs the catering report and prints the results.

commands.md : Records terminal commands and their outputs, as well as a project setup history log.

README.md : Explains the project, business rules, setup, testing, and an AI use statement.

requirements.txt : Lists the project dependencies (pytest and ruff).

.gitignore : Lists files and folders that Git excludes, such as virtual environments and Python cache files.

tests/__init__.py : Marks the tests directory as a Python package.

tests/test_business_rules.py : Contains the 25 automated tests for the business rules and functions.

## AI Use Statement
I did not use AI on this exam.