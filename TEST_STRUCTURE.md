# Test Structure & Organization Guide

## 📁 Project Directory Structure

```
test-whizquiz-pnt-b25/
├── config/
│   ├── __pycache__/
│   └── base_config.py           # Configuration (BASE_URL, TIMEOUT)
├── pages/
│   ├── __pycache__/
│   ├── base_page.py             # Base class for all pages
│   ├── login_page.py            # Login page object
│   ├── inventory_page.py        # Inventory/Dashboard page object
│   ├── dashboard_page.py        # Dashboard with menu navigation
│   ├── menu_page.py             # Menu management page
│   └── user_page.py             # User management page
├── tests/
│   ├── test_login.py            # Login test cases
│   ├── test_menu.py             # Menu management test cases
│   └── test_user.py             # User management test cases
├── run_test.py                  # Main test runner
└── report.html                  # Test execution report (generated)
```

## 📋 Test Files & Test Cases

### 1. **test_login.py** - Authentication Tests
- `test_valid_login()` - Validates admin login with correct credentials

### 2. **test_menu.py** - Menu Management Tests
- `test_create_menu()` - Creates a new menu and verifies success
- `test_view_dashboard_menus()` - Views dashboard and lists all available menus

### 3. **test_user.py** - User Management Tests
- `test_create_user()` - Creates a single new user
- `test_create_multiple_users()` - Creates multiple users in sequence

## 🎯 Page Object Classes

### BasePage
- Base class for all pages
- Methods: `navigate()`, `get_title()`

### LoginPage
- Selectors: EMAIL_INPUT, PASSWORD_INPUT, SIGN_IN_BUTTON, ERROR_MESSAGE
- Methods: `login()`, `get_error_message()`

### DashboardPage
- Selectors: DASHBOARD_TITLE, MENU_BUTTON, USER_MENU
- Methods: `is_logged_in()`, `get_dashboard_title()`, `click_menu()`, `get_all_menu_items()`

### MenuPage
- Selectors: ADD_MENU_BUTTON, MENU_NAME_INPUT, MENU_TABLE
- Methods: `create_menu()`, `is_menu_created_successfully()`, `search_menu()`

### UserPage
- Selectors: ADD_USER_BUTTON, USER_EMAIL_INPUT, USER_ROLE_SELECT
- Methods: `create_user()`, `is_user_created_successfully()`, `search_user()`

## 🚀 Running Tests

**Run all tests with HTML report:**
```bash
python run_test.py
```

**Run specific test file:**
```bash
pytest tests/test_menu.py -v --html=report.html --self-contained-html
```

**Run specific test:**
```bash
pytest tests/test_user.py::test_create_user -v --html=report.html
```

## 📊 Report Generation
- HTML report: `report.html`
- Screenshots: `test_*.png` (generated in project root)

## ✅ Dashboard Menu Navigation
After login, the dashboard displays menu items that can be accessed:
- Click on menu items using: `dashboard_page.click_menu("Menu Name")`
- View all menus using: `dashboard_page.get_all_menu_items()`

## 🔍 Where to Add New Tests
1. Create new test file in `tests/` directory: `tests/test_feature_name.py`
2. Create corresponding page object in `pages/` directory if needed
3. Import and add test file path to `run_test.py`
4. Run tests: `python run_test.py`
