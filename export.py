import csv

def export_to_csv(expenses, filename="izdevumi_eksports.csv"):
    """
    Eksportē visus izdevumus uz CSV failu.
    """
    if not expenses:
        return False
    
    headers = expenses[0].keys()
    
    try:
        with open(filename, mode="w", newline="", encoding="utf-8-sig") as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            writer.writerows(expenses)
        return True
    except IOError:
        return False