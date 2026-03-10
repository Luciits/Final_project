from datetime import datetime
def sum_total(expenses):
    """
    Aprēķina kopējo summu visiem sarakstā esošajiem izdevumiem.
    Pieņem sarakstu ar vārdnīcām, kur katrai ir atslēga 'amount'.
    """
    return sum(expense["amount"] for expense in expenses)

def filter_by_month(expenses, year, month):
    """
    Atgriež tikai norādītā gada un mēneša izdevumus.
    """
    result = []
    for expense in expenses:
        d = datetime.strptime(expense["date"], "%Y-%m-%d")
        if d.year == year and d.month == month:
            result.append(expense)
    return result

def sum_by_category(expenses):
    """
    Atgriež vārdnīcu ar kopsummu katrai kategorijai.
    """
    totals = {}
    for expense in expenses:
        cat = expense["category"]
        totals[cat] = totals.get(cat, 0) + expense["amount"]
    return {cat: round(total, 2) for cat, total in totals.items()}

def get_available_months(expenses):
    """
    Izvelk unikālus mēnešus (YYYY-MM) no visiem izdevumiem.
    """
    months = set()
    for expense in expenses:
        # Pārveidojam datumu formātā "2025-02"
        month_str = expense["date"][:7] 
        months.add(month_str)
    return sorted(list(months), reverse=True)

def get_budget_status(expenses, limit):
    """
    Aprēķina budžeta atlikumu un atgriež statusu.
    """
    total = sum_total(expenses)
    remaining = limit - total
    is_over = total > limit
    return {
        "total": total,
        "limit": limit,
        "remaining": remaining,
        "is_over": is_over,
        "percent": round(total / limit * 10, 1) if limit > 0 else 0
    }

def get_full_analysis(expenses):
    """
    Veic pilnu datu analīzi: statistiku un kategoriju kopsavilkumu.
    """
    if not expenses:
        return None

    total_sum = sum(exp["amount"] for exp in expenses)
    unique_dates = {exp["date"] for exp in expenses}
    
    # Kategoriju aprēķini
    cat_totals = {}
    for exp in expenses:
        cat = exp["category"]
        cat_totals[cat] = cat_totals.get(cat, 0) + exp["amount"]

    # Sagatavojam kopsavilkumu par katru kategoriju (ar procentiem)
    category_summary = []
    for cat, amt in cat_totals.items():
        category_summary.append({
            "name": cat,
            "amount": round(amt, 2),
            "percentage": round((amt / total_sum * 100), 1) if total_sum > 0 else 0
        })
    
    # Sakārtojam kategorijas no dārgākās uz lētāko
    category_summary.sort(key=lambda x: x["amount"], reverse=True)

    return {
        "total_sum": round(total_sum, 2),
        "daily_avg": round(total_sum / len(unique_dates), 2) if unique_dates else 0,
        "top_category": category_summary[0]["name"] if category_summary else "N/A",
        "entry_count": len(expenses),
        "unique_days": len(unique_dates),
        "categories": category_summary
    }

def search_expenses(expenses, query):
    """
    Meklē izdevumus, kuru aprakstā ir meklētā frāze.
    """
    query = query.lower()
    return [
        exp for exp in expenses 
        if query in exp["description"].lower()
    ]