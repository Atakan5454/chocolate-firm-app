"""
Data Models
Defines data structures for the application.
"""

from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime


@dataclass
class User:
    """User model."""
    id: int
    name: str
    email: str
    password: str
    role: str = "customer"
    created_at: str = field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d"))


@dataclass
class UserProfile:
    """User profile model."""
    user_id: int
    favorite_chocolate_types: List[str] = field(default_factory=list)
    allergies: List[str] = field(default_factory=list)
    notification_enabled: bool = True


@dataclass
class Product:
    """Product model."""
    id: int
    code: str
    name: str
    description: str
    category: str
    origin: str
    ingredients: List[str]
    allergens: List[str]
    expiry_date: str
    price: float
    image: Optional[str] = None


@dataclass
class RegisteredProduct:
    """Registered product model (user's registered products)."""
    id: int
    user_id: int
    product_id: int
    registered_date: str = field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d"))


@dataclass
class Complaint:
    """Complaint model."""
    id: int
    user_id: int
    product_id: int
    title: str
    description: str
    category: str
    status: str  # "Received", "In Progress", "Resolved"
    created_at: str = field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d"))


@dataclass
class Notification:
    """Notification model."""
    id: int
    user_id: int
    title: str
    message: str
    is_read: bool = False
    created_at: str = field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d"))


@dataclass
class Order:
    """Order model."""
    id: int
    user_id: int
    status: str  # "Pending", "Confirmed", "Shipped"
    total_price: float
    created_at: str = field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d"))


@dataclass
class ChatMessage:
    """Chat message model."""
    id: int
    user_id: int
    sender: str  # "user" or "assistant"
    message: str
    created_at: str = field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d"))

