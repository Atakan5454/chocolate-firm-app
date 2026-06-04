"""
Chocolate Firm App - Entry Point
Production-quality Flet application for chocolate firm.
"""

import flet as ft
from app.main_app import main


if __name__ == "__main__":
    ft.app(target=main)
