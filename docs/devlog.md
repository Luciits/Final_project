# Izstrādes Žurnāls (DEVLOG)

## 1. Posms: Plānošana un struktūra
- **Datums:** 2026-03-07
- **Darbība:** Izveidots projekta plāns (`plan.md`) un definēta 3 slāņu arhitektūra.
- **Izaicinājums:** Izlemt starp viena faila aplikāciju vai moduļiem. Izvēlēti moduļi (`app`, `storage`, `logic`) labākai uzturēšanai.

## 2. Posms: Pamata funkcionalitāte un JSON
- **Darbība:** Izveidots `storage.py` ar JSON ielādi/saglabāšanu un `app.py` ar pamata izvēlni.
- **Problēma:** Pirmoreiz palaižot, programma meta kļūdu, ja `expenses.json` neeksistēja.
- **Risinājums:** Pievienota `os.path.exists()` pārbaude un `try-except` bloks `load_expenses` funkcijā.

## 3. Posms: Aprēķinu loģika un filtrēšana
- **Darbība:** Izstrādāts `logic.py`. Pievienota summēšana un filtrēšana pēc mēneša.
- **Uzlabojums:** Sākotnēji datumi bija vienkāršs teksts. Pārgāju uz ISO formātu (YYYY-MM-DD), lai atvieglotu hronoloģisko kārtošanu.

## 4. Posms: Dzēšana un Validācija
- **Darbība:** Pievienota `delete_expense_ui`.
- **Izaicinājums:** Nodrošināt, ka lietotājs neievada neeksistējošu ieraksta numuru.
- **Risinājums:** Ieviesta `IndexError` un `ValueError` apstrāde ievades laikā.

## 5. Posms: Eksports un Refaktorēšana
- **Darbība:** Pievienots CSV eksports.
- **Lēmums:** Sākotnēji eksports bija `storage.py`, bet saskaņā ar plānu tas tika pārcelts uz atsevišķu moduli `export.py`, lai ievērotu "Single Responsibility Principle".
- **Detaļa:** Izmantots `utf-8-sig` kodējums, lai Excel atpazītu latviešu burtus.

## 6. Posms: Budžeta limita kontrole
- **Datums:** 2026-03-09
- **Darbība:** Ieviesta iespēja iestatīt mēneša tēriņu griestus.
- **Izaicinājumi:** Mainīgo redzamība (scope). Funkcijai add_expense bija nepieciešama piekļuve budget_limit, kas definēts main() ciklā.
- **Risiājums:** Funkcija tika refaktorēta, pievienojot budget_limit kā argumentu. Tas nodrošināja tīru datu plūsmu un ļāva parādīt brīdinājumu uzreiz pēc datu saglabāšanas.
- **Datu struktūra:** Izvēlēts atsevišķs budget.json fails, lai nejauktu konfigurācijas datus ar darījumu sarakstu.
## 7. Posms: Paplašināta analītika
- **Darbība:** paplašinātas statistikas iespējas kas norāda vidējo izdevumu dienā un dārgāko kategoriju
- **Izaicinājumi:** Datu kārtošana vārdnīcās. Iemācījos izmantot `sorted()` ar `lambda` funkciju, lai kategoriju kopsavilkumā augšgalā vienmēr būtu lielākie tēriņi.
- **Risinājums:** Ieviesu validāciju `if total_sum > 0`, kas šādos gadījumos atgriež 0%, novēršot programmas "nobrukšanu".
## Secinājumi
Projekta gaitā iemācījos strādāt ar Git zariem (`merge`), strukturēt kodu vairākos failos un veikt datu validāciju, lai lietotājs nevarētu "salauzt" programmu.