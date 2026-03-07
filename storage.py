import json
import os
import csv


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

def export_to_csv(expenses, filename="izdevumi_eksports.csv"):
    """
    Eksportē visus izdevumus uz CSV failu, ko var atvērt ar Excel.
    Atgriež True, ja izdevās, vai False, ja saraksts tukšs.
    """
    if not expenses:
        return False
    
    # Paņemam atslēgas no pirmā ieraksta kā kolonnu nosaukumus
    headers = expenses[0].keys()
    
    try:
        # encoding="utf-8-sig" palīdz Excel pareizi attēlot latviešu burtus
        with open(filename, mode="w", newline="", encoding="utf-8-sig") as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            writer.writerows(expenses)
        return True
    except IOError:
        return False