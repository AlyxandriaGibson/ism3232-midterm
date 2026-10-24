# Terminal Record: Harvest Table Catering

## 1. Building the Project
```
cd ~
pwd
mkdir ism3232-midterm
cd ism3232-midterm
git init
git branch -M main
git status
pwd
python3 -m venv .venv
source .venv/bin/activate
which python3
pip install pytest ruff && pip freeze > requirements.txt
echo '.venv/' > .gitignore && echo '__pycache__/' >> .gitignore
touch business_rules.py
touch main.py
touch commands.md
touch README.md
mkdir -p tests && touch tests/__init__.py tests/test_business_rules.py
tree -L 2
ls -la
git status
ruff format . && ruff check . && pytest -v
git add . && git commit -m 'Part 1 of Midterm Practical Exam: Project setup and structure.' && git push
git push --set-upstream origin main
```

## 2. The virtual environment
```
which python3
```

```
/home/agibson159/ism3232-midterm/.venv/bin/python3
```

## 3. The project structure
```
tree -L 2
```

```
.
├── README.md
├── __pycache__
│   └── business_rules.cpython-314.pyc
├── business_rules.py
├── commands.md
├── main.py
├── requirements.txt
└── tests
    ├── __init__.py
    ├── __pycache__
    └── test_business_rules.py
```

One folder that is in my computer but not in my GitHub repository would be the .venv folder, which is not in my Github repository because it is listed in .gitignore.

## 4. Every function and test
```
rg 'def '
```

```
business_rules.py
16:def calculate_food_cost(guest_price: float, guests: int) -> float:
21:def get_event_discount(guests: int, nonprofit: bool = False) -> float:
31:def calculate_event_total(
43:def needs_signoff(total: float) -> bool:
48:def needs_second_chef(guests: int, total: float) -> bool:
53:def total_booked(events: list) -> float:
63:def largest_event(events: list) -> str:
77:def format_event_line(

tests/test_business_rules.py
13:def test_calculate_food_cost():
17:def test_calculate_food_costs_zero_guests():
21:def test_discount_below_25_guests():
25:def test_discount_at_25_guests():
29:def test_discount_at_99_guests():
33:def test_discount_at_100_guests():
37:def test_nonprofit_gets_12_percent_discount():
41:def test_nonprofit_changes_discount():
45:def test_event_total_no_discount():
49:def test_event_total_nonprofit_discount():
53:def test_service_fee_at_500_discount_cost():
57:def test_no_service_fee_above_500_discount_cost():
61:def test_signoff_over_2500():
65:def test_signoff_below_2500():
69:def test_signoff_at_2500():
73:def test_second_chef_above_80_guests():
77:def test_no_second_chef_at_80_guests():
81:def test_second_chef_at_3000_total():
85:def test_no_second_chef_below_3000_total():
89:def test_total_booked_short_list():
97:def test_largest_event_short_list():
105:def test_largest_event_tie_returns_first_client():
113:def test_largest_event_empty_list():
117:def test_format_event_line_without_requirements():
122:def test_format_event_line_with_requirements():
```

In rg 'def ' business_rules.py defines 8 functions, and tests/test_business_rules.py defines 25 tests.

## 5. Which files print
```
rg -l 'print'
```

```
main.py
```

main.py is the only file that prints because it executes the catering report generation loop, whereas business_rules.py only defines functions and returns values with no print function inside.

## 6. The commit history
```
git log --oneline
```

```
4426fa9 (HEAD -> main, origin/main) Finalization of Part 4: Implementation of the total_booked, largest_event, and format_event_line tests in tests/test_business_rules.py
2f4944a Addition to Part 4: Implementation of the second chef rules in tests/test_business_rules.py
db18a7a Addition to Part 4: Implementation of the needs signoff tests in tests/test_business_rules.py
0b015ae Addition to Part 4: Implementation of the event total calculation tests in tests/test_business_rules.py
773cbdb Creation of Part 4: Addition of food cost tests and event discount tests in tests/test_business_rules.py.
9ed2afe Creation of Part 3: Fix some business_rules errors and creation/completion of main.py, ensuring it matches the given output exactly.
8ec2f42 Creation of Part 2: Creating eight functions in business_rules.py.
af21106 Part 1 of Midterm Practical Exam: Project setup and structure.
```

There have been 8 commits at this point.