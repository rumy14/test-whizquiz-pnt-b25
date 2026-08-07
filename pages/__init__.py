<<<<<<< HEAD
"""Page objects for QuizWhiz application"""
from .base_page import BasePage

__all__ = ["BasePage"]
=======
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
>>>>>>> 77c80fd7483add4b1789892f2ed53b1cc4ecb958
