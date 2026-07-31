"""Page objects for the WhizQuiz admin application."""

from pages.base_page import BasePage
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from pages.menu_page import MenuPage
from pages.user_page import UserPage, UsersPage

__all__ = [
    "BasePage",
    "DashboardPage",
    "LoginPage",
    "MenuPage",
    "UserPage",
    "UsersPage",
]