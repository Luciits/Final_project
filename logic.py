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
    Aprēķina atlikumu un atgriež statusu.
    """
    total = sum_total(expenses)
    remaining = limit - total
    is_over = total > limit
    return {
        "total": total,
        "limit": limit,
        "remaining": remaining,
        "is_over": is_over,
        "percent": (total / limit * 100) if limit > 0 else 0
    }