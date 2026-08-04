import pytest
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
    ])