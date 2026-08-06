from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent
PLAYWRIGHT_REPORT_DIR = PROJECT_ROOT / "playwright-report"
TEST_RESULTS_DIR = PROJECT_ROOT / "test-results"
SCREENSHOTS_DIR = TEST_RESULTS_DIR / "screenshots"


def screenshot_path(name: str) -> str:
    """Return a stable path for a named test screenshot."""
    SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)
    return str(SCREENSHOTS_DIR / f"{name}.png")