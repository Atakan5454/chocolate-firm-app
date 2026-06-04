"""
Main Application
Chocolate Firm App - Entry point and main controller.
"""

import flet as ft
from app.theme import Colors, Spacing, Dimensions
from app.navigation import NavigationManager, Screen
from app.services import (
    StorageService,
    AuthService,
    ProductService,
    RegisteredProductService,
    ComplaintService,
    NotificationService,
    ChatService,
    ProfileService
)
from app.screens import (
    LoginScreen,
    HomeScreen,
    ScanScreen,
    AssistantScreen,
    ShopScreen,
    ProfileScreen
)


class ChocolateFirmApp:
    """Main application controller."""
    
    def __init__(self, page: ft.Page):
        """
        Initialize the application.
        
        Args:
            page: Flet page instance
        """
        self.page = page
        self.page.title = "Chocolate Firm App"
        self.page.window_width = 450
        self.page.window_height = 800
        self.page.bgcolor = Colors.CREAM_BACKGROUND
        
        # Initialize services
        self.storage_service = StorageService("data")
        self.auth_service = AuthService(self.storage_service)
        self.product_service = ProductService(self.storage_service)
        self.registered_product_service = RegisteredProductService(self.storage_service)
        self.complaint_service = ComplaintService(self.storage_service)
        self.notification_service = NotificationService(self.storage_service)
        self.chat_service = ChatService(self.storage_service)
        self.profile_service = ProfileService(self.storage_service)
        
        # Initialize navigation
        self.nav_manager = NavigationManager()
        
        # Register screens BEFORE building UI (screens must be registered before navigation)
        self._register_screens()
        
        # Build UI
        self._build_ui()
    
    def _build_ui(self):
        """Build main UI layout."""
        # Main content area
        self.main_content = ft.Container(
            expand=True,
            bgcolor=Colors.CREAM_BACKGROUND
        )
        
        # Bottom navigation bar
        self.bottom_nav = ft.NavigationBar(
            on_change=self._on_nav_change,
            destinations=[
                ft.NavigationBarDestination(icon=ft.Icons.HOME, label="Home"),
                ft.NavigationBarDestination(icon=ft.Icons.QR_CODE, label="Scan"),
                ft.NavigationBarDestination(icon=ft.Icons.CHAT, label="Assistant"),
                ft.NavigationBarDestination(icon=ft.Icons.SHOPPING_CART, label="Shop"),
                ft.NavigationBarDestination(icon=ft.Icons.PERSON, label="Profile"),
            ],
            bgcolor=Colors.WHITE,
            selected_index=0,
            height=Dimensions.BOTTOM_NAV_HEIGHT
        )
        
        # Main layout
        self.page.add(
            ft.Column(
                [
                    self.main_content,
                    self.bottom_nav
                ],
                spacing=0,
                expand=True
            )
        )
        
        # Navigate to login initially
        self.nav_manager.navigate_to(Screen.LOGIN)
    
    def _register_screens(self):
        """Register all screens with navigation manager."""
        self.nav_manager.register_screen(
            Screen.LOGIN,
            lambda: LoginScreen(
                auth_service=self.auth_service,
                on_login_success=self._on_login_success
            )
        )
        
        self.nav_manager.register_screen(
            Screen.HOME,
            lambda: HomeScreen()
        )
        
        self.nav_manager.register_screen(
            Screen.SCAN,
            lambda: ScanScreen()
        )
        
        self.nav_manager.register_screen(
            Screen.ASSISTANT,
            lambda: AssistantScreen()
        )
        
        self.nav_manager.register_screen(
            Screen.SHOP,
            lambda: ShopScreen()
        )
        
        self.nav_manager.register_screen(
            Screen.PROFILE,
            lambda: ProfileScreen(on_logout=self._on_logout)
        )
        
        self.nav_manager.set_on_navigation_change(self._on_navigation_change)
    
    def _on_navigation_change(self, screen: Screen):
        """Handle screen navigation change."""
        # Don't show nav bar on login
        if screen == Screen.LOGIN:
            self.bottom_nav.visible = False
        else:
            self.bottom_nav.visible = True
        
        # Update main content
        self.main_content.content = self.nav_manager.build_current_screen()
        self.page.update()
    
    def _on_nav_change(self, e):
        """Handle bottom navigation change."""
        selected_index = self.bottom_nav.selected_index
        
        screen_map = [
            Screen.HOME,
            Screen.SCAN,
            Screen.ASSISTANT,
            Screen.SHOP,
            Screen.PROFILE
        ]
        
        if 0 <= selected_index < len(screen_map):
            self.nav_manager.navigate_to(screen_map[selected_index])
    
    def _on_login_success(self):
        """Handle successful login."""
        self.nav_manager.navigate_to(Screen.HOME)
    
    def _on_logout(self):
        """Handle logout."""
        self.auth_service.logout()
        self.bottom_nav.selected_index = 0
        self.nav_manager.navigate_to(Screen.LOGIN)


def main(page: ft.Page):
    """Application entry point."""
    app = ChocolateFirmApp(page)


if __name__ == "__main__":
    ft.app(target=main)

