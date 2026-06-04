"""
Application Constants
Constants and enumerations used throughout the application.
"""

from enum import Enum


class Screen(str, Enum):
    """Screen identifiers."""
    LOGIN = "login"
    HOME = "home"
    SCAN = "scan"
    ASSISTANT = "assistant"
    SHOP = "shop"
    PROFILE = "profile"


class ComplaintStatus(str, Enum):
    """Complaint status values."""
    RECEIVED = "Received"
    IN_PROGRESS = "In Progress"
    RESOLVED = "Resolved"


class OrderStatus(str, Enum):
    """Order status values."""
    PENDING = "Pending"
    CONFIRMED = "Confirmed"
    SHIPPED = "Shipped"
    DELIVERED = "Delivered"


class ChatSender(str, Enum):
    """Chat message sender types."""
    USER = "user"
    ASSISTANT = "assistant"


class UserRole(str, Enum):
    """User role types."""
    CUSTOMER = "customer"
    ADMIN = "admin"


# Chocolate Categories
CHOCOLATE_CATEGORIES = [
    "Milk",
    "Dark",
    "White",
    "Hazelnut",
    "Almond",
    "Mixed"
]

# Common Allergens
COMMON_ALLERGENS = [
    "Milk",
    "Nuts",
    "Peanuts",
    "Gluten",
    "Soy",
    "Sesame"
]

# Complaint Categories
COMPLAINT_CATEGORIES = [
    "Damaged Packaging",
    "Taste Issue",
    "Quality Issue",
    "Delivery Issue",
    "Allergen Concern",
    "Other"
]

# Message Strings (for easy localization later)
MESSAGES = {
    # Errors
    "INVALID_EMAIL": "Please enter a valid email address.",
    "INVALID_PASSWORD": "Password must be at least 6 characters.",
    "INVALID_CREDENTIALS": "Invalid email or password.",
    "USER_NOT_FOUND": "User not found.",
    "PRODUCT_NOT_FOUND": "Product not found.",
    "INTERNAL_ERROR": "An internal error occurred. Please try again.",
    
    # Success
    "LOGIN_SUCCESS": "Login successful.",
    "LOGOUT_SUCCESS": "Logged out successfully.",
    "PRODUCT_REGISTERED": "Product registered successfully.",
    "COMPLAINT_SUBMITTED": "Complaint submitted successfully.",
    "PROFILE_UPDATED": "Profile updated successfully.",
    
    # Info
    "NO_PRODUCTS": "No products available.",
    "NO_COMPLAINTS": "No complaints yet.",
    "NO_NOTIFICATIONS": "No notifications.",
    "LOADING": "Loading...",
}

# Icon Mappings
ICON_MAP = {
    "home": "home",
    "scan": "qr_code_2",
    "assistant": "smart_toy",
    "shop": "shopping_cart",
    "profile": "person",
    "product": "shopping_bag",
    "complaint": "warning",
    "notification": "notifications",
    "settings": "settings",
    "logout": "logout",
}

