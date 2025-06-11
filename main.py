from tkinter import *  # do tworzenia roota
import tkintermapview

uczelnie: list = []
pracownicy: list = []
studenci: list = []


class Uczelnia:  # definicja klasy - uczelnia
    def __init__(self, nazwa, wojewodztwo):
        self.nazwa = nazwa
        self.wojewodztwo = wojewodztwo
        self.coordinates = self.get_coordinates()
        self.marker = map_widget.set_marker(self.coordinates[0], self.coordinates[1], text=f'{self.nazwa}')

    def get_coordinates(self) -> list:  # funkcja wewnątrz klasy to metoda
        import requests
        from bs4 import BeautifulSoup
        adres_url: str = f'https://pl.wikipedia.org/wiki/{self.nazwa}'
        response_html = BeautifulSoup(requests.get(adres_url).text, 'html.parser')
        return [
            float(response_html.select('.latitude')[1].text.replace(',', '.')),
            float(response_html.select('.longitude')[1].text.replace(',', '.')),
        ]


class Pracownik:  # definicja klasy - uczelnia
    def __init__(self, imie_nazwisko_pracownika, powiat, uczelnia):
        self.imie_nazwisko_pracownika = imie_nazwisko_pracownika
        self.powiat = powiat
        self.uczelnia = uczelnia
        self.coordinates = self.get_coordinates()
        self.marker = map_widget.set_marker(self.coordinates[0], self.coordinates[1],
                                            text=f'{self.imie_nazwisko_pracownika}', marker_color_circle="green")

    def get_coordinates(self) -> list:  # funkcja wewnątrz klasy to metoda
        import requests
        from bs4 import BeautifulSoup
        adres_url: str = f'https://pl.wikipedia.org/wiki/Powiat_{self.powiat}'
        response_html = BeautifulSoup(requests.get(adres_url).text, 'html.parser')
        return [
            float(response_html.select('.latitude')[1].text.replace(',', '.')),
            float(response_html.select('.longitude')[1].text.replace(',', '.')),
        ]


class Student:  # definicja klasy - uczelnia
    def __init__(self, imie_nazwisko_studenta, grupa, uczelnia_studenta):
        self.imie_nazwisko_studenta = imie_nazwisko_studenta
        self.grupa = grupa
        self.uczelnia_studenta = uczelnia_studenta

        self.coordinates = self.get_coordinates()
        self.marker = map_widget.set_marker(self.coordinates[0], self.coordinates[1],
                                            text=f'{self.imie_nazwisko_studenta}', marker_color_circle="yellow")

    def get_coordinates(self) -> list:  # funkcja wewnątrz klasy to metoda
        import requests
        from bs4 import BeautifulSoup
        adres_url: str = f'https://pl.wikipedia.org/wiki/{self.uczelnia_studenta}'
        response_html = BeautifulSoup(requests.get(adres_url).text, 'html.parser')
        return [
            float(response_html.select('.latitude')[1].text.replace(',', '.')),
            float(response_html.select('.longitude')[1].text.replace(',', '.')),
        ]



def zaloguj():
    login = entry_login.get()
    haslo = entry_haslo.get()

    if login == "wat" and haslo == "wat":
        ramka_logowanie.grid_remove()
        ramka_uczelnie.grid(row=1, column=0, sticky="nsew")
        ramka_pracownicy.grid(row=1, column=1, sticky="nsew")
        ramka_studenci.grid(row=1, column=2, sticky="nsew")
        ramka_mapa.grid(row=3, column=0, columnspan=3, sticky="nsew")
    else:
        entry_login.delete(0, END)
        entry_haslo.delete(0, END)
        Label(ramka_logowanie, text="Błędny login lub hasło. Wpisz ponownie", fg="red").grid(row=1, column=0,
                                                                                             columnspan=5)


def add_uczelnia() -> None:
    nazwa = entry_nazwa_uczelni.get()
    wojewodztwo = entry_wojewodztwo.get()

    uczelnia = Uczelnia(nazwa=nazwa, wojewodztwo=wojewodztwo)
    uczelnie.append(uczelnia)

    entry_nazwa_uczelni.delete(0, END)
    entry_wojewodztwo.delete(0, END)

    entry_nazwa_uczelni.focus()
    show_uczelnia()


