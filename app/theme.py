"""
Theme Configuration
Centralized theme and styling rules for the entire application.
"""

class Colors:
    """Application color palette."""
    
    # Primary Colors
    PRIMARY_BROWN = "#6F4E37"
    SECONDARY_LIGHT_BROWN = "#C8A27A"
    
    # Background
    CREAM_BACKGROUND = "#F7F3EE"
    WHITE = "#FFFFFF"
    
    # Text
    DARK_TEXT = "#2F2F2F"
    LIGHT_TEXT = "#757575"
    
    # States
    SUCCESS = "#4CAF50"
    WARNING = "#FF9800"
    ERROR = "#F44336"
    
    # Additional
    LIGHT_GRAY = "#F5F5F5"
    BORDER_GRAY = "#E0E0E0"


class Spacing:
    """Consistent spacing values."""
    
    XS = 4
    S = 8
    M = 16
    L = 24
    XL = 32
    XXL = 48


class BorderRadius:
    """Consistent border radius values."""
    
    SMALL = 8
    MEDIUM = 12
    LARGE = 16
    EXTRA_LARGE = 20


class Typography:
    """Typography configuration."""
    
    # Font family
    FONT_FAMILY = "Segoe UI, -apple-system, BlinkMacSystemFont, sans-serif"
    
    # Font sizes
    HEADING_1 = 32
    HEADING_2 = 24
    HEADING_3 = 20
    BODY_LARGE = 16
    BODY_MEDIUM = 14
    BODY_SMALL = 12
    CAPTION = 10
    
    # Font weights (Flet uses bold parameter instead)
    BOLD = True
    NORMAL = False


class Shadows:
    """Shadow configuration for cards and containers."""
    
    # Soft shadow for elevated elements
    ELEVATION_1 = {
        "blur_radius": 2,
        "spread_radius": 1,
        "blur_x": 0,
        "blur_y": 2,
    }
    
    ELEVATION_2 = {
        "blur_radius": 4,
        "spread_radius": 1,
        "blur_x": 0,
        "blur_y": 4,
    }


class Dimensions:
    """Application dimensions."""
    
    # Content width constraints
    MAX_CONTENT_WIDTH = 450
    MIN_CONTENT_WIDTH = 320
    
    # Component heights
    BUTTON_HEIGHT = 48
    INPUT_HEIGHT = 48
    CARD_MIN_HEIGHT = 120
    BOTTOM_NAV_HEIGHT = 64


class StylingRules:
    """Common styling rules and patterns."""
    
    def get_card_style():
        """Returns styling for card components."""
        return {
            "bgcolor": Colors.WHITE,
            "border_radius": BorderRadius.LARGE,
            "padding": Spacing.M,
            "shadow": Shadows.ELEVATION_1,
        }
    
    def get_button_style():
        """Returns styling for primary buttons."""
        return {
            "height": Dimensions.BUTTON_HEIGHT,
            "bgcolor": Colors.PRIMARY_BROWN,
            "color": Colors.WHITE,
            "border_radius": BorderRadius.MEDIUM,
        }
    
    def get_input_style():
        """Returns styling for input fields."""
        return {
            "height": Dimensions.INPUT_HEIGHT,
            "bgcolor": Colors.LIGHT_GRAY,
            "border_color": Colors.BORDER_GRAY,
            "border_radius": BorderRadius.MEDIUM,
        }

