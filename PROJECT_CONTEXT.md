# Chocolate Firm App - Project Context

## Project Overview

Chocolate Firm App is a Python-based prototype application developed for a Requirements Engineering school project.

The purpose of the application is to demonstrate how requirements can be translated into a working application using vibe-coding.

The application runs locally on a laptop and does not require cloud services or external databases.

All data is stored locally using JSON files.

The application should feel like a modern mobile application but runs as a desktop/web application using Flet.

---

# Technology Stack

Language:

* Python

Framework:

* Flet

Storage:

* JSON files

Version Control:

* Git
* GitHub

No external backend required.

---

# Design System

## Style

The application should have a clean, minimal and premium appearance inspired by modern consumer apps.

Design principles:

* Minimalistic
* Mobile-inspired
* Clean layout
* Consistent spacing
* Easy to navigate
* Professional appearance

---

## Color Palette

Primary Brown:
#6F4E37

Secondary Light Brown:
#C8A27A

Cream Background:
#F7F3EE

White:
#FFFFFF

Dark Text:
#2F2F2F

Success:
#4CAF50

Warning:
#FF9800

Error:
#F44336

---

## UI Rules

* Rounded corners
* Soft shadows
* Modern cards
* Large whitespace
* Consistent margins
* Consistent padding
* Mobile inspired layout
* Maximum content width around 450px
* Modern icons
* Responsive design

---

# Navigation

Bottom Navigation:

1. Home
2. Scan
3. Assistant
4. Shop
5. Profile

---

# Authentication

The application contains a local login system.

Users must log in before accessing the application.

Acceptance Criteria:

* User enters email
* User enters password
* Credentials are validated against users.json
* Invalid credentials show an error
* Successful login opens Home screen
* User remains logged in during the session
* User can log out from Profile screen

Demo Account:

Email:
[atakan@example.com](mailto:atakan@example.com)

Password:
demo123

---

# Screens

## Login

Purpose:

Authenticate users before entering the application.

Components:

* Email field
* Password field
* Login button
* Error message

---

## Home

Purpose:

Provide a dashboard overview.

Components:

* Welcome message
* Registered products
* Recommended products
* Recent notifications

---

## Scan

Purpose:

Allow users to register products.

Components:

* Product code input
* Scan button
* Product information
* Register product button

Note:

Real QR scanning is not required.

A product code input field is sufficient.

---

## Product Detail

Purpose:

Display detailed information about a product.

Components:

* Product image
* Product name
* Description
* Ingredients
* Allergens
* Origin
* Expiry date

---

## Assistant

Purpose:

Provide support through a chatbot.

Components:

* Chat messages
* Message input
* Send button

The chatbot may use predefined responses.

No real AI integration required.

---

## Shop

Purpose:

Allow users to browse products.

Components:

* Product cards
* Product details
* Add to cart
* Shopping cart
* Order confirmation

No real payment system required.

---

## Profile

Purpose:

Manage personal information.

Components:

* Personal information
* Preferences
* Allergies
* Registered products
* Complaints
* Notifications
* Logout button

---

## Complaints

Purpose:

Allow users to register complaints.

Components:

* Complaint title
* Complaint description
* Complaint category
* Complaint status

Statuses:

* Received
* In Progress
* Resolved

---

# Functional Requirements

## Product Registration

As a customer I want to register a chocolate product so I can track product information.

Acceptance Criteria:

* Product code can be entered
* Product exists in products.json
* Product information is displayed
* Product can be registered
* Product appears in My Products

---

## Product Overview

As a customer I want to see my registered products.

Acceptance Criteria:

* Products are displayed
* Expiry date is displayed
* Product details can be opened

---

## Product Recommendations

As a customer I want recommendations based on my preferences.

Acceptance Criteria:

* Recommended products are displayed
* Recommendations appear on Home screen

---

## Complaints

As a customer I want to submit complaints.

Acceptance Criteria:

* Complaint can be created
* Complaint is stored
* Complaint status is visible

---

## Complaint Tracking

As a customer I want to track complaint status.

Acceptance Criteria:

* Complaint overview available
* Status visible

---

## Assistant

As a customer I want help from a chatbot.

Acceptance Criteria:

* Message can be sent
* Response is returned

---

## Shop

As a customer I want to order products.

Acceptance Criteria:

* Products visible
* Add to cart available
* Order confirmation available

---

## Profile Management

As a customer I want to manage my profile.

Acceptance Criteria:

* Personal information editable
* Preferences editable
* Allergies editable
* Changes saved

---

## Notifications

As a customer I want to receive updates.

Acceptance Criteria:

* Notifications visible
* Notifications linked to actions

---

# Data Storage

Data Folder:

data/

Files:

users.json
profiles.json
products.json
registered_products.json
complaints.json
notifications.json
orders.json
chat_messages.json

---

# Data Model

## User

{
"id": 1,
"name": "Atakan",
"email": "[atakan@example.com](mailto:atakan@example.com)",
"password": "demo123",
"role": "customer",
"created_at": "2026-01-01"
}

---

## Profile

{
"user_id": 1,
"favorite_chocolate_types": ["Milk", "Hazelnut"],
"allergies": ["Nuts"],
"notification_enabled": true
}

---

## Product

{
"id": 1,
"code": "CHOCO001",
"name": "Milk Chocolate",
"description": "Creamy milk chocolate bar",
"category": "Milk",
"origin": "Belgium",
"ingredients": ["Cocoa", "Milk", "Sugar"],
"allergens": ["Milk"],
"expiry_date": "2026-12-31",
"price": 2.99,
"image": "assets/milk_chocolate.png"
}

---

## Registered Product

{
"id": 1,
"user_id": 1,
"product_id": 1,
"registered_date": "2026-01-15"
}

---

## Complaint

{
"id": 1,
"user_id": 1,
"product_id": 1,
"title": "Damaged Packaging",
"description": "Packaging was torn",
"category": "Packaging",
"status": "In Progress",
"created_at": "2026-01-20"
}

---

## Notification

{
"id": 1,
"user_id": 1,
"title": "Complaint Updated",
"message": "Your complaint is now in progress",
"is_read": false
}

---

## Order

{
"id": 1,
"user_id": 1,
"status": "Confirmed",
"total_price": 5.98
}

---

## Chat Message

{
"id": 1,
"user_id": 1,
"sender": "user",
"message": "Where can I find allergen information?"
}

---

# Development Rules

* Keep code simple and readable.
* Focus on requirement validation.
* Use local JSON files.
* No database required.
* No cloud deployment required.
* Prioritize functionality over complexity.
* Build reusable components where possible.
* Ensure every requirement can be demonstrated during the final presentation.
