import pytest

if __name__ == "__main__":
    pytest.main([
       "tests/test_login.py",
       "tests/test_menu.py",
       "tests/test_user.py",
       #"tests/test_add_to_cart.py",
       #"tests/test_sorting_product.py",
       "--html=report.html",
       "--self-contained-html",
       "-v"
    ])