import json
import os


def load_expenses(filepath="expenses.json"):
    """
    Ielādē izdevumus no JSON faila. 
    Atgriež tukšu sarakstu, ja fails neeksistē vai ir bojāts.
    """
    if not os.path.exists(filepath):
        return []
    
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        # Ja fails ir tukšs vai nav derīgs JSON, atgriežam tukšu sarakstu
        return []

def save_expenses(expenses, filepath="expenses.json"):
    """
    Saglabā izdevumu sarakstu JSON failā ar atkāpēm labākai lasāmībai.
    """
    try:
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(expenses, f, indent=4, ensure_ascii=False)
    except IOError as e:
        print(f"❌ Kļūda saglabājot datus: {e}")

def save_budget(limit, filepath="budget.json"):
    """
    Saglabā mēneša budžeta limitu
    """
    try:
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump({"limit": limit}, f)
    except IOError:
        print("❌ Neizdevās saglabāt budžeta limitu.")

def load_budget(filepath="budget.json"):
    """
    Ielādē budžeta limitu. Ja nav noteikts, atgriež 0.
    """
    if not os.path.exists(filepath):
        return 0.0
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data.get("limit", 0.0)
    except (json.JSONDecodeError, IOError):
        return 0.0