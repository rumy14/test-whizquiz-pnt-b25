"""Page objects for the WhizQuiz admin application."""

from pages.base_page import BasePage
from pages.auth import LoginPage
from pages.dashboard import DashboardPage
from pages.menu import MenuPage
from pages.users import UserPage, UsersPage

__all__ = [
    "BasePage",
    "DashboardPage",
    "LoginPage",
    "MenuPage",
    "UserPage",
    "UsersPage",
]