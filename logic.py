def sum_total(expenses):
    """
    Aprēķina kopējo summu visiem sarakstā esošajiem izdevumiem.
    Pieņem sarakstu ar vārdnīcām, kur katrai ir atslēga 'amount'.
    """
    return sum(expense["amount"] for expense in expenses)