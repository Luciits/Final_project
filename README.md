# Final_project
Gala projekts izdevumu izsekotājs
# Izdevumu Izsekotājs (CLI)

Vienkārša un efektīva komandrindas lietojumprogramma personīgo finanšu uzskaitei, kas izstrādāta Python valodā.

## Galvenās iespējas
- **Izdevumu reģistrēšana:** Datums, summa, kategorija un apraksts.
- **Datu validācija:** Pārbauda datuma formātu un summas pareizību.
- **Analīze:** Iespēja filtrēt datus pēc mēneša un skatīt kopsavilkumu pa kategorijām.
- **Datu drošība:** Automātiska saglabāšana JSON failā pēc katras izmaiņas.
- **Eksports:** Iespēja eksportēt datus uz CSV failu turpmākai analīzei Excel programmā.

## Projekta struktūra
- `app.py` - Lietotāja saskarne un programmas vadība.
- `logic.py` - Aprēķinu un filtrēšanas loģika.
- `storage.py` - JSON datu ielāde un saglabāšana.
- `export.py` - CSV eksporta funkcionalitāte.
- `docs/plan.md` - Detalizēts izstrādes plāns un arhitektūras apraksts.

### ✨ Bonusa iespējas
- **Budžeta kontrole:** Iespēja iestatīt mēneša limitu un saņemt brīdinājumus par tā pārsniegšanu.
- **Padziļināta analītika:** Automātiska vidējo dienas tēriņu aprēķināšana un dārgākās kategorijas noteikšana.
- **Datu meklēšana:** Ātra izdevumu atrašana pēc apraksta atslēgvārdiem.
- **Procentuālais sadalījums:** Kategoriju kopsavilkumā redzams katras nozares īpatsvars kopējā budžetā.

## Uzstādīšana un palaišana
1. Pārliecinieties, ka datorā ir uzstādīts Python 3.
2. Lejupielādējiet projekta failus.
3. Terminālī dodieties uz projekta mapi.
4. Palaidiet programmu ar komandu:
   ```bash
   python app.py

## Autors
Artūrs V. Luters - Programmēšanas pamati, 2026