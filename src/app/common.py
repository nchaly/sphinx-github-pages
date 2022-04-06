from typing import Optional


def common_function_01():
    """Does nothing without any external arguments."""
    pass


def common_function_02(name: str, label: Optional[str] = None):
    """Does nothing but that's ok."""
    pass


class UserData:
    """Stores user data"""
    def __init__(self, name: str):
        self.name = name

    def say_hi(self):
        """Says hi."""
        print(f'Hi from {self.name}.')
