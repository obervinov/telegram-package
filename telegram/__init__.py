"""
This is just a special file that tells pip that your main module is in this folder
No need to add anything here. Feel free to delete this line when you make your own package
Leave it empty
"""
# flake8: noqa
from .telegram import TelegramBot

__all__ = ["TelegramBot"]
