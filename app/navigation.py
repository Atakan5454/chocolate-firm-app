"""
Navigation System
Manages screen navigation in the application.
"""

from enum import Enum
from typing import Callable, Dict


class Screen(Enum):
    """Screen identifiers."""
    LOGIN = "login"
    HOME = "home"
    SCAN = "scan"
    ASSISTANT = "assistant"
    SHOP = "shop"
    PROFILE = "profile"


class NavigationManager:
    """Manages navigation between screens."""
    
    def __init__(self):
        """Initialize navigation manager."""
        self._screen_builders: Dict[Screen, Callable] = {}
        self._current_screen: Screen = Screen.LOGIN
        self._on_navigation_change: Callable = None
    
    def register_screen(self, screen: Screen, builder: Callable) -> None:
        """
        Register a screen builder.
        
        Args:
            screen: Screen identifier
            builder: Callable that returns the screen content
        """
        self._screen_builders[screen] = builder
    
    def navigate_to(self, screen: Screen) -> None:
        """
        Navigate to a screen.
        
        Args:
            screen: Target screen identifier
        """
        if screen in self._screen_builders:
            self._current_screen = screen
            if self._on_navigation_change:
                self._on_navigation_change(screen)
        else:
            raise ValueError(f"Screen {screen} not registered")
    
    def get_current_screen(self) -> Screen:
        """Get current screen identifier."""
        return self._current_screen
    
    def build_current_screen(self) -> any:
        """Build and return current screen content."""
        if self._current_screen in self._screen_builders:
            return self._screen_builders[self._current_screen]()
        return None
    
    def set_on_navigation_change(self, callback: Callable) -> None:
        """
        Set callback for navigation changes.
        
        Args:
            callback: Function called when navigation changes
        """
        self._on_navigation_change = callback

