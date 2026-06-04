import json
from pathlib import Path
from datetime import date, datetime
import flet as ft

PRIMARY = "#6F4E37"
SECONDARY = "#C8A27A"
BACKGROUND = "#F7F3EE"
WHITE = "#FFFFFF"
TEXT = "#565656"
MUTED_TEXT = "#565656"
ERROR = "#C62828"
SUCCESS = "#2E7D32"
WARNING = "#FF9800"

DATA_DIR = Path("data")
USERS_FILE = DATA_DIR / "users.json"
PRODUCTS_FILE = DATA_DIR / "products.json"
REGISTERED_FILE = DATA_DIR / "registered_products.json"
COMPLAINTS_FILE = DATA_DIR / "complaints.json"
ORDERS_FILE = DATA_DIR / "orders.json"
NOTIFICATIONS_FILE = DATA_DIR / "notifications.json"

PHONE_WIDTH = 390
PHONE_HEIGHT = 760


def load_json(path):
    if not path.exists():
        return []
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def save_json(path, data):
    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)


def txt(value, size=13, color=TEXT, weight=None):
    return ft.Text(value, size=size, color=color, weight=weight)


def make_card(content):
    return ft.Container(
        content=content,
        bgcolor=WHITE,
        border_radius=18,
        padding=16,
        margin=8,
        shadow=ft.BoxShadow(
            blur_radius=10,
            spread_radius=1,
            color="#22000000",
            offset=ft.Offset(0, 3),
        ),
    )


def days_until_expiry(expiry_date):
    try:
        expiry = datetime.strptime(expiry_date, "%Y-%m-%d").date()
        return (expiry - date.today()).days
    except Exception:
        return None


def main(page: ft.Page):
    page.title = "Chocolate Firm App"
    page.bgcolor = "#D8C3AA"
    page.window_width = 470
    page.window_height = 850
    page.window_resizable = False
    page.padding = 0

    state = {
        "user": None,
        "screen": "login",
        "selected_product": None,
        "cart": [],
    }

    def add_notification(user_id, message):
        notifications = load_json(NOTIFICATIONS_FILE)
        notifications.append(
            {
                "id": len(notifications) + 1,
                "user_id": user_id,
                "message": message,
                "date": str(date.today()),
                "is_read": False,
            }
        )
        save_json(NOTIFICATIONS_FILE, notifications)

    def render_phone(content, show_nav=True):
        page.controls.clear()

        phone_content = ft.Column(
            controls=[
                ft.Container(content=content, expand=True, padding=18),
                bottom_nav() if show_nav else ft.Container(),
            ],
            expand=True,
        )

        phone_frame = ft.Container(
            width=PHONE_WIDTH,
            height=PHONE_HEIGHT,
            bgcolor=BACKGROUND,
            border_radius=32,
            padding=0,
            clip_behavior=ft.ClipBehavior.HARD_EDGE,
            content=phone_content,
            shadow=ft.BoxShadow(
                blur_radius=24,
                spread_radius=2,
                color="#33000000",
                offset=ft.Offset(0, 8),
            ),
        )

        page.add(
            ft.Row(
                controls=[phone_frame],
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                expand=True,
            )
        )
        page.update()

    def bottom_nav():
        items = [
            ("home", "🏠", "Home"),
            ("scan", "📷", "Scan"),
            ("assistant", "🤖", "Assistent"),
            ("shop", "🛍️", "Shop"),
            ("profile", "👤", "Profiel"),
        ]

        nav_items = []

        for key, icon, label in items:
            active = state["screen"] == key
            nav_items.append(
                ft.Container(
                    expand=True,
                    content=ft.TextButton(
                        content=ft.Column(
                            controls=[
                                ft.Text(icon, size=18),
                                ft.Text(
                                    label,
                                    size=9,
                                    color=PRIMARY if active else MUTED_TEXT,
                                ),
                            ],
                            spacing=1,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                        on_click=lambda e, k=key: navigate(k),
                    ),
                )
            )

        return ft.Container(
            bgcolor=WHITE,
            height=72,
            padding=4,
            content=ft.Row(
                controls=nav_items,
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
            ),
        )

    def navigate(screen):
        state["screen"] = screen

        if screen == "home":
            show_home()
        elif screen == "scan":
            show_scan()
        elif screen == "assistant":
            show_assistant()
        elif screen == "shop":
            show_shop()
        elif screen == "profile":
            show_profile()
        elif screen == "complaints":
            show_complaints()
        elif screen == "edit_profile":
            show_edit_profile()

    def show_login():
        email = ft.TextField(label="Email", border_radius=14, bgcolor=WHITE)
        password = ft.TextField(
            label="Wachtwoord",
            password=True,
            can_reveal_password=True,
            border_radius=14,
            bgcolor=WHITE,
        )

        error_text = ft.Text("", color=ERROR, size=13)

        def login(e):
            users = load_json(USERS_FILE)

            for user in users:
                if user["email"] == email.value and user["password"] == password.value:
                    state["user"] = user
                    state["screen"] = "home"
                    show_home()
                    return

            error_text.value = "Onjuiste email of wachtwoord."
            page.update()

        content = ft.Column(
            controls=[
                ft.Container(height=60),
                ft.Text("🍫", size=64),
                ft.Text(
                    "Chocolate Firm",
                    size=30,
                    weight=ft.FontWeight.BOLD,
                    color=PRIMARY,
                ),
                txt("Jouw persoonlijke chocolade-app", size=14),
                ft.Container(height=22),
                email,
                password,
                error_text,
                ft.ElevatedButton(
                    "Inloggen",
                    bgcolor=PRIMARY,
                    color=WHITE,
                    height=48,
                    width=330,
                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=16)),
                    on_click=login,
                ),
                ft.TextButton(
                    "Nog geen account? Account aanmaken",
                    on_click=lambda e: show_register(),
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=12,
        )

        render_phone(content, show_nav=False)

    def show_register():
        name = ft.TextField(label="Naam", border_radius=14, bgcolor=WHITE)
        email = ft.TextField(label="Email", border_radius=14, bgcolor=WHITE)
        password = ft.TextField(
            label="Wachtwoord",
            password=True,
            can_reveal_password=True,
            border_radius=14,
            bgcolor=WHITE,
        )

        message = ft.Text("", size=13)

        def create_account(e):
            if not name.value or not email.value or not password.value:
                message.value = "Vul alle velden in."
                message.color = ERROR
                page.update()
                return

            users = load_json(USERS_FILE)

            if any(user["email"] == email.value for user in users):
                message.value = "Er bestaat al een account met dit emailadres."
                message.color = ERROR
                page.update()
                return

            new_user = {
                "id": len(users) + 1,
                "name": name.value,
                "email": email.value,
                "password": password.value,
                "favorite_chocolate": "",
                "allergies": "",
                "notifications_enabled": True,
            }

            users.append(new_user)
            save_json(USERS_FILE, users)

            add_notification(new_user["id"], "Welkom bij Chocolate Firm.")

            state["user"] = new_user
            state["screen"] = "home"
            show_home()

        content = ft.Column(
            controls=[
                ft.Container(height=50),
                ft.Text("🍫", size=58),
                ft.Text(
                    "Account aanmaken",
                    size=28,
                    weight=ft.FontWeight.BOLD,
                    color=PRIMARY,
                ),
                txt("Maak een persoonlijk Chocolate Firm account.", size=14),
                ft.Container(height=18),
                name,
                email,
                password,
                message,
                ft.ElevatedButton(
                    "Account aanmaken",
                    bgcolor=PRIMARY,
                    color=WHITE,
                    height=48,
                    width=330,
                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=16)),
                    on_click=create_account,
                ),
                ft.TextButton(
                    "Ik heb al een account",
                    on_click=lambda e: show_login(),
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=12,
        )

        render_phone(content, show_nav=False)

    def show_home():
        user = state["user"]
        products = load_json(PRODUCTS_FILE)
        registered = load_json(REGISTERED_FILE)
        complaints = load_json(COMPLAINTS_FILE)
        orders = load_json(ORDERS_FILE)
        notifications = load_json(NOTIFICATIONS_FILE)

        my_product_cards = []

        for item in registered:
            if item.get("user_id") == user["id"]:
                product = next((p for p in products if p["id"] == item["product_id"]), None)
                if product:
                    expiry_text = []
                    if product.get("expiry_date"):
                        expiry_text.append(txt(f"Houdbaar tot: {product['expiry_date']}"))

                        days_left = days_until_expiry(product["expiry_date"])
                        if days_left is not None and days_left <= 30:
                            expiry_text.append(
                                txt("⚠ Verloopt binnenkort", color=WARNING, weight=ft.FontWeight.BOLD)
                            )

                    my_product_cards.append(
                        make_card(
                            ft.Column(
                                controls=[
                                    txt(
                                        f"🍫 {product['name']}",
                                        size=16,
                                        weight=ft.FontWeight.BOLD,
                                        color=PRIMARY,
                                    ),
                                    txt(f"Herkomst: {product['origin']}"),
                                    txt(f"Geregistreerd: {item['registered_date']}"),
                                    *expiry_text,
                                ],
                                spacing=6,
                            )
                        )
                    )

        if not my_product_cards:
            my_product_cards.append(
                make_card(txt("Je hebt nog geen producten geregistreerd. Scan je eerste product."))
            )

        user_complaints = [c for c in complaints if c.get("user_id") == user["id"]]
        user_orders = [o for o in orders if o.get("user_id") == user["id"]]
        user_notifications = [
            n for n in notifications if n.get("user_id") == user["id"]
        ][-3:]

        notification_controls = []
        if not user_notifications:
            notification_controls.append(txt("Je hebt nog geen meldingen."))
        else:
            for notification in reversed(user_notifications):
                notification_controls.append(
                    txt(f"🔔 {notification['message']} ({notification['date']})")
                )

        recommended_product = products[1] if len(products) > 1 else None

        content = ft.Column(
            controls=[
                ft.Text(
                    f"Hallo {user['name']} 👋",
                    size=25,
                    weight=ft.FontWeight.BOLD,
                    color=PRIMARY,
                ),
                txt("Welkom terug bij Chocolate Firm.", size=14),
                ft.Container(height=10),
                txt("Mijn producten", size=19, weight=ft.FontWeight.BOLD),
                *my_product_cards,
                txt("Aanbevolen voor jou", size=19, weight=ft.FontWeight.BOLD),
                make_card(
                    ft.Column(
                        controls=[
                            txt(
                                f"✨ {recommended_product['name'] if recommended_product else 'Hazelnut Chocolate'}",
                                size=16,
                                weight=ft.FontWeight.BOLD,
                                color=PRIMARY,
                            ),
                            txt("Een smaakvolle keuze op basis van jouw voorkeuren."),
                            txt(f"€{recommended_product['price'] if recommended_product else '3.49'}"),
                        ],
                        spacing=6,
                    )
                ),
                txt("Recente meldingen", size=19, weight=ft.FontWeight.BOLD),
                make_card(ft.Column(controls=notification_controls, spacing=4)),
                txt("Overzicht", size=19, weight=ft.FontWeight.BOLD),
                make_card(
                    ft.Column(
                        controls=[
                            txt(f"🛍️ Bestellingen geplaatst: {len(user_orders)}"),
                            txt(f"📝 Ingediende klachten: {len(user_complaints)}"),
                            txt("🤖 De assistent staat klaar om je te helpen."),
                        ],
                        spacing=4,
                    )
                ),
            ],
            spacing=6,
            scroll=ft.ScrollMode.AUTO,
        )

        render_phone(content)

    def show_scan():
        code_input = ft.TextField(
            label="Productcode",
            hint_text="Bijvoorbeeld CHOCO001",
            border_radius=14,
            bgcolor=WHITE,
        )

        result_area = ft.Column(spacing=6)
        message = ft.Text("", size=13)

        def register_product(e):
            user = state["user"]
            product = state["selected_product"]

            registered = load_json(REGISTERED_FILE)

            already_exists = any(
                item["user_id"] == user["id"] and item["product_id"] == product["id"]
                for item in registered
            )

            if already_exists:
                message.value = "Dit product is al geregistreerd."
                message.color = ERROR
                page.update()
                return

            registered.append(
                {
                    "id": len(registered) + 1,
                    "user_id": user["id"],
                    "product_id": product["id"],
                    "registered_date": str(date.today()),
                }
            )

            save_json(REGISTERED_FILE, registered)
            add_notification(user["id"], f"{product['name']} is toegevoegd aan jouw producten.")

            message.value = "Product succesvol geregistreerd."
            message.color = SUCCESS
            page.update()

        def search_product(e):
            products = load_json(PRODUCTS_FILE)
            search_code = code_input.value.strip().upper()

            product = next((p for p in products if p["code"].upper() == search_code), None)
            result_area.controls.clear()

            if not product:
                message.value = "Product niet gevonden."
                message.color = ERROR
                page.update()
                return

            state["selected_product"] = product
            message.value = "Product gevonden."
            message.color = SUCCESS

            product_controls = [
                txt(
                    f"🍫 {product['name']}",
                    size=20,
                    weight=ft.FontWeight.BOLD,
                    color=PRIMARY,
                ),
                txt(f"Code: {product['code']}"),
                txt(f"Herkomst: {product['origin']}"),
                txt(f"Prijs: €{product['price']}"),
            ]

            if "description" in product:
                product_controls.append(txt(f"Beschrijving: {product['description']}"))
            if "ingredients" in product:
                product_controls.append(txt(f"Ingrediënten: {', '.join(product['ingredients'])}"))
            if "allergens" in product:
                product_controls.append(txt(f"Allergenen: {', '.join(product['allergens'])}"))
            if "expiry_date" in product:
                product_controls.append(txt(f"Houdbaar tot: {product['expiry_date']}"))

                days_left = days_until_expiry(product["expiry_date"])
                if days_left is not None and days_left <= 30:
                    product_controls.append(
                        txt("⚠ Dit product verloopt binnenkort.", color=WARNING, weight=ft.FontWeight.BOLD)
                    )

            product_controls.append(
                ft.ElevatedButton(
                    "Product registreren",
                    bgcolor=PRIMARY,
                    color=WHITE,
                    on_click=register_product,
                )
            )

            result_area.controls.append(make_card(ft.Column(controls=product_controls, spacing=6)))
            page.update()

        def scan_qr(e):
            code_input.value = "CHOCO001"
            search_product(e)

        camera_preview = ft.Container(
            height=145,
            bgcolor="#EADFD2",
            border_radius=22,
            padding=18,
            content=ft.Column(
                controls=[
                    ft.Text("📷", size=40),
                    txt("Camera", size=15, weight=ft.FontWeight.BOLD),
                    txt("Richt de camera op de QR-code van je product.", size=12),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=4,
            ),
        )

        content = ft.Column(
            controls=[
                ft.Text("Product scannen", size=25, weight=ft.FontWeight.BOLD, color=PRIMARY),
                txt("Scan een QR-code of voer zelf een productcode in.", size=14),
                camera_preview,
                ft.ElevatedButton(
                    "Scan QR-code",
                    bgcolor=SECONDARY,
                    color=WHITE,
                    height=45,
                    width=330,
                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=16)),
                    on_click=scan_qr,
                ),
                code_input,
                ft.ElevatedButton(
                    "Product zoeken",
                    bgcolor=PRIMARY,
                    color=WHITE,
                    height=45,
                    width=330,
                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=16)),
                    on_click=search_product,
                ),
                message,
                result_area,
            ],
            spacing=8,
            scroll=ft.ScrollMode.AUTO,
        )

        render_phone(content)

    def show_assistant():
        chat_area = ft.Column(spacing=8)
        question_input = ft.TextField(
            label="Stel je vraag",
            hint_text="Waar kan ik je mee helpen?",
            border_radius=14,
            bgcolor=WHITE,
        )

        def add_message(sender, message, is_bot=False):
            chat_area.controls.append(
                make_card(
                    ft.Column(
                        controls=[
                            txt(
                                sender,
                                size=13,
                                weight=ft.FontWeight.BOLD,
                                color=PRIMARY if is_bot else SECONDARY,
                            ),
                            txt(message),
                        ],
                        spacing=4,
                    )
                )
            )

        def get_answer(question):
            q = question.lower()

            if "allergeen" in q or "allergenen" in q:
                return "Allergenen staan bij de productinformatie nadat je een product hebt gescand."
            if "klacht" in q:
                return "Je kunt je klachten beheren via Profiel en daarna Klachten beheren. Bij vragen kun je contact opnemen met de klantenservice."
            if "houdbaar" in q or "datum" in q:
                return "De houdbaarheidsdatum staat bij de productinformatie. Producten die binnenkort verlopen worden extra gemarkeerd."
            if "scan" in q or "qr" in q:
                return "Ga naar Scan en gebruik de knop Scan QR-code of voer een productcode in."
            if "bestel" in q or "shop" in q:
                return "In de Shop kun je producten toevoegen aan je winkelmandje en een bestelling plaatsen."
            if "account" in q or "profiel" in q:
                return "In Profiel kun je je gegevens, voorkeuren en allergieën bekijken en aanpassen."
            return "Ik kan helpen met vragen over producten, allergenen, klachten, houdbaarheid, scannen, bestellen en accountinformatie. Voor andere vragen verwijs ik je door naar de klantenservice."

        def send_question(e):
            if not question_input.value:
                return

            user_question = question_input.value
            add_message("Jij", user_question)
            add_message("Assistent", get_answer(user_question), is_bot=True)
            question_input.value = ""
            page.update()

        def quick_question(question):
            question_input.value = question
            send_question(None)

        content = ft.Column(
            controls=[
                ft.Text("Assistent", size=25, weight=ft.FontWeight.BOLD, color=PRIMARY),
                txt("Stel een vraag aan de digitale Chocolate Firm assistent.", size=14),
                make_card(
                    ft.Column(
                        controls=[
                            txt("Veelgestelde vragen", size=17, weight=ft.FontWeight.BOLD),
                            ft.ElevatedButton(
                                "Waar vind ik allergenen?",
                                bgcolor=WHITE,
                                color=PRIMARY,
                                on_click=lambda e: quick_question("Waar vind ik allergenen?"),
                            ),
                            ft.ElevatedButton(
                                "Hoe dien ik een klacht in?",
                                bgcolor=WHITE,
                                color=PRIMARY,
                                on_click=lambda e: quick_question("Hoe dien ik een klacht in?"),
                            ),
                            ft.ElevatedButton(
                                "Hoe werkt bestellen?",
                                bgcolor=WHITE,
                                color=PRIMARY,
                                on_click=lambda e: quick_question("Hoe werkt bestellen?"),
                            ),
                        ],
                        spacing=6,
                    )
                ),
                chat_area,
                question_input,
                ft.ElevatedButton(
                    "Verstuur",
                    bgcolor=PRIMARY,
                    color=WHITE,
                    height=45,
                    width=330,
                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=16)),
                    on_click=send_question,
                ),
            ],
            spacing=8,
            scroll=ft.ScrollMode.AUTO,
        )

        add_message(
            "Assistent",
            "Welkom! Waar kan ik je mee helpen?",
            is_bot=True,
        )

        render_phone(content)

    def show_shop():
        user = state["user"]
        products = load_json(PRODUCTS_FILE)
        message = ft.Text("", size=13)
        cart_list = ft.Column(spacing=4)

        def cart_total():
            return sum(item["price"] * item["quantity"] for item in state["cart"])

        def refresh_cart():
            cart_list.controls.clear()

            if not state["cart"]:
                cart_list.controls.append(txt("Je winkelmandje is leeg."))
                return

            for item in state["cart"]:
                cart_list.controls.append(
                    txt(f"{item['quantity']}x {item['name']} - €{item['price'] * item['quantity']:.2f}")
                )

            cart_list.controls.append(
                txt(f"Totaal: €{cart_total():.2f}", size=15, weight=ft.FontWeight.BOLD, color=PRIMARY)
            )

        def add_to_cart(product):
            existing = next((item for item in state["cart"] if item["product_id"] == product["id"]), None)

            if existing:
                existing["quantity"] += 1
            else:
                state["cart"].append(
                    {
                        "product_id": product["id"],
                        "name": product["name"],
                        "price": product["price"],
                        "quantity": 1,
                    }
                )

            message.value = f"{product['name']} toegevoegd aan winkelmandje."
            message.color = SUCCESS
            refresh_cart()
            page.update()

        def place_order(e):
            if not state["cart"]:
                message.value = "Je winkelmandje is leeg."
                message.color = ERROR
                page.update()
                return

            orders = load_json(ORDERS_FILE)
            total = round(cart_total(), 2)

            orders.append(
                {
                    "id": len(orders) + 1,
                    "user_id": user["id"],
                    "items": state["cart"],
                    "total_price": total,
                    "status": "Bevestigd",
                    "created_at": str(date.today()),
                }
            )

            save_json(ORDERS_FILE, orders)
            add_notification(user["id"], f"Je bestelling van €{total:.2f} is bevestigd.")

            state["cart"] = []
            refresh_cart()

            message.value = "Bestelling succesvol geplaatst."
            message.color = SUCCESS
            page.update()

        product_cards = []

        for product in products:
            product_cards.append(
                make_card(
                    ft.Column(
                        controls=[
                            txt(
                                f"🍫 {product['name']}",
                                size=16,
                                weight=ft.FontWeight.BOLD,
                                color=PRIMARY,
                            ),
                            txt(f"Herkomst: {product['origin']}"),
                            txt(f"Prijs: €{product['price']}"),
                            ft.ElevatedButton(
                                "Toevoegen",
                                bgcolor=PRIMARY,
                                color=WHITE,
                                on_click=lambda e, p=product: add_to_cart(p),
                            ),
                        ],
                        spacing=6,
                    )
                )
            )

        refresh_cart()

        content = ft.Column(
            controls=[
                ft.Text("Shop", size=25, weight=ft.FontWeight.BOLD, color=PRIMARY),
                txt("Bekijk producten en plaats eenvoudig een bestelling.", size=14),
                txt("Producten", size=19, weight=ft.FontWeight.BOLD),
                *product_cards,
                txt("Winkelmandje", size=19, weight=ft.FontWeight.BOLD),
                make_card(
                    ft.Column(
                        controls=[
                            cart_list,
                            ft.ElevatedButton(
                                "Bestelling plaatsen",
                                bgcolor=PRIMARY,
                                color=WHITE,
                                height=45,
                                width=300,
                                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=16)),
                                on_click=place_order,
                            ),
                            message,
                        ],
                        spacing=8,
                    )
                ),
            ],
            spacing=8,
            scroll=ft.ScrollMode.AUTO,
        )

        render_phone(content)

    def show_complaints():
        user = state["user"]
        photo_added = {"value": False}

        title_input = ft.TextField(
            label="Onderwerp",
            hint_text="Bijvoorbeeld: Beschadigde verpakking",
            border_radius=14,
            bgcolor=WHITE,
        )

        category_input = ft.Dropdown(
            label="Categorie",
            border_radius=14,
            bgcolor=WHITE,
            options=[
                ft.dropdown.Option("Verpakking"),
                ft.dropdown.Option("Smaak"),
                ft.dropdown.Option("Levering"),
                ft.dropdown.Option("Kwaliteit"),
            ],
        )

        description_input = ft.TextField(
            label="Beschrijving",
            hint_text="Beschrijf kort wat er aan de hand is",
            multiline=True,
            min_lines=2,
            max_lines=3,
            border_radius=14,
            bgcolor=WHITE,
        )

        message = ft.Text("", size=13)
        photo_status = ft.Text("", size=13, color=SUCCESS)
        complaints_list = ft.Column(spacing=6)

        def add_photo(e):
            photo_added["value"] = True
            photo_status.value = "✓ Foto toegevoegd"
            page.update()

        def delete_complaint(complaint_id):
            all_complaints = load_json(COMPLAINTS_FILE)
            all_complaints = [complaint for complaint in all_complaints if complaint["id"] != complaint_id]
            save_json(COMPLAINTS_FILE, all_complaints)
            refresh_complaints()

            message.value = "Klacht verwijderd."
            message.color = SUCCESS
            page.update()

        def refresh_complaints():
            complaints_list.controls.clear()
            all_complaints = load_json(COMPLAINTS_FILE)

            user_complaints = [c for c in all_complaints if c.get("user_id") == user["id"]]

            if not user_complaints:
                complaints_list.controls.append(make_card(txt("Je hebt nog geen klachten ingediend.")))
                return

            for complaint in user_complaints:
                complaints_list.controls.append(
                    make_card(
                        ft.Column(
                            controls=[
                                txt(
                                    f"📝 {complaint['title']}",
                                    size=16,
                                    weight=ft.FontWeight.BOLD,
                                    color=PRIMARY,
                                ),
                                txt(f"Categorie: {complaint['category']}"),
                                txt(f"Beschrijving: {complaint['description']}"),
                                txt(f"Status: {complaint['status']}", weight=ft.FontWeight.BOLD, color=PRIMARY),
                                txt(f"Foto toegevoegd: {'Ja' if complaint.get('photo_added') else 'Nee'}"),
                                txt(f"Aangemaakt op: {complaint['created_at']}"),
                                ft.OutlinedButton(
                                    "Klacht verwijderen",
                                    style=ft.ButtonStyle(
                                        color=ERROR,
                                        shape=ft.RoundedRectangleBorder(radius=14),
                                    ),
                                    on_click=lambda e, cid=complaint["id"]: delete_complaint(cid),
                                ),
                            ],
                            spacing=4,
                        )
                    )
                )

        def submit_complaint(e):
            if not title_input.value or not description_input.value or not category_input.value:
                message.value = "Vul alle velden in."
                message.color = ERROR
                page.update()
                return

            all_complaints = load_json(COMPLAINTS_FILE)

            all_complaints.append(
                {
                    "id": len(all_complaints) + 1,
                    "user_id": user["id"],
                    "title": title_input.value,
                    "description": description_input.value,
                    "category": category_input.value,
                    "status": "Ontvangen",
                    "photo_added": photo_added["value"],
                    "created_at": str(date.today()),
                }
            )

            save_json(COMPLAINTS_FILE, all_complaints)
            add_notification(user["id"], "Je klacht is ontvangen en geregistreerd.")

            title_input.value = ""
            description_input.value = ""
            category_input.value = None
            photo_added["value"] = False
            photo_status.value = ""

            message.value = "Klacht succesvol ingediend."
            message.color = SUCCESS

            refresh_complaints()
            page.update()

        refresh_complaints()

        content = ft.Column(
            controls=[
                ft.Text("Klachten", size=25, weight=ft.FontWeight.BOLD, color=PRIMARY),
                txt("Dien een klacht in, volg de status of verwijder een klacht.", size=14),
                ft.ElevatedButton(
                    "Terug naar profiel",
                    bgcolor=SECONDARY,
                    color=WHITE,
                    on_click=lambda e: navigate("profile"),
                ),
                make_card(
                    ft.Column(
                        controls=[
                            txt("Nieuwe klacht", size=17, weight=ft.FontWeight.BOLD),
                            title_input,
                            category_input,
                            description_input,
                            ft.OutlinedButton(
                                "Foto toevoegen",
                                style=ft.ButtonStyle(
                                    color=PRIMARY,
                                    shape=ft.RoundedRectangleBorder(radius=14),
                                ),
                                on_click=add_photo,
                            ),
                            photo_status,
                            ft.ElevatedButton(
                                "Klacht indienen",
                                bgcolor=PRIMARY,
                                color=WHITE,
                                height=45,
                                width=330,
                                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=16)),
                                on_click=submit_complaint,
                            ),
                            message,
                        ],
                        spacing=8,
                    )
                ),
                txt("Mijn klachten", size=19, weight=ft.FontWeight.BOLD),
                complaints_list,
            ],
            spacing=8,
            scroll=ft.ScrollMode.AUTO,
        )

        render_phone(content)

    def show_edit_profile():
        user = state["user"]

        name_input = ft.TextField(
            label="Naam",
            value=user.get("name", ""),
            border_radius=14,
            bgcolor=WHITE,
        )
        favorite_input = ft.TextField(
            label="Favoriete chocoladesoort",
            value=user.get("favorite_chocolate", ""),
            border_radius=14,
            bgcolor=WHITE,
        )
        allergies_input = ft.TextField(
            label="Allergieën",
            value=user.get("allergies", ""),
            border_radius=14,
            bgcolor=WHITE,
        )
        notification_dropdown = ft.Dropdown(
            label="Notificaties",
            border_radius=14,
            bgcolor=WHITE,
            value="Aan" if user.get("notifications_enabled", True) else "Uit",
            options=[
                ft.dropdown.Option("Aan"),
                ft.dropdown.Option("Uit"),
            ],
        )

        message = ft.Text("", size=13)

        def save_profile(e):
            users = load_json(USERS_FILE)

            for stored_user in users:
                if stored_user["id"] == user["id"]:
                    stored_user["name"] = name_input.value
                    stored_user["favorite_chocolate"] = favorite_input.value
                    stored_user["allergies"] = allergies_input.value
                    stored_user["notifications_enabled"] = notification_dropdown.value == "Aan"

                    state["user"] = stored_user
                    break

            save_json(USERS_FILE, users)

            message.value = "Profiel succesvol opgeslagen."
            message.color = SUCCESS
            page.update()

        content = ft.Column(
            controls=[
                ft.Text("Profiel bewerken", size=25, weight=ft.FontWeight.BOLD, color=PRIMARY),
                txt("Beheer je gegevens, voorkeuren en notificaties.", size=14),
                make_card(
                    ft.Column(
                        controls=[
                            name_input,
                            txt(f"Email: {user['email']}"),
                            favorite_input,
                            allergies_input,
                            notification_dropdown,
                            ft.ElevatedButton(
                                "Wijzigingen opslaan",
                                bgcolor=PRIMARY,
                                color=WHITE,
                                height=45,
                                width=330,
                                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=16)),
                                on_click=save_profile,
                            ),
                            message,
                        ],
                        spacing=8,
                    )
                ),
                ft.ElevatedButton(
                    "Terug naar profiel",
                    bgcolor=SECONDARY,
                    color=WHITE,
                    on_click=lambda e: navigate("profile"),
                ),
            ],
            spacing=8,
            scroll=ft.ScrollMode.AUTO,
        )

        render_phone(content)

    def show_profile():
        user = state["user"]
        products = load_json(PRODUCTS_FILE)
        registered = load_json(REGISTERED_FILE)
        complaints = load_json(COMPLAINTS_FILE)
        orders = load_json(ORDERS_FILE)
        notifications = load_json(NOTIFICATIONS_FILE)

        my_products = []

        for item in registered:
            if item.get("user_id") == user["id"]:
                product = next((p for p in products if p["id"] == item["product_id"]), None)
                if product:
                    expiry_controls = []
                    if product.get("expiry_date"):
                        expiry_controls.append(f" - houdbaar tot {product['expiry_date']}")
                    my_products.append(txt(f"🍫 {product['name']}{''.join(expiry_controls)}"))

        if not my_products:
            my_products.append(txt("Nog geen producten geregistreerd."))

        my_complaints_count = len([c for c in complaints if c.get("user_id") == user["id"]])
        my_orders = [o for o in orders if o.get("user_id") == user["id"]]
        my_notifications = [n for n in notifications if n.get("user_id") == user["id"]]

        order_controls = []
        if not my_orders:
            order_controls.append(txt("Nog geen bestellingen geplaatst."))
        else:
            for order in my_orders:
                order_controls.append(
                    txt(f"Bestelling #{order['id']} - €{order['total_price']:.2f} - {order['status']}")
                )

        notification_controls = []
        if not my_notifications:
            notification_controls.append(txt("Nog geen meldingen."))
        else:
            for notification in reversed(my_notifications[-5:]):
                notification_controls.append(txt(f"🔔 {notification['message']}"))

        def logout(e):
            state["user"] = None
            state["screen"] = "login"
            state["selected_product"] = None
            state["cart"] = []
            show_login()

        content = ft.Column(
            controls=[
                ft.Text("Profiel", size=25, weight=ft.FontWeight.BOLD, color=PRIMARY),
                make_card(
                    ft.Column(
                        controls=[
                            txt("Mijn gegevens", size=17, weight=ft.FontWeight.BOLD),
                            txt(f"Naam: {user['name']}"),
                            txt(f"Email: {user['email']}"),
                            txt(f"Favoriete chocolade: {user.get('favorite_chocolate', '-') or '-'}"),
                            txt(f"Allergieën: {user.get('allergies', '-') or '-'}"),
                            txt(f"Notificaties: {'Aan' if user.get('notifications_enabled', True) else 'Uit'}"),
                            ft.ElevatedButton(
                                "Profiel bewerken",
                                bgcolor=PRIMARY,
                                color=WHITE,
                                on_click=lambda e: navigate("edit_profile"),
                            ),
                        ],
                        spacing=5,
                    )
                ),
                make_card(
                    ft.Column(
                        controls=[
                            txt("Mijn producten", size=17, weight=ft.FontWeight.BOLD),
                            *my_products,
                        ],
                        spacing=5,
                    )
                ),
                make_card(
                    ft.Column(
                        controls=[
                            txt("Mijn bestellingen", size=17, weight=ft.FontWeight.BOLD),
                            *order_controls,
                        ],
                        spacing=5,
                    )
                ),
                make_card(
                    ft.Column(
                        controls=[
                            txt("Meldingen", size=17, weight=ft.FontWeight.BOLD),
                            *notification_controls,
                        ],
                        spacing=5,
                    )
                ),
                make_card(
                    ft.Column(
                        controls=[
                            txt("Klantenservice", size=17, weight=ft.FontWeight.BOLD),
                            txt(f"Ingediende klachten: {my_complaints_count}"),
                            ft.ElevatedButton(
                                "Klachten beheren",
                                bgcolor=PRIMARY,
                                color=WHITE,
                                on_click=lambda e: navigate("complaints"),
                            ),
                        ],
                        spacing=6,
                    )
                ),
                ft.ElevatedButton(
                    "Uitloggen",
                    bgcolor=PRIMARY,
                    color=WHITE,
                    height=45,
                    width=330,
                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=16)),
                    on_click=logout,
                ),
            ],
            spacing=8,
            scroll=ft.ScrollMode.AUTO,
        )

        render_phone(content)

    show_login()


ft.run(main)