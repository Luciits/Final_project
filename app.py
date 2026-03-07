import storage
from datetime import date, datetime
import logic

# Sākumā definējam konstantes
CATEGORIES = ["Ēdiens", "Transports", "Izklaide", "Komunālie", "Veselība", "Iepirkšanās", "Cits"]

def is_valid_date(date_text):
    """Pārbauda, vai teksts atbilst formātam YYYY-MM-DD."""
    try:
        datetime.strptime(date_text, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def add_expense(expenses):
    """
    Nodrošina lietotāja saskarni jauna izdevuma pievienošanai.
    
    Lietotājs ievada datumu, izvēlas kategoriju no saraksta, ievada summu 
    un aprakstu. Dati tiek validēti un saglabāti JSON failā.
    """
    print("\n--- Pievienot jaunu izdevumu ---")
    
    # 1. Datums
    date_input = input(f"Datums (YYYY-MM-DD) [{date.today()}]: ") or str(date.today())
    if not is_valid_date(date_input):
        print(f"❌ Kļūda: '{date_input}' nav derīgs datums! Lieto formātu YYYY-MM-DD.")
        return
    
    # 2. Kategorijas izvēle
    print("Pieejamās kategorijas:")
    for i, cat in enumerate(CATEGORIES, 1):
        print(f"{i}) {cat}")
    
    try:
        choice = int(input("Izvēlies kategorijas numuru (1-7): "))
        if 1 <= choice <= len(CATEGORIES):
            category = CATEGORIES[choice - 1]  # Šeit mēs iegūstam tekstu, piem., "Ēdiens"
        else:
            print("❌ Kļūda: Nepareizs numurs!")
            return

        # 3. Summa
        amount_input = input("Summa (EUR): ")
        amount = float(amount_input)
        if amount <= 0:
            print("❌ Kļūda: Summai jābūt pozitīvai!")
            return

        # 4. Apraksts
        description = input("Apraksts: ") or "Nav apraksta"
        
        # Izveidojam ierakstu
        new_item = {
            "date": date_input,
            "amount": round(amount, 2),
            "category": category,
            "description": description
        }
        
        expenses.append(new_item)
        storage.save_expenses(expenses)
        print(f"✅ Pievienots: {category} | {amount:.2f} EUR")
        
    except ValueError:
        print("❌ Kļūda: Summai un izvēlei jābūt skaitļiem!")

def show_all_expenses(expenses):
    """
    Formatē un izvada terminālī visus reģistrētos izdevumus ar kopsummu.
    """
    print("\n--- Visi izdevumi ---")
    if not expenses:
        print("Saraksts ir tukšs.")
        return

    print(f"{'Datums':<12} | {'Summa':>10} | {'Kategorija':<15} | {'Apraksts'}")
    print("-" * 55)
    
    for exp in expenses:
        print(f"{exp['date']:<12} | {exp['amount']:>8.2f} EUR | {exp['category']:<15} | {exp['description']}")
    # IZMANTOJAM LOGIC MODULI
    total = logic.sum_total(expenses)
    print("-" * 55)
    print(f"{'KOPĀ:':<12} | {total:>8.2f} EUR")


def main():
    """
    Lietojumprogrammas galvenā cilpa.
    
    Nodrošina interaktīvu izvēlni un koordinē darbības starp 
    lietotāju un programmas moduļiem (storage, logic).
    """
    # Ielādējam datus programmas sākumā
    expenses = storage.load_expenses()
    
    while True:
        print("\n=== IZDEVUMU IZSEKOTĀJS ===")
        print("1) Pievienot izdevumu")
        print("2) Parādīt visus izdevumus")
        print("7) Iziet")
        
        choice = input("\nIzvēlies darbību: ")
        
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            show_all_expenses(expenses)
        elif choice == "7":
            print("Uz redzēšanos!")
            break
        else:
            print("Nepareiza izvēle, mēģini vēlreiz.")

if __name__ == "__main__":
    main()