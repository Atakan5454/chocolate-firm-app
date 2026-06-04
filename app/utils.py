"""
Utility Functions
Helper functions for common operations.
"""

from datetime import datetime
from typing import Optional, List


class DateUtils:
    """Date and time utility functions."""
    
    @staticmethod
    def get_today() -> str:
        """Get today's date as string (YYYY-MM-DD)."""
        return datetime.now().strftime("%Y-%m-%d")
    
    @staticmethod
    def get_current_datetime() -> str:
        """Get current date and time as string."""
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    @staticmethod
    def format_date(date_string: str, format_str: str = "%d/%m/%Y") -> str:
        """
        Format date string.
        
        Args:
            date_string: Date string in YYYY-MM-DD format
            format_str: Output format string
            
        Returns:
            Formatted date string
        """
        try:
            date_obj = datetime.strptime(date_string, "%Y-%m-%d")
            return date_obj.strftime(format_str)
        except ValueError:
            return date_string
    
    @staticmethod
    def is_date_expired(expiry_date: str) -> bool:
        """
        Check if date is in the past.
        
        Args:
            expiry_date: Date string in YYYY-MM-DD format
            
        Returns:
            True if date is in the past
        """
        try:
            expiry = datetime.strptime(expiry_date, "%Y-%m-%d")
            return expiry < datetime.now()
        except ValueError:
            return False
    
    @staticmethod
    def days_until_expiry(expiry_date: str) -> Optional[int]:
        """
        Calculate days until expiry date.
        
        Args:
            expiry_date: Date string in YYYY-MM-DD format
            
        Returns:
            Number of days until expiry, or None if invalid
        """
        try:
            expiry = datetime.strptime(expiry_date, "%Y-%m-%d")
            days = (expiry - datetime.now()).days
            return days
        except ValueError:
            return None


class StringUtils:
    """String utility functions."""
    
    @staticmethod
    def truncate(text: str, max_length: int = 50) -> str:
        """
        Truncate text to maximum length.
        
        Args:
            text: Text to truncate
            max_length: Maximum length
            
        Returns:
            Truncated text with ellipsis if needed
        """
        if len(text) > max_length:
            return text[:max_length - 3] + "..."
        return text
    
    @staticmethod
    def is_valid_email(email: str) -> bool:
        """
        Validate email format.
        
        Args:
            email: Email string
            
        Returns:
            True if email format is valid
        """
        import re
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    
    @staticmethod
    def capitalize_words(text: str) -> str:
        """Capitalize first letter of each word."""
        return ' '.join(word.capitalize() for word in text.split())


class ValidationUtils:
    """Validation utility functions."""
    
    @staticmethod
    def is_not_empty(value: str) -> bool:
        """Check if string is not empty."""
        return value is not None and value.strip() != ""
    
    @staticmethod
    def is_valid_password(password: str, min_length: int = 6) -> bool:
        """
        Validate password.
        
        Args:
            password: Password string
            min_length: Minimum password length
            
        Returns:
            True if password is valid
        """
        return password is not None and len(password) >= min_length
    
    @staticmethod
    def has_required_fields(data: dict, required_fields: List[str]) -> bool:
        """
        Check if dictionary has all required fields.
        
        Args:
            data: Dictionary to check
            required_fields: List of required field names
            
        Returns:
            True if all required fields are present
        """
        return all(field in data and data[field] is not None for field in required_fields)


class FormatUtils:
    """Format utility functions."""
    
    @staticmethod
    def format_price(price: float, currency: str = "$") -> str:
        """
        Format price for display.
        
        Args:
            price: Price amount
            currency: Currency symbol
            
        Returns:
            Formatted price string
        """
        return f"{currency}{price:.2f}"
    
    @staticmethod
    def format_list(items: List[str], separator: str = ", ") -> str:
        """
        Format list as string.
        
        Args:
            items: List of strings
            separator: Item separator
            
        Returns:
            Formatted string
        """
        return separator.join(items)
    
    @staticmethod
    def format_product_code(code: str) -> str:
        """Format product code for display."""
        return code.upper()

