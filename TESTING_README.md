# Testing Guide

## Report Structure
All test reports are now stored in the `reports/` folder with timestamped filenames.

- **reports/** - Contains all test report files
  - `login_tests_*.html` - Login module test reports
  - `create_user_tests_*.html` - User creation module test reports
  - `create_plan_tests_*.html` - Plan creation module test reports
  - `dashboard_tests_*.html` - Dashboard module test reports
  - `test_summary_*.txt` - Summary of all test runs

## Running Tests

### Option 1: Run All Tests Sequentially (Recommended)
Run each test module one by one with individual reports:

```bash
python run_tests_sequential.py
```

This will:
- Run Login Tests → Create User Tests → Create Plan Tests → Dashboard Tests
- Generate individual HTML reports for each module
- Create a summary file with overall results
- Save all reports to `reports/` folder with timestamps

### Option 2: Run Single Module
Run only the login test module:

```bash
python run_test.py
```

This generates a timestamped report in the `reports/` folder.

### Option 3: Run Specific Test Using Pytest
```bash
.venv\Scripts\python.exe -m pytest tests/test_login.py -v
```

## Report Files

Reports are automatically timestamped in format: `module_name_YYYYMMDD_HHMMSS.html`

Example:
```
reports/
├── login_tests_20260804_141758.html
├── create_user_tests_20260804_141758.html
├── create_plan_tests_20260804_141758.html
├── dashboard_tests_20260804_141758.html
└── test_summary_20260804_141758.txt
```

## Test Modules

| Module | Test File | Status |
|--------|-----------|--------|
| Login | `tests/test_login.py` | ✅ Passing |
| Create User | `tests/test_create_user_page.py` | ⏳ In Progress |
| Create Plan | `tests/test_create_plan.py` | ⏳ In Progress |
| Dashboard | `tests/test_dashboard.py` | ⏳ Needs Fixes |

## Debugging Failed Tests

1. **Check the HTML Report** - Open `reports/module_name_*.html` in browser
2. **View Console Output** - Run the sequential test runner to see detailed error messages
3. **Check Page Objects** - Verify import paths in test files match actual page file locations

## Fixing Import Errors

All page imports should follow the pattern:
```python
from pages.{category}.{page_name} import ClassName
```

Example:
```python
from pages.auth.login_page import LoginPage
from pages.inventory.inventory_page import InventoryPage
from pages.plans.create_plan_page import CreatePlanPage
```

## Adding New Tests

1. Create test file in `tests/` folder: `test_module_name.py`
2. Add correct imports with proper paths
3. Add module to `TEST_MODULES` list in `run_tests_sequential.py`:
   ```python
   TEST_MODULES = [
       ("Module Name", "tests/test_module_name.py"),
       # ... other modules
   ]
   ```
4. Run sequential tests to include your new module

---

**Last Updated:** 2026-08-04