def show_uczelnia() -> None:
    listbox_uczelnie.delete(0, END)
    for idx, uczelnia in enumerate(uczelnie):
        listbox_uczelnie.insert(idx, f'{idx + 1}. {uczelnia.nazwa}, {uczelnia.wojewodztwo}')


def remove_uczelnia() -> None:
    i = listbox_uczelnie.index(ACTIVE)
    print(i)
    uczelnie[i].marker.delete()
    uczelnie.pop(i)
    show_uczelnia()


def edit_uczelnia() -> None:
    i = listbox_uczelnie.index(ACTIVE)
    wojewodztwo = uczelnie[i].wojewodztwo
    nazwa = uczelnie[i].nazwa

    entry_wojewodztwo.insert(0, wojewodztwo)
    entry_nazwa_uczelni.insert(0, nazwa)

    button_aktualizuj_uczelnie.configure(text='Zapisz', command=lambda: update_uczelnia(i))


def update_uczelnia(i):
    nazwa = entry_nazwa_uczelni.get()
    wojewodztwo = entry_wojewodztwo.get()

    uczelnie[i].nazwa = nazwa
    uczelnie[i].wojewodztwo = wojewodztwo

    uczelnie[i].coordinates = uczelnie[i].get_coordinates()
    uczelnie[i].marker.delete()
    uczelnie[i].marker = map_widget.set_marker(uczelnie[i].coordinates[0], uczelnie[i].coordinates[1],
                                               text=f'{uczelnie[i].nazwa}')

    show_uczelnia()
    button_aktualizuj_uczelnie.configure(text='Aktualizuj', command=edit_uczelnia)  # zmiana właściwosci przycisku

    entry_nazwa_uczelni.delete(0, END)
    entry_wojewodztwo.delete(0, END)

    entry_wojewodztwo.focus()


def add_pracownik() -> None:
    imie_nazwisko_pracownik = entry_pracownik.get()
    powiat_pracownik = entry_powiat.get()
    uczelnia_pracownik = entry_uczelnia_dla_pracownika.get()

    pracownik = Pracownik(imie_nazwisko_pracownika=imie_nazwisko_pracownik, powiat=powiat_pracownik,
                          uczelnia=uczelnia_pracownik)
    pracownicy.append(pracownik)

    entry_pracownik.delete(0, END)
    entry_powiat.delete(0, END)
    entry_uczelnia_dla_pracownika.delete(0, END)

    entry_pracownik.focus()
    show_pracownik()


def show_pracownik() -> None:
    listbox_pracownicy.delete(0, END)
    for idx, pracownik in enumerate(pracownicy):
        listbox_pracownicy.insert(idx,
                                  f'{idx + 1}. {pracownik.imie_nazwisko_pracownika}, powiat {pracownik.powiat}, {pracownik.uczelnia}')


def remove_pracownik() -> None:
    i = listbox_pracownicy.index(ACTIVE)
    print(i)
    pracownicy[i].marker.delete()
    pracownicy.pop(i)
    show_pracownik()


def edit_pracownik() -> None:
    i = listbox_pracownicy.index(ACTIVE)
    imie_nazwisko = pracownicy[i].imie_nazwisko_pracownika
    powiat = pracownicy[i].powiat
    uczelnia = pracownicy[i].uczelnia

    entry_powiat.insert(0, powiat)
    entry_pracownik.insert(0, imie_nazwisko)
    entry_uczelnia_dla_pracownika.insert(0, uczelnia)

    button_aktualizuj_pracownicy.configure(text='Zapisz', command=lambda: update_pracownik(i))


def update_pracownik(i):
    imie_nazwisko = entry_pracownik.get()
    powiat = entry_powiat.get()
    uczelnia = entry_uczelnia_dla_pracownika.get()

    pracownicy[i].imie_nazwisko_pracownika = imie_nazwisko
    pracownicy[i].powiat = powiat
    pracownicy[i].uczelnia = uczelnia

    pracownicy[i].coordinates = pracownicy[i].get_coordinates()
    pracownicy[i].marker.delete()
    pracownicy[i].marker = map_widget.set_marker(pracownicy[i].coordinates[0], pracownicy[i].coordinates[1],
                                                 text=f'{pracownicy[i].imie_nazwisko_pracownika}',
                                                 marker_color_circle="green")

    show_pracownik()
    button_aktualizuj_pracownicy.configure(text='Aktualizuj', command=edit_pracownik)  # zmiana właściwosci przycisku

    entry_pracownik.delete(0, END)
    entry_powiat.delete(0, END)
    entry_uczelnia_dla_pracownika.delete(0, END)

    entry_pracownik.focus()


