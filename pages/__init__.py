"""Page objects for the WhizQuiz admin application."""

from .base_page import BasePage
from .auth import LoginPage
from .dashboard import DashboardPage
from .menu import MenuPage
from .users import UserPage, UsersPage

__all__ = [
    "BasePage",
    "DashboardPage",
    "LoginPage",
    "MenuPage",
    "UserPage",
    "UsersPage",
]
