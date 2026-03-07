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