def add_student() -> None:
    imie_nazwisko = entry_student.get()
    grupa = entry_grupa.get()
    uczelnia = entry_uczelnia_studenci.get()

    student = Student(imie_nazwisko_studenta=imie_nazwisko, grupa=grupa, uczelnia_studenta=uczelnia)
    studenci.append(student)

    entry_student.delete(0, END)
    entry_grupa.delete(0, END)
    entry_uczelnia_studenci.delete(0, END)

    entry_student.focus()
    show_students()


def show_students() -> None:
    listbox_studenci.delete(0, END)
    for idx, student in enumerate(studenci):
        listbox_studenci.insert(idx,
                                f'{idx + 1}. {student.imie_nazwisko_studenta} z grupy {student.grupa} na uczleni: {student.uczelnia_studenta}')


def remove_student() -> None:
    i = listbox_studenci.index(ACTIVE)
    print(i)
    studenci[i].marker.delete()
    studenci.pop(i)
    show_students()


def edit_student() -> None:
    i = listbox_studenci.index(ACTIVE)
    student = studenci[i]

    entry_student.insert(0, student.imie_nazwisko_studenta)
    entry_grupa.insert(0, student.grupa)
    entry_uczelnia_studenci.insert(0, student.uczelnia_studenta)

    button_aktualizuj_studenci.configure(text='Zapisz', command=lambda: update_student(i))


def update_student(i) -> None:
    imie_nazwisko = entry_student.get()
    grupa = entry_grupa.get()
    uczelnia = entry_uczelnia_studenci.get()

    studenci[i].imie_nazwisko_studenta = imie_nazwisko
    studenci[i].grupa = grupa
    studenci[i].uczelnia_studenta = uczelnia

    studenci[i].coordinates = studenci[i].get_coordinates()
    studenci[i].marker.delete()
    studenci[i].marker = map_widget.set_marker(studenci[i].coordinates[0], studenci[i].coordinates[1],
                                               text=f'{studenci[i].imie_nazwisko_studenta}',
                                               marker_color_circle="yellow")

    show_students()
    button_aktualizuj_studenci.configure(text='Aktualizuj', command=edit_student)

    entry_student.delete(0, END)
    entry_grupa.delete(0, END)
    entry_uczelnia_studenci.delete(0, END)

    entry_student.focus()


def pokaz_uczelnia_na_mapie():
    wojewodztwo_do_wyswietlenia = entry_wojewodztwo_zapytanie.get().strip().lower()

    # Usuwamy stare markery
    for uczelnia in uczelnie:
        if hasattr(uczelnia, 'marker') and uczelnia.marker:
            uczelnia.marker.delete()
            uczelnia.marker = None

    # Filtrujemy uczelnie i dodajemy marker'y na mapie
    for uczelnia in uczelnie:
        if uczelnia.wojewodztwo.lower() == wojewodztwo_do_wyswietlenia:
            uczelnia.marker = map_widget.set_marker(uczelnia.coordinates[0], uczelnia.coordinates[1],
                                                    text=uczelnia.nazwa)

    # Opcjonalnie - ustaw widok mapy na pierwszą uczelnię z filtrowanych
    filtered = [u for u in uczelnie if u.wojewodztwo.lower() == wojewodztwo_do_wyswietlenia]
    if filtered:
        map_widget.set_position(filtered[0].coordinates[0], filtered[0].coordinates[1])
        map_widget.set_zoom(10)


def pokaz_wszystkie_uczelnie_na_mapie():
    # Usuwamy stare markery, jeśli istnieją
    for uczelnia in uczelnie:
        if hasattr(uczelnia, 'marker') and uczelnia.marker:
            uczelnia.marker.delete()
            uczelnia.marker = None

    # Dodajemy markery dla wszystkich uczelni
    for uczelnia in uczelnie:
        uczelnia.marker = map_widget.set_marker(
            uczelnia.coordinates[0],
            uczelnia.coordinates[1],
            text=uczelnia.nazwa

        )
    map_widget.set_position(52.23, 21.0)
    map_widget.set_zoom(6)


