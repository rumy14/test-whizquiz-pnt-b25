"""Test Dashboard module functionality"""
import pytest
from pages.auth import LoginPage
from pages.dashboard import DashboardPage


class TestDashboard:
    """Dashboard page tests"""

    @pytest.fixture(autouse=True)
    def setup(self, page):
        """Setup test - login and navigate to dashboard"""
        login = LoginPage(page)
        login.goto_login()
        login.login("admin@gmail.com", "admin123")
        self.page = page
        self.dashboard = DashboardPage(page)

    def test_dashboard_loads(self):
        """Test dashboard page loads successfully"""
        assert self.dashboard.is_dashboard_loaded(), "Dashboard title not visible"

    def test_all_stats_cards_visible(self):
        """Test all statistics cards are displayed"""
        assert self.dashboard.verify_all_stats_visible(), "Not all stats cards are visible"

    def test_all_tables_visible(self):
        """Test all data tables are displayed"""
        assert self.dashboard.verify_all_tables_visible(), "Not all tables are visible"

    def test_active_users_count_displayed(self):
        """Test active users count is displayed"""
        count = self.dashboard.get_active_users_count()
        assert count is not None, "Active users count not found"
        assert count > 0, "Active users count should be > 0"
        assert count == 38, f"Expected 38 active users, got {count}"

    def test_paid_users_count_displayed(self):
        """Test paid users count is displayed"""
        count = self.dashboard.get_paid_users_count()
        assert count is not None, "Paid users count not found"
        assert count > 0, "Paid users count should be > 0"
        assert count == 39, f"Expected 39 paid users, got {count}"

    def test_active_quizzes_count_displayed(self):
        """Test active quizzes count is displayed"""
        count = self.dashboard.get_active_quizzes_count()
        assert count is not None, "Active quizzes count not found"
        assert count > 0, "Active quizzes count should be > 0"
        assert count == 26, f"Expected 26 active quizzes, got {count}"

    def test_participants_count_displayed(self):
        """Test participants count is displayed"""
        count = self.dashboard.get_participants_count()
        assert count is not None, "Participants count not found"
        assert count > 0, "Participants count should be > 0"
        assert count == 222, f"Expected 222 participants, got {count}"

    def test_recent_users_table_has_data(self):
        """Test recent users table contains data"""
        data = self.dashboard.get_recent_users_table_data()
        assert len(data) > 0, "Recent users table is empty"
        assert 'username' in data[0], "Username column not found"
        assert 'plan' in data[0], "Plan column not found"
        assert 'created_at' in data[0], "Created at column not found"

    def test_top_quizzes_table_has_data(self):
        """Test top quizzes table contains data"""
        data = self.dashboard.get_top_quizzes_table_data()
        assert len(data) > 0, "Top quizzes table is empty"
        assert 'quiz_name' in data[0], "Quiz name column not found"
        assert 'participants' in data[0], "Participants column not found"

    def test_recent_users_first_entry(self):
        """Test recent users table first entry is valid"""
        data = self.dashboard.get_recent_users_table_data()
        assert len(data) > 0, "No recent users found"
        first_user = data[0]
        assert first_user['username'], "Username is empty"
        assert first_user['plan'], "Plan is empty"

    def test_top_quizzes_first_entry(self):
        """Test top quizzes table first entry is valid"""
        data = self.dashboard.get_top_quizzes_table_data()
        assert len(data) > 0, "No top quizzes found"
        first_quiz = data[0]
        assert first_quiz['quiz_name'], "Quiz name is empty"
        assert first_quiz['participants'], "Participants is empty"

    def test_revenue_chart_visible(self):
        """Test revenue chart is displayed"""
        assert self.dashboard.is_visible(self.dashboard.REVENUE_CHART), "Revenue chart not visible"

    def test_select_revenue_period(self):
        """Test changing revenue period"""
        # This assumes the period selector updates the chart
        self.dashboard.select_revenue_period("Last Week")
        # Verify chart is still visible after period change
        assert self.dashboard.is_visible(self.dashboard.REVENUE_CHART), "Revenue chart not visible after period change"

    def test_dashboard_responsive_layout(self):
        """Test dashboard layout is responsive"""
        # Test that stats cards are visible in current viewport
        viewport_size = self.page.viewport_size
        assert viewport_size is not None, "Viewport size not available"
        assert self.dashboard.verify_all_stats_visible(), "Stats cards not visible in current viewport"
