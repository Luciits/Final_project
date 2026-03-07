A. Programmas aprakts.

Izstrādāt komandrindas (CLI) lietojumprogrammu, kas ļauj lietotājam reģistrēt ikdienas izdevumus, saglabāt tos JSON failā, veikt datu analīzi (filtrēšanu, summēšanu) un eksportēt atskaites CSV formātā.

B. Datu struktūra.

Katrs izdevums tiek glabāts kā vārdnīca (dictionary), un visi izdevumi kopā veido sarakstu (list).
{
    "date": "2026-03-07",
    "amount": 12.50,
    "category": "Ēdiens",
    "description": "Pusdienas kafejnīcā"
}

Es izvēlējos šādu formātu jo:

Saderība ar JSON un Python:
Vārdnīcas struktūra (Key: Value) tieši kartējas uz Python dict tipu un JSON objektu. Tas ļauj izmantot standarta json moduli datu ielādei un saglabāšanai bez sarežģītas transformācijas.

Datu meklēšana un filtrēšana:

date (YYYY-MM-DD): ISO 8601 formāts izvēlēts, jo tas ir viegli šķirojams (alfabētiskā secība sakrīt ar hronoloģisko) un vienkārši parsējams ar datetime.strptime().

amount (float): Skaitlisks tips ļauj veikt matemātiskas operācijas (summēšanu, vidējā aprēķinu) bez papildu teksta konvertēšanas katrā loģikas solī.

category: Atsevišķs lauks kategorijai ļauj efektīvi grupēt izdevumus (piemēram, izmantojot vārdnīcu, lai uzskaitītu kopsummas pa kategorijām).

C. Moduļu plāns

Lai nodrošinātu koda lasāmību un vieglu uzturēšanu, programma tiks sadalīta 4 loģiskos moduļos. Katram modulim ir sava skaidri definēta atbildība.

app.py (Lietotāja saskarne un vadība)
Šis ir programmas ieejas punkts. Tas ir vienīgais modulis, kurā notiek tieša komunikācija ar lietotāju.

Galvenās funkcijas:

show_menu(): Parāda pieejamās komandas.

main(): Nodrošina galveno ciklu un maršrutē lietotāja izvēles.

add_expense_ui(): Ievāc datus no lietotāja, veic sākotnējo validāciju un izsauc saglabāšanas loģiku.

display_expenses(): Formatē un izvada datus tabulas veidā terminālī.

storage.py (Datu uzglabāšana)
Šis modulis atbild tikai par darbu ar failu sistēmu (JSON). Tas nezina, ko dati nozīmē, tikai to, kā tos saglabāt un nolasīt.

Galvenās funkcijas:

load_expenses(): Nolasa expenses.json failu. Ja fails neeksistē, atgriež tukšu sarakstu, lai novērstu kļūdas.

save_expenses(expenses): Pārraksta JSON failu ar aktuālo sarakstu, izmantojot indent=4 lasāmībai.

logic.py (Biznesa loģika)
Šis ir "tīrs" modulis. Tas satur tikai funkcijas, kas apstrādā datus (sarakstus un vārdnīcas), un tajā netiek izmantoti print() vai input().

Galvenās funkcijas:

filter_by_month(expenses, year, month): Atgriež tikai tos ierakstus, kas atbilst norādītajam periodam.

sum_total(expenses): Aprēķina kopējo summu jebkuram padotam sarakstam.

sum_by_category(expenses): Izveido kopsavilkumu (vārdnīcu), kur atslēgas ir kategorijas un vērtības ir kopējie izdevumi tajās.

get_available_months(expenses): Analizē visus ierakstus un izvelk unikālus mēnešus filtrēšanas izvēlnei.

export.py (Datu eksports)
Modulis, kas nodrošina datu pārnešanu uz citiem formātiem.

Galvenās funkcijas:

export_to_csv(expenses, filename): Izmanto csv moduli, lai ierakstītu datus .csv failā, nodrošinot pareizu kodējumu (utf-8-sig) latviešu valodas atbalstam.

D. Lietotāja scenāriji

Jauna izdevuma pievienošana:

Lietotājs izvēlas komandu "Pievienot izdevumu".

Lietotājs nospiež Enter pie datuma (izmantojot šodienas datumu).

Lietotājs izvēlas kategoriju "Ēdiens" no saraksta.

Lietotājs ievada summu "15.50" un aprakstu "Pusdienas".

Programmas atbilde: "✓ Pievienots: 2026-03-07 | Ēdiens | 15.50 EUR".

Mēneša tēriņu analīze:

Lietotājs izvēlas komandu "Filtrēt pēc mēneša".

Programma parāda sarakstu ar mēnešiem, kuros ir ieraksti (piemēram, "1) 2026-02, 2) 2026-03").

Lietotājs izvēlas "2".

Programmas atbilde: Tabula ar visiem marta izdevumiem un marta kopsummu.

Kļūda ievadē (Validācija):

Lietotājs pievieno izdevumu, bet summas laukā ieraksta "desmit eiro".

Programmas atbilde: "❌ Kļūda: Summai jābūt skaitlim! Lūdzu, mēģiniet vēlreiz." (Programma neuzkaras, bet atgriežas pie izvēlnes).

E. Robežgadījumi un to risinājumi

Pirmā palaišanas reize (nav expenses.json)

load_expenses() funkcija pārbauda os.path.exists(). Ja fails netiek atrasts, tiek atgriezts tukšs saraksts [] bez kļūdas paziņojuma.

Negatīva summa

Pievienošanas funkcijā tiks pārbaudīts if amount <= 0. Ja vērtība nav derīga, lietotājam tiks rādīts brīdinājums.

Tukšs apraksts

Ja lietotājs neko neievada aprakstā, programma automātiski piešķirs vērtību ""Nav apraksta"", lai JSON failā nebūtu tukšu lauku.

Mēnesis bez izdevumiem

Ja filtrā izvēlētajā mēnesī nav datu, programma nevis rādīs tukšu tabulu, bet gan paziņojumu: ""Šajā mēnesī izdevumu nav.""

Dzēšana no tukša saraksta

Ja sarakstā nav neviena ieraksta, komanda ""Dzēst izdevumu"" uzreiz informēs lietotāju, ka nekas nav pieejams dzēšanai.

Nepareizs datuma formāts
Izmantojot datetime.strptime(), jebkurš formāts, kas nav YYYY-MM-DD, tiks noķerts ar ValueError un lietotājam lūgts ievadīt datumu atkārtoti.