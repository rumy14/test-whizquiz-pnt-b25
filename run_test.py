import pytest
from utils.artifacts import TEST_RESULTS_DIR


if __name__ == "__main__":
    TEST_RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    pytest.main([
   "tests",
       f"--html={TEST_RESULTS_DIR / 'report.html'}",
       "--self-contained-html",
       "-v"
    ])