def pokaz_pracownikow_na_mapie():
    powiat_do_wyswietlenia = entry_powiat_zapytanie.get().strip().lower()
    uczelnia_do_wyswietlenia = entry_uczelnia_zapytanie.get().strip().lower()

    # Usuwamy stare markery
    for pracownik in pracownicy:
        if hasattr(pracownik, 'marker') and pracownik.marker:
            pracownik.marker.delete()
            pracownik.marker = None

    # Filtrujemy uczelnie i dodajemy marker'y na mapie
    dopasowani = []
    for pracownik in pracownicy:
        if (powiat_do_wyswietlenia in pracownik.powiat.lower() and
                uczelnia_do_wyswietlenia in pracownik.uczelnia.lower()):
            pracownik.marker = map_widget.set_marker(pracownik.coordinates[0], pracownik.coordinates[1],
                                                     text=pracownik.imie_nazwisko_pracownika,
                                                     marker_color_circle="green")
            dopasowani.append(pracownik)
    # Opcjonalnie - ustaw widok mapy na pierwszą uczelnię z filtrowanych
    if dopasowani:
        map_widget.set_position(dopasowani[0].coordinates[0], dopasowani[0].coordinates[1])
        map_widget.set_zoom(10)


def pokaz_wszystkich_pracownikow_na_mapie():
    # Usuwamy stare markery, jeśli istnieją
    for pracownik in pracownicy:
        if hasattr(pracownik, 'marker') and pracownik.marker:
            pracownik.marker.delete()
            pracownik.marker = None

    # Dodajemy markery dla wszystkich uczelni
    for pracownik in pracownicy:
        pracownik.marker = map_widget.set_marker(
            pracownik.coordinates[0],
            pracownik.coordinates[1],
            text=pracownik.imie_nazwisko_pracownika,
            marker_color_circle="green"
        )
    map_widget.set_position(52.23, 21.0)
    map_widget.set_zoom(6)


def pokaz_studentow_na_mapie():
    grupa_do_wyswietlenia = entry_grupa_zapytanie.get().strip().lower()
    uczelnia_do_wyswietlenia_studenci = entry_uczelnia_studenci_zapytanie.get().strip().lower()

    # Usuwamy stare markery
    for student in studenci:
        if hasattr(student, 'marker') and student.marker:
            student.marker.delete()
            student.marker = None

    # Filtrujemy uczelnie i dodajemy marker'y na mapie
    dopasowani = []
    for student in studenci:
        if (grupa_do_wyswietlenia in student.grupa.lower() and
                uczelnia_do_wyswietlenia_studenci in student.uczelnia_studenta.lower()):
            student.marker = map_widget.set_marker(student.coordinates[0], student.coordinates[1],
                                                   text=student.imie_nazwisko_studenta, marker_color_circle="yellow")
            dopasowani.append(student)
    # Opcjonalnie - ustaw widok mapy na pierwszą uczelnię z filtrowanych
    if dopasowani:
        map_widget.set_position(dopasowani[0].coordinates[0], dopasowani[0].coordinates[1])
        map_widget.set_zoom(10)


def pokaz_wszystkich_studentow_na_mapie():
    # Usuwamy stare markery, jeśli istnieją
    for student in studenci:
        if hasattr(student, 'marker') and student.marker:
            student.marker.delete()
            student.marker = None

    # Dodajemy markery dla wszystkich uczelni
    for student in studenci:
        student.marker = map_widget.set_marker(
            student.coordinates[0],
            student.coordinates[1],
            text=student.imie_nazwisko_studenta,
            marker_color_circle="yellow"
        )
    map_widget.set_position(52.23, 21.0)
    map_widget.set_zoom(6)


root = Tk()
root.geometry("1400x800")
root.title('StudentBook')

from tkinter import *

# Konfiguracja siatki
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(3, weight=1)

