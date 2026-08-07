import pytest
import os
from datetime import datetime

# Create reports directory if it doesn't exist
REPORTS_DIR = "reports"
if not os.path.exists(REPORTS_DIR):
    os.makedirs(REPORTS_DIR)

# Define test modules in sequential order
TEST_MODULES = [
    ("Login Tests", "tests/test_login.py"),
    ("Create User Tests", "tests/test_create_user_page.py"),
    ("Create Plan Tests", "tests/test_create_plan.py"),
    ("Dashboard Tests", "tests/test_dashboard.py"),
    ("Subscriptions Tests", "tests/test_subscriptions.py"),
]

def run_sequential_tests():
    """Run tests module by module sequentially"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    summary_file = os.path.join(REPORTS_DIR, f"test_summary_{timestamp}.txt")
    
    results = []
    
    print("\n" + "="*70)
    print("RUNNING TESTS SEQUENTIALLY")
    print("="*70 + "\n")
    
    for module_name, test_path in TEST_MODULES:
        print(f"\n{'='*70}")
        print(f"Running: {module_name}")
        print(f"Test File: {test_path}")
        print(f"{'='*70}\n")
        
        # Create report file for this module
        report_file = os.path.join(REPORTS_DIR, f"{module_name.replace(' ', '_').lower()}_{timestamp}.html")
        
        # Run pytest for this module
        exit_code = pytest.main([
            test_path,
            f"--html={report_file}",
            "--self-contained-html",
            "-v",
            "--tb=short"
        ])
        
        status = "✅ PASSED" if exit_code == 0 else "❌ FAILED"
        results.append({
            "module": module_name,
            "test_path": test_path,
            "status": status,
            "report": report_file,
            "exit_code": exit_code
        })
        
        print(f"\n{module_name}: {status}")
    
    # Print summary
    print("\n" + "="*70)
    print("TEST SUMMARY")
    print("="*70 + "\n")
    
    with open(summary_file, "w", encoding="utf-8") as f:
        f.write(f"Test Execution Summary - {datetime.now()}\n")
        f.write("="*70 + "\n\n")
        
        for result in results:
            status_display = "PASSED" if "PASSED" in result['status'] else "FAILED"
            print(f"{result['module']:.<40} {result['status']}")
            f.write(f"{result['module']:<40} {status_display}\n")
            f.write(f"  Report: {result['report']}\n\n")
    
    print("\n" + "="*70)
    print(f"Summary saved to: {summary_file}")
    print("="*70 + "\n")
    
    # Return exit code based on all results
    return 0 if all(r["exit_code"] == 0 for r in results) else 1

if __name__ == "__main__":
    exit_code = run_sequential_tests()
    exit(exit_code)
