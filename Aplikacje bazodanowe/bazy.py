import cx_Oracle
import random
import datetime
import oracledb 
import string
import csv

# Tworzymy połączenie z bazą danych
dsn_tns = oracledb.makedsn('217.173.198.135', '1521', service_name='tpdb')
username = 's101948'
password = 's101948'
connection = oracledb.connect(user=username, password=password, dsn=dsn_tns)

tab = int(input("Wybierz tabelke 1 - Adopcja, 2 - Zwierze, 3 - Wszystkie: "))
howMuch = int(input("Podaj ilosc insertow: "))

# Tworzymy kursor
cursor = connection.cursor()

#### Opiekun
imiona = ["Jan", "Anna", "Piotr", "Katarzyna", "Tomasz", "Barbara", "Marcin", "Marta", "Robert", "Magdalena"]
nazwiska = ["Kowalski", "Nowak", "Wójcik", "Kwiatkowski", "Kaczmarek", "Wojciechowski", "Mazur", "Krawczyk", "Piotrowski", "Grabowski"]
adresy_email = ["jan.kowalski@gmail.com", "anna.nowak@yahoo.com", "piotr.wojcik@wp.pl", "katarzyna.kwiatkowski@o2.pl", "tomasz.kaczmarek@interia.pl"]
telefony = ["+48123456789", "+48555667788", "+48999888777", "+48123456789", "+48678901234", "+48222222222", "+48888888888", "+48444444444"]
opis_nowego_miejsca = "".join(random.choices(string.ascii_letters, k=random.randint(10, 50)))
uwagi = "".join(random.choices(string.ascii_letters, k=random.randint(10, 50)))

f = open("zapytania.txt", "a")

if tab == 1:
    howMuch2 = int(input("Podaj ile insertow do tabeli Adopcja: "))
    # Generujemy 100 wpisów losowych danych dla tabeli OSOBA_ADOPTUJĄCA
    dataOsobaAdoptujaca = [(i, random.choice(imiona), random.choice(nazwiska), random.choice(adresy_email),
         str(random.randint(10000000000, 99999999999)), random.choice(telefony),
         datetime.date(1990, 1, 1) + datetime.timedelta(days=random.randint(1, 10000)),
         i) for i in range(howMuch)]

    # Tworzymy polecenie SQL wstawiające dane do tabeli OSOBA_ADOPTUJĄCA
    sqlOsobaAdoptujaca = "INSERT INTO OSOBA_ADOPTUJĄCA (osoba_adoptujaca_id, imie, nazwisko, adres_email, pesel, telefon, data_urodzenia, \"ADRES_OSOBY_ADOPTUJĄCEJ_ADRES_ID\") VALUES (:1, :2, :3, :4, :5, :6, :7, :8)"

    # Wykonujemy polecenie SQL z wygenerowanymi danymi
    cursor.executemany(sqlOsobaAdoptujaca, dataOsobaAdoptujaca)
    for param in dataOsobaAdoptujaca:
        statement = "INSERT INTO OSOBA_ADOPTUJĄCA (osoba_adoptujaca_id, imie, nazwisko, adres_email, pesel, telefon, data_urodzenia, \"ADRES_OSOBY_ADOPTUJĄCEJ_ADRES_ID\") VALUES (%s, %s, %s, %s, %s, %s, %s, %s)" % param
        f.write(statement + "\n")
    print("dodano do tabeli OsobaAdoptujaca")


    #INSERT INTO ADOPCJA (adopcja_id,data_adopcji,opis_nowego_miejsca,uwagi,"OSOBA_ADOPTUJĄCA_OSOBA_ID") VALUES (1,sysdate,0,0,1);
    # ADOPCJA
    dataAdopcja = [( i, datetime.date(2021, 1, 1) + datetime.timedelta(days=random.randint(1, 365)), random.choice(opis_nowego_miejsca),
         random.choice(uwagi), i) for i in range(howMuch2)]


        # Tworzymy polecenie SQL wstawiające dane do tabeli OPIEKUN
    sqlAdopcja = "INSERT INTO ADOPCJA (adopcja_id, data_adopcji, opis_nowego_miejsca, uwagi, OSOBA_ADOPTUJĄCA_OSOBA_ID) VALUES (:1, :2, :3, :4, :5)"


    # Wykonujemy polecenie SQL z wygenerowanymi danymi

    cursor.executemany(sqlAdopcja, dataAdopcja)
    for param in dataAdopcja:
        statement = "INSERT INTO ADOPCJA (adopcja_id, data_adopcji, opis_nowego_miejsca, uwagi, OSOBA_ADOPTUJĄCA_OSOBA_ID) VALUES (%s, %s, %s, %s, %s)" % param
        f.write(statement + "\n")
    print("dodano do tabeli Adopcja")


elif tab == 2:
    howMuch2 = int(input("Podaj ile INSERTow do tabeli Zwierze: "))

    dataOpiekun = [( i, datetime.date(2021, 1, 1) + datetime.timedelta(days=random.randint(1, 365)), random.choice(imiona),
         random.choice(nazwiska), random.choice(telefony), random.choice(adresy_email), i) for i in range(howMuch)]


    # Tworzymy polecenie SQL wstawiające dane do tabeli OPIEKUN
    sqlOpiekun = "INSERT INTO OPIEKUN (OPIEKUN_ID, DATA_ZATRUDNIENIA, IMIE, NAZWISKO, TELEFON, ADRES_EMAIL, ADRES_OPIEKUNA_ADRES_ID) VALUES (:1, :2, :3, :4, :5, :6, :7)"


    # Wykonujemy polecenie SQL z wygenerowanymi danymi

    cursor.executemany(sqlOpiekun, dataOpiekun)
    for param in dataOpiekun:
        statement = "INSERT INTO OPIEKUN (OPIEKUN_ID, DATA_ZATRUDNIENIA, IMIE, NAZWISKO, TELEFON, ADRES_EMAIL, ADRES_OPIEKUNA_ADRES_ID) VALUES (%s, %s, %s, %s, %s, %s, %s)" % param
        f.write(statement + "\n")
    print("dodano do tabeli Opiekun")
    

    dataWeterynarz = [(i, datetime.date(2021, 1, 1) + datetime.timedelta(days=random.randint(1, 365)), random.choice(imiona),
         random.choice(nazwiska), random.choice(telefony)) for i in range(howMuch)]

    SqlWeterynarz = "INSERT INTO WETERYNARZ (WETERYNARZ_ID, DATA_ZATRUDNIENIA, IMIE, NAZWISKO, TELEFON) VALUES (:1, :2, :3, :4, :5)"

    # Wykonujemy polecenie SQL z wygenerowanymi danymi
    cursor.executemany(SqlWeterynarz, dataWeterynarz)
    for param in dataWeterynarz:
        statement = "INSERT INTO WETERYNARZ (WETERYNARZ_ID, DATA_ZATRUDNIENIA, IMIE, NAZWISKO, TELEFON) VALUES (%s, %s, %s, %s, %s)" % param
        f.write(statement + "\n")
    print("dodano do tabeli Weterynarz")

    #INSERT INTO ZWIERZE (zwierze_id, imie,data_urodzenia,od_kiedy,do_kiedy,opis,gatunek_gatunek_id,adopcja_adopcja_id, weterynarz_weterynarz_id,op_opiekun_id) VALUES (1,'Cola',sysdate,sysdate,sysdate,0,1,1,1,1);
    #GATUNEK
    #INSERT INTO "RZĄD"(rzad_id,nazwa) VALUES (1,'drapiezne');
    #INSERT INTO GATUNEK (gatunek_id, nazwa,rodzaj_rodzaj_id) VALUES (5,'Wilk ',5);

    dataRzad = [(i, random.choice(imiona),) for i in range(howMuch)]

    SqlRzad = "INSERT INTO RZĄD (rzad_id,nazwa) VALUES (:1, :2)"

    # Wykonujemy polecenie SQL z wygenerowanymi danymi
    cursor.executemany(SqlRzad, dataRzad)
    for param in dataRzad:
        statement = "INSERT INTO RZĄD (rzad_id,nazwa) VALUES (%s, %s)" % param
        f.write(statement + "\n")
    print("dodano do tabeli Rzad")


    dataRODZINA  = [(i, random.choice(imiona), i) for i in range(howMuch)]

    SqlRODZINA  = "INSERT INTO RODZINA  (rodzina_id, nazwa,RZĄD_RZAD_ID) VALUES (:1, :2, :3)"

    # Wykonujemy polecenie SQL z wygenerowanymi danymi
    cursor.executemany(SqlRODZINA, dataRODZINA)
    for param in dataRODZINA:
        statement = "INSERT INTO RODZINA  (rodzina_id, nazwa,RZĄD_RZAD_ID) VALUES (%s, %s, %s)" % param
        f.write(statement + "\n")
    print("dodano do tabeli Rodzina")


    dataRodzaj = [(i, random.choice(imiona), i) for i in range(howMuch)]

    SqlRodzaj = "INSERT INTO RODZAJ (rodzaj_id, nazwa,rodzina_rodzina_id) VALUES (:1, :2, :3)"

    # Wykonujemy polecenie SQL z wygenerowanymi danymi
    for param in dataRodzaj:
        statement = "INSERT INTO RODZAJ (rodzaj_id, nazwa,rodzina_rodzina_id) VALUES (%s, %s, %s)" % param
        f.write(statement + "\n")
    print("dodano do tabeli Rodzaj")


    dataGatunek = [(i, random.choice(imiona), i) for i in range(howMuch)]

    SqlGatunek = "INSERT INTO GATUNEK (gatunek_id, nazwa,rodzaj_rodzaj_id) VALUES (:1, :2, :3)"

    # Wykonujemy polecenie SQL z wygenerowanymi danymi
    cursor.executemany(SqlGatunek, dataGatunek)
    for param in dataGatunek:
        statement = "INSERT INTO GATUNEK (gatunek_id, nazwa,rodzaj_rodzaj_id) VALUES (%s, %s, %s)" % param
        f.write(statement + "\n")
    print("dodano do tabeli Gatunek")



    # Generujemy 100 wpisów losowych danych dla tabeli OSOBA_ADOPTUJĄCA
    dataOsobaAdoptujaca = [(i, random.choice(imiona), random.choice(nazwiska), random.choice(adresy_email),
         str(random.randint(10000000000, 99999999999)), random.choice(telefony),
         datetime.date(1990, 1, 1) + datetime.timedelta(days=random.randint(1, 10000)),
         i) for i in range(howMuch)]

    # Tworzymy polecenie SQL wstawiające dane do tabeli OSOBA_ADOPTUJĄCA
    sqlOsobaAdoptujaca = "INSERT INTO OSOBA_ADOPTUJĄCA (osoba_adoptujaca_id, imie, nazwisko, adres_email, pesel, telefon, data_urodzenia, \"ADRES_OSOBY_ADOPTUJĄCEJ_ADRES_ID\") VALUES (:1, :2, :3, :4, :5, :6, :7, :8)"

    # Wykonujemy polecenie SQL z wygenerowanymi danymi
    for param in dataOsobaAdoptujaca:
        statement = "INSERT INTO OSOBA_ADOPTUJĄCA (osoba_adoptujaca_id, imie, nazwisko, adres_email, pesel, telefon, data_urodzenia, \"ADRES_OSOBY_ADOPTUJĄCEJ_ADRES_ID\") VALUES (%s, %s, %s, %s, %s, %s, %s, %s)" % param
        f.write(statement + "\n")
    print("dodano do tabeli OsobaAdoptujaca")


    #INSERT INTO ADOPCJA (adopcja_id,data_adopcji,opis_nowego_miejsca,uwagi,"OSOBA_ADOPTUJĄCA_OSOBA_ID") VALUES (1,sysdate,0,0,1);
    # ADOPCJA
    dataAdopcja = [( i, datetime.date(2021, 1, 1) + datetime.timedelta(days=random.randint(1, 365)), random.choice(opis_nowego_miejsca),
         random.choice(uwagi), i) for i in range(howMuch)]


        # Tworzymy polecenie SQL wstawiające dane do tabeli OPIEKUN
    sqlAdopcja = "INSERT INTO ADOPCJA (adopcja_id, data_adopcji, opis_nowego_miejsca, uwagi, OSOBA_ADOPTUJĄCA_OSOBA_ID) VALUES (:1, :2, :3, :4, :5)"


    # Wykonujemy polecenie SQL z wygenerowanymi danymi

    cursor.executemany(sqlAdopcja, dataAdopcja)
    for param in dataAdopcja:
        statement = "INSERT INTO ADOPCJA (adopcja_id, data_adopcji, opis_nowego_miejsca, uwagi, OSOBA_ADOPTUJĄCA_OSOBA_ID) VALUES (%s, %s, %s, %s, %s)" % param
        f.write(statement + "\n")
    print("dodano do tabeli Adopcja")
    # Zwierze
    dataZwierze = [( i, 
                random.choice(imiona), 
                datetime.date(2021, 1, 1) + datetime.timedelta(days=random.randint(1, 365)),
                datetime.date(2021, 1, 1) + datetime.timedelta(days=random.randint(1, 365)), 
                datetime.date(2021, 1, 1) + datetime.timedelta(days=random.randint(1, 365)),
                random.choice(opis_nowego_miejsca),
                i, 
                i, 
                i,
                i) for i in range(howMuch2)]
    


    # Tworzymy polecenie SQL wstawiające dane do tabeli OPIEKUN
    sqlZwierze = "INSERT INTO ZWIERZE (zwierze_id, imie,data_urodzenia,od_kiedy,do_kiedy,opis,gatunek_gatunek_id,adopcja_adopcja_id, weterynarz_weterynarz_id,op_opiekun_id) VALUES (:1, :2, :3, :4, :5, :6, :7, :8, :9, :10)"
    # Wykonujemy polecenie SQL z wygenerowanymi danymi

    cursor.executemany(sqlZwierze, dataZwierze)
    for param in dataZwierze:
        statement = "INSERT INTO ZWIERZE (zwierze_id, imie,data_urodzenia,od_kiedy,do_kiedy,opis,gatunek_gatunek_id,adopcja_adopcja_id, weterynarz_weterynarz_id,op_opiekun_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)" % param
        f.write(statement + "\n")
    print("dodano do tabeli Zwierze")
else:
    print("Dodawanie do wszystkich tabelek")

    dataOpiekun = [( i, datetime.date(2021, 1, 1) + datetime.timedelta(days=random.randint(1, 365)), random.choice(imiona),
    random.choice(nazwiska), random.choice(telefony), random.choice(adresy_email), i) for i in range(howMuch)]


    # Tworzymy polecenie SQL wstawiające dane do tabeli OPIEKUN
    sqlOpiekun = "INSERT INTO OPIEKUN (OPIEKUN_ID, DATA_ZATRUDNIENIA, IMIE, NAZWISKO, TELEFON, ADRES_EMAIL, ADRES_OPIEKUNA_ADRES_ID) VALUES (:1, :2, :3, :4, :5, :6, :7)"


    # Wykonujemy polecenie SQL z wygenerowanymi danymi

    cursor.executemany(sqlOpiekun, dataOpiekun)

    dataWeterynarz = [(i, datetime.date(2021, 1, 1) + datetime.timedelta(days=random.randint(1, 365)), random.choice(imiona),
         random.choice(nazwiska), random.choice(telefony)) for i in range(howMuch)]

    SqlWeterynarz = "INSERT INTO WETERYNARZ (WETERYNARZ_ID, DATA_ZATRUDNIENIA, IMIE, NAZWISKO, TELEFON) VALUES (:1, :2, :3, :4, :5)"

    # Wykonujemy polecenie SQL z wygenerowanymi danymi
    cursor.executemany(SqlWeterynarz, dataWeterynarz)

    #INSERT INTO ZWIERZE (zwierze_id, imie,data_urodzenia,od_kiedy,do_kiedy,opis,gatunek_gatunek_id,adopcja_adopcja_id, weterynarz_weterynarz_id,op_opiekun_id) VALUES (1,'Cola',sysdate,sysdate,sysdate,0,1,1,1,1);
    #GATUNEK
    #INSERT INTO "RZĄD"(rzad_id,nazwa) VALUES (1,'drapiezne');
    #INSERT INTO GATUNEK (gatunek_id, nazwa,rodzaj_rodzaj_id) VALUES (5,'Wilk ',5);

    dataRzad = [(i, random.choice(imiona),) for i in range(howMuch)]

    SqlRzad = "INSERT INTO RZĄD (rzad_id,nazwa) VALUES (:1, :2)"

    # Wykonujemy polecenie SQL z wygenerowanymi danymi
    cursor.executemany(SqlRzad, dataRzad)


    dataRODZINA  = [(i, random.choice(imiona), i) for i in range(howMuch)]

    SqlRODZINA  = "INSERT INTO RODZINA  (rodzina_id, nazwa,RZĄD_RZAD_ID) VALUES (:1, :2, :3)"

    # Wykonujemy polecenie SQL z wygenerowanymi danymi
    cursor.executemany(SqlRODZINA, dataRODZINA)


    dataRodzaj = [(i, random.choice(imiona), i) for i in range(howMuch)]

    SqlRodzaj = "INSERT INTO RODZAJ (rodzaj_id, nazwa,rodzina_rodzina_id) VALUES (:1, :2, :3)"

    # Wykonujemy polecenie SQL z wygenerowanymi danymi
    cursor.executemany(SqlRodzaj, dataRodzaj)


    dataGatunek = [(i, random.choice(imiona), i) for i in range(howMuch)]

    SqlGatunek = "INSERT INTO GATUNEK (gatunek_id, nazwa,rodzaj_rodzaj_id) VALUES (:1, :2, :3)"

    # Wykonujemy polecenie SQL z wygenerowanymi danymi
    cursor.executemany(SqlGatunek, dataGatunek)



    # Generujemy 100 wpisów losowych danych dla tabeli OSOBA_ADOPTUJĄCA
    dataOsobaAdoptujaca = [(i, random.choice(imiona), random.choice(nazwiska), random.choice(adresy_email),
         str(random.randint(10000000000, 99999999999)), random.choice(telefony),
         datetime.date(1990, 1, 1) + datetime.timedelta(days=random.randint(1, 10000)),
         i) for i in range(howMuch)]

    # Tworzymy polecenie SQL wstawiające dane do tabeli OSOBA_ADOPTUJĄCA
    sqlOsobaAdoptujaca = "INSERT INTO OSOBA_ADOPTUJĄCA (osoba_adoptujaca_id, imie, nazwisko, adres_email, pesel, telefon, data_urodzenia, \"ADRES_OSOBY_ADOPTUJĄCEJ_ADRES_ID\") VALUES (:1, :2, :3, :4, :5, :6, :7, :8)"

    # Wykonujemy polecenie SQL z wygenerowanymi danymi
    cursor.executemany(sqlOsobaAdoptujaca, dataOsobaAdoptujaca)


    #INSERT INTO ADOPCJA (adopcja_id,data_adopcji,opis_nowego_miejsca,uwagi,"OSOBA_ADOPTUJĄCA_OSOBA_ID") VALUES (1,sysdate,0,0,1);
    # ADOPCJA
    dataAdopcja = [( i, datetime.date(2021, 1, 1) + datetime.timedelta(days=random.randint(1, 365)), random.choice(opis_nowego_miejsca),
         random.choice(uwagi), i) for i in range(howMuch)]


        # Tworzymy polecenie SQL wstawiające dane do tabeli OPIEKUN
    sqlAdopcja = "INSERT INTO ADOPCJA (adopcja_id, data_adopcji, opis_nowego_miejsca, uwagi, OSOBA_ADOPTUJĄCA_OSOBA_ID) VALUES (:1, :2, :3, :4, :5)"


    # Wykonujemy polecenie SQL z wygenerowanymi danymi

    cursor.executemany(sqlAdopcja, dataAdopcja)
    # Zwierze
    dataZwierze = [( i, 
                random.choice(imiona), 
                datetime.date(2021, 1, 1) + datetime.timedelta(days=random.randint(1, 365)),
                datetime.date(2021, 1, 1) + datetime.timedelta(days=random.randint(1, 365)), 
                datetime.date(2021, 1, 1) + datetime.timedelta(days=random.randint(1, 365)),
                random.choice(opis_nowego_miejsca),
                i, 
                i, 
                i,
                i) for i in range(howMuch)]
    
    # Tworzymy polecenie SQL wstawiające dane do tabeli OPIEKUN
    sqlZwierze = "INSERT INTO ZWIERZE (zwierze_id, imie,data_urodzenia,od_kiedy,do_kiedy,opis,gatunek_gatunek_id,adopcja_adopcja_id, weterynarz_weterynarz_id,op_opiekun_id) VALUES (:1, :2, :3, :4, :5, :6, :7, :8, :9, :10)"
    # Wykonujemy polecenie SQL z wygenerowanymi danymi

    cursor.executemany(sqlZwierze, dataZwierze)


    

# Wykonujemy polecenie SQL z wygenerowanymi danymi
num_rows_inserted = cursor.rowcount

# open a text file in write mode
with open('output.txt', 'w') as f:
    # write the number of rows inserted to the text file
    f.write(f"Number of rows inserted: {num_rows_inserted}")
# Commitujemy zmiany
connection.commit()




# Zamykamy kursor i połączenie
cursor.close()
connection.close()