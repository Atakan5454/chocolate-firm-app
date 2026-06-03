import flet as ft


def main(page: ft.Page):
    page.title = "Chocolate Firm App"
    page.add(
        ft.Text("Chocolate Firm App werkt!", size=28, weight=ft.FontWeight.BOLD),
        ft.Text("Flet is succesvol gestart.")
    )


ft.app(target=main)