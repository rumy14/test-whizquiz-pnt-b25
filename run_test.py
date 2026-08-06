import pytest
<<<<<<< HEAD
import os
from datetime import datetime

if __name__ == "__main__":
    # Create reports directory if it doesn't exist
    REPORTS_DIR = "reports"
    if not os.path.exists(REPORTS_DIR):
        os.makedirs(REPORTS_DIR)
    
    # Generate timestamped report filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_file = os.path.join(REPORTS_DIR, f"test_login_{timestamp}.html")
    
    pytest.main([
       "tests/test_login.py",
        #"tests/test_add_to_cart.py",
        #"tests/test_sorting_product.py",
        f"--html={report_file}",
        "--self-contained-html",
        "-v"
=======
from utils.artifacts import TEST_RESULTS_DIR


if __name__ == "__main__":
    TEST_RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    pytest.main([
   "tests",
       f"--html={TEST_RESULTS_DIR / 'report.html'}",
       "--self-contained-html",
       "-v"
>>>>>>> 77c80fd7483add4b1789892f2ed53b1cc4ecb958
    ])