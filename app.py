import storage
from datetime import date

# Sākumā definējam konstantes
CATEGORIES = ["Ēdiens", "Transports", "Izklaide", "Komunālie", "Veselība", "Iepirkšanās", "Cits"]

def add_expense(expenses):
    """
    Nodrošina lietotāja saskarni jauna izdevuma pievienošanai.
    
    Ievāc datus (datumu, kategoriju, summu, aprakstu), veic pamata 
    validāciju un saglabā izmaiņas JSON failā.
    """
    print("\n--- Pievienot jaunu izdevumu ---")
    
    # Datums ar noklusējuma vērtību (šodiena)
    date_input = input(f"Datums (YYYY-MM-DD) [{date.today()}]: ") or str(date.today())
    
    # Kategorijas izvēle
    print("Izvēlies kategoriju:")
    for i, cat in enumerate(CATEGORIES, 1):
        print(f"{i}) {cat}")
    
    try:
        cat_choice = int(input("Izvēle (numurs): "))
        category = CATEGORIES[cat_choice - 1]
        
        amount = float(input("Summa (EUR): "))
        description = input("Apraksts: ") or "Nav apraksta"
        
        # Izveidojam jauno ierakstu
        new_expense = {
            "date": date_input,
            "amount": amount,
            "category": category,
            "description": description
        }
        
        expenses.append(new_expense)
        storage.save_expenses(expenses)
        print("✅ Izdevums saglabāts!")
        
    except (ValueError, IndexError):
        print("❌ Kļūda: Nepareiza ievade. Mēģini vēlreiz.")

def show_all_expenses(expenses):
    """
    Formatē un izvada terminālī visus reģistrētos izdevumus.
    
    Ja saraksts ir tukšs, informē lietotāju. Beigās izvada 
    visu izdevumu kopsummu, izmantojot logic moduli.
    """
    print("\n--- Visi izdevumi ---")
    if not expenses:
        print("Saraksts ir tukšs.")
        return

    for exp in expenses:
        print(f"{exp['date']} | {exp['amount']:.2f} EUR | {exp['category']} | {exp['description']}")

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