# RAMKI
ramka_logowanie = LabelFrame(root, text="🔐 Panel logowania", padx=10, pady=10)
ramka_uczelnie = LabelFrame(root, text="🏫 Uczelnie (kolor czerwony)", padx=10, pady=10)
ramka_pracownicy = LabelFrame(root, text="👨‍🏫 Pracownicy (kolor zielony)", padx=10, pady=10)
ramka_studenci = LabelFrame(root, text="🎓 Studenci (kolor żółty)", padx=10, pady=10)
ramka_mapa = LabelFrame(root, text="🗺️ Mapa", padx=10, pady=10)

ramka_logowanie.grid(row=0, column=0, columnspan=3, sticky="nsew")

# LOGOWANIE
Label(ramka_logowanie, text="Login: ").grid(row=0, column=0)
entry_login = Entry(ramka_logowanie)
entry_login.grid(row=0, column=1, sticky="ew", padx=5)

Label(ramka_logowanie, text="Hasło: ").grid(row=0, column=2)
entry_haslo = Entry(ramka_logowanie, show="*")
entry_haslo.grid(row=0, column=3, sticky="ew", padx=5)

button_zaloguj = Button(ramka_logowanie, text="Zaloguj", command=zaloguj)
button_zaloguj.grid(row=0, column=4, padx=10)

# UCZELNIE
listbox_uczelnie = Listbox(ramka_uczelnie, width=70, height=8)
listbox_uczelnie.grid(row=0, column=0, columnspan=4, sticky="ew")

Label(ramka_uczelnie, text="Województwo:").grid(row=1, column=0, sticky=W)
entry_wojewodztwo = Entry(ramka_uczelnie)
entry_wojewodztwo.grid(row=1, column=1, columnspan=3, sticky="ew")

Label(ramka_uczelnie, text="Nazwa uczelni:").grid(row=2, column=0, sticky=W)
entry_nazwa_uczelni = Entry(ramka_uczelnie)
entry_nazwa_uczelni.grid(row=2, column=1, columnspan=3, sticky="ew")

Label(ramka_uczelnie, text="Z którego województwa wyswietlić?").grid(row=5, column=0, sticky=W)
entry_wojewodztwo_zapytanie = Entry(ramka_uczelnie)
entry_wojewodztwo_zapytanie.grid(row=5, column=1, columnspan=3, sticky="ew")

button_dodaj_uczelnie = Button(ramka_uczelnie, text="Dodaj", command=add_uczelnia)
button_dodaj_uczelnie.grid(row=4, column=0, sticky="ew")
button_usun_uczelnie = Button(ramka_uczelnie, text="Usuń", command=remove_uczelnia)
button_usun_uczelnie.grid(row=4, column=1, sticky="ew")
button_aktualizuj_uczelnie = Button(ramka_uczelnie, text="Aktualizuj", command=edit_uczelnia)
button_aktualizuj_uczelnie.grid(row=4, column=2, sticky="ew")
button_pokaz_uczelnie = Button(ramka_uczelnie, text="Pokaż", command=pokaz_uczelnia_na_mapie)
button_pokaz_uczelnie.grid(row=6, column=3, sticky="ew")
button_mapa_uczelnie_wszystkie = Button(ramka_uczelnie, text="Mapa", command=pokaz_wszystkie_uczelnie_na_mapie)
button_mapa_uczelnie_wszystkie.grid(row=4, column=3, sticky="ew")

# PRACOWNICY
listbox_pracownicy = Listbox(ramka_pracownicy, width=70, height=8)
listbox_pracownicy.grid(row=0, column=0, columnspan=4, sticky="ew")

Label(ramka_pracownicy, text="Powiat:").grid(row=1, column=0, sticky=W)
entry_powiat = Entry(ramka_pracownicy)
entry_powiat.grid(row=1, column=1, columnspan=3, sticky="ew")

Label(ramka_pracownicy, text="Uczelnia:").grid(row=2, column=0, sticky=W)
entry_uczelnia_dla_pracownika = Entry(ramka_pracownicy)
entry_uczelnia_dla_pracownika.grid(row=2, column=1, columnspan=3, sticky="ew")

Label(ramka_pracownicy, text="Imię i nazwisko:").grid(row=3, column=0, sticky=W)
entry_pracownik = Entry(ramka_pracownicy)
entry_pracownik.grid(row=3, column=1, columnspan=3, sticky="ew")

Label(ramka_pracownicy, text="Z którego powiatu wyswietlić?").grid(row=6, column=0, sticky=W)
entry_powiat_zapytanie = Entry(ramka_pracownicy)
entry_powiat_zapytanie.grid(row=6, column=1, columnspan=3, sticky="ew")

Label(ramka_pracownicy, text="Z której uczelni wyswietlić?").grid(row=7, column=0, sticky=W)
entry_uczelnia_zapytanie = Entry(ramka_pracownicy)
entry_uczelnia_zapytanie.grid(row=7, column=1, columnspan=3, sticky="ew")

button_dodaj_pracownicy = Button(ramka_pracownicy, text="Dodaj", command=add_pracownik)
button_dodaj_pracownicy.grid(row=5, column=0, sticky="ew")
button_usun_pracownicy = Button(ramka_pracownicy, text="Usuń", command=remove_pracownik)
button_usun_pracownicy.grid(row=5, column=1, sticky="ew")
button_aktualizuj_pracownicy = Button(ramka_pracownicy, text="Aktualizuj", command=edit_pracownik)
button_aktualizuj_pracownicy.grid(row=5, column=2, sticky="ew")
button_pokaz_pracownikow = Button(ramka_pracownicy, text="Pokaż", command=pokaz_pracownikow_na_mapie)
button_pokaz_pracownikow.grid(row=8, column=3, sticky="ew")
button_mapa_pracownicy_wszystkie = Button(ramka_pracownicy, text="Mapa", command=pokaz_wszystkich_pracownikow_na_mapie)
button_mapa_pracownicy_wszystkie.grid(row=5, column=3, sticky="ew")

# STUDENCI
listbox_studenci = Listbox(ramka_studenci, width=70, height=8)
listbox_studenci.grid(row=0, column=0, columnspan=4, sticky="ew")

Label(ramka_studenci, text="Grupa:").grid(row=1, column=0, sticky=W)
entry_grupa = Entry(ramka_studenci)
entry_grupa.grid(row=1, column=1, columnspan=3, sticky="ew")

Label(ramka_studenci, text="Uczelnia:").grid(row=2, column=0, sticky=W)
entry_uczelnia_studenci = Entry(ramka_studenci)
entry_uczelnia_studenci.grid(row=2, column=1, columnspan=3, sticky="ew")

Label(ramka_studenci, text="Imię i nazwisko:").grid(row=3, column=0, sticky=W)
entry_student = Entry(ramka_studenci)
entry_student.grid(row=3, column=1, columnspan=3, sticky="ew")

Label(ramka_studenci, text="Z którego grupy wyswietlić?").grid(row=6, column=0, sticky=W)
entry_grupa_zapytanie = Entry(ramka_studenci)
entry_grupa_zapytanie.grid(row=6, column=1, columnspan=3, sticky="ew")

Label(ramka_studenci, text="Z której uczelni wyswietlić?").grid(row=7, column=0, sticky=W)
entry_uczelnia_studenci_zapytanie = Entry(ramka_studenci)
entry_uczelnia_studenci_zapytanie.grid(row=7, column=1, columnspan=3, sticky="ew")

button_dodaj_studenci = Button(ramka_studenci, text="Dodaj", command=add_student)
button_dodaj_studenci.grid(row=4, column=0, sticky="ew")
button_usun_studenci = Button(ramka_studenci, text="Usuń", command=remove_student)
button_usun_studenci.grid(row=4, column=1, sticky="ew")
button_aktualizuj_studenci = Button(ramka_studenci, text="Aktualizuj", command=edit_student)
button_aktualizuj_studenci.grid(row=4, column=2, sticky="ew")
button_pokaz_studentow = Button(ramka_studenci, text="Pokaż", command=pokaz_studentow_na_mapie)
button_pokaz_studentow.grid(row=8, column=3, sticky="ew")
button_mapa_studenci_wszystkie = Button(ramka_studenci, text="Mapa", command=pokaz_wszystkich_studentow_na_mapie)
button_mapa_studenci_wszystkie.grid(row=4, column=3, sticky="ew")

# MAPA
map_widget = tkintermapview.TkinterMapView(ramka_mapa, width=1400, height=450, corner_radius=0)
map_widget.grid(row=0, column=0)
map_widget.set_position(52.23, 21.0)
map_widget.set_zoom(6)

root.mainloop()
