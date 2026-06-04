"""
Application Configuration
Global settings and constants for the application.
"""

# Application Info
APP_NAME = "Chocolate Firm App"
APP_VERSION = "1.0.0"
APP_DESCRIPTION = "Premium chocolate product tracking and assistance application"

# Window Configuration
WINDOW_WIDTH = 450
WINDOW_HEIGHT = 800
WINDOW_RESIZABLE = False

# Data Storage
DATA_DIRECTORY = "data"

# JSON Files
DATA_FILES = {
    "USERS": "users.json",
    "PROFILES": "profiles.json",
    "PRODUCTS": "products.json",
    "REGISTERED_PRODUCTS": "registered_products.json",
    "COMPLAINTS": "complaints.json",
    "NOTIFICATIONS": "notifications.json",
    "ORDERS": "orders.json",
    "CHAT_MESSAGES": "chat_messages.json",
}

# Application States
class AppState:
    """Application state constants."""
    AUTHENTICATED = "authenticated"
    UNAUTHENTICATED = "unauthenticated"
    LOADING = "loading"

# User Roles
class UserRole:
    """User role constants."""
    CUSTOMER = "customer"
    ADMIN = "admin"

# Complaint Statuses
class ComplaintStatus:
    """Complaint status constants."""
    RECEIVED = "Received"
    IN_PROGRESS = "In Progress"
    RESOLVED = "Resolved"

# Order Statuses
class OrderStatus:
    """Order status constants."""
    PENDING = "Pending"
    CONFIRMED = "Confirmed"
    SHIPPED = "Shipped"
    DELIVERED = "Delivered"

# Chat Message Senders
class ChatSender:
    """Chat message sender constants."""
    USER = "user"
    ASSISTANT = "assistant"

# Notification Types
class NotificationType:
    """Notification type constants."""
    COMPLAINT_UPDATE = "complaint_update"
    PRODUCT_AVAILABLE = "product_available"
    NEW_RECOMMENDATION = "new_recommendation"
    ORDER_UPDATE = "order_update"

