from tkinter import * #do tworzenia roota
import tkintermapview

uczelnie: list =[]
pracownicy: list =[]
studenci: list =[]


class Uczelnia: #definicja klasy - uczelnia
    def __init__(self, nazwa, wojewodztwo):
        self.nazwa = nazwa
        self.wojewodztwo = wojewodztwo

        #self.coordinates = self.get_coordinates()
        #self.marker = map_widget.set_marker(self.coordinates[0], self.coordinates[1],
        #                                   text=f'{self.nazwa})

    # def get_coordinates(self) -> list:  # funkcja wewnątrz klasy to metoda
    #     import requests
    #     from bs4 import BeautifulSoup
    #     adres_url: str = f'https://pl.wikipedia.org/wiki/{self.location}'
    #     response_html = BeautifulSoup(requests.get(adres_url).text, 'html.parser')
    #     return [
    #         float(response_html.select('.latitude')[1].text.replace(',', '.')),
    #         float(response_html.select('.longitude')[1].text.replace(',', '.')),
    #     ]
    #

class Pracownik: #definicja klasy - uczelnia
    def __init__(self, imie_nazwisko_pracownika, powiat, uczelnia):
        self.imie_nazwisko_pracownika = imie_nazwisko_pracownika
        self.powiat = powiat
        self.uczelnia = uczelnia

        #self.coordinates = self.get_coordinates()
        #self.marker = map_widget.set_marker(self.coordinates[0], self.coordinates[1],
        #                                   text=f'{self.nazwa})

    # def get_coordinates(self) -> list:  # funkcja wewnątrz klasy to metoda
    #     import requests
    #     from bs4 import BeautifulSoup
    #     adres_url: str = f'https://pl.wikipedia.org/wiki/{self.location}'
    #     response_html = BeautifulSoup(requests.get(adres_url).text, 'html.parser')
    #     return [
    #         float(response_html.select('.latitude')[1].text.replace(',', '.')),
    #         float(response_html.select('.longitude')[1].text.replace(',', '.')),
    #     ]
    #

class Student: #definicja klasy - uczelnia
    def __init__(self, imie_nazwisko_studenta, grupa, uczelnia_studenta):
        self.imie_nazwisko_studenta = imie_nazwisko_studenta
        self.grupa = grupa
        self.uczelnia_studenta = uczelnia_studenta

        #self.coordinates = self.get_coordinates()
        #self.marker = map_widget.set_marker(self.coordinates[0], self.coordinates[1],
        #                                   text=f'{self.nazwa})

    # def get_coordinates(self) -> list:  # funkcja wewnątrz klasy to metoda
    #     import requests
    #     from bs4 import BeautifulSoup
    #     adres_url: str = f'https://pl.wikipedia.org/wiki/{self.location}'
    #     response_html = BeautifulSoup(requests.get(adres_url).text, 'html.parser')
    #     return [
    #         float(response_html.select('.latitude')[1].text.replace(',', '.')),
    #         float(response_html.select('.longitude')[1].text.replace(',', '.')),
    #     ]
    #






# Funkcja logowania
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
        Label(ramka_logowanie, text="Błędny login lub hasło. Wpisz pon ownie", fg="red").grid(row=1, column=0,
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
        listbox_uczelnie.insert(idx, f'{idx + 1}. {uczelnia.nazwa}')

def remove_uczelnia() -> None:
    i = listbox_uczelnie.index(ACTIVE)
    #print(i)
    #uczelnie[i].marker.delete()
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

    # uczelnie[i].coordinates = users[i].get_coordinates()
    # uczelnie[i].marker.delete()
    # czelnie[i].marker = map_widget.set_marker(uczelnie[i].coordinates[0], uczelnie[i].coordinates[1],
    #                                         text=f'{uczelnie[i].nazwa}}')

    show_uczelnia()
    button_aktualizuj_uczelnie.configure(text='Aktualizuj', command=edit_uczelnia)  # zmiana właściwosci przycisku

    entry_nazwa_uczelni.delete(0, END)
    entry_wojewodztwo.delete(0, END)


    entry_wojewodztwo.focus()

def add_pracownik() -> None:
    imie_nazwisko_pracownik = entry_pracownik.get()
    powiat_pracownik = entry_powiat.get()
    uczelnia_pracownik = entry_uczelnia_dla_pracownika.get()


    pracownik = Pracownik(imie_nazwisko_pracownika=imie_nazwisko_pracownik, powiat=powiat_pracownik, uczelnia=uczelnia_pracownik)
    pracownicy.append(pracownik)

    entry_pracownik.delete(0, END)
    entry_powiat.delete(0, END)
    entry_uczelnia_dla_pracownika.delete(0, END)

    entry_pracownik.focus()
    show_pracownik()

def show_pracownik() -> None:
    listbox_pracownicy.delete(0, END)
    for idx, pracownik in enumerate(pracownicy):
        listbox_pracownicy.insert(idx, f'{idx + 1}. {pracownik.imie_nazwisko_pracownika}')

def remove_pracownik() -> None:
    i = listbox_pracownicy.index(ACTIVE)
    # print(i)
    # uczelnie[i].marker.delete()
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

    # uczelnie[i].coordinates = users[i].get_coordinates()
    # uczelnie[i].marker.delete()
    # czelnie[i].marker = map_widget.set_marker(uczelnie[i].coordinates[0], uczelnie[i].coordinates[1],
    #                                         text=f'{uczelnie[i].nazwa}}')

    show_pracownik()
    button_aktualizuj_pracownicy.configure(text='Aktualizuj', command=edit_pracownik)  # zmiana właściwosci przycisku

    entry_pracownik.delete(0, END)
    entry_powiat.delete(0, END)
    entry_uczelnia_dla_pracownika.delete(0, END)


    entry_pracownik.focus()





root = Tk()
root.geometry("1400x800")
root.title('StudentBook')

from tkinter import *

# Konfiguracja siatki (dynamiczne rozciąganie)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(3, weight=1)

# RAMKI
ramka_logowanie = LabelFrame(root, text="🔐 Panel logowania", padx=10, pady=10)
ramka_uczelnie = LabelFrame(root, text="🏫 Uczelnie", padx=10, pady=10)
ramka_pracownicy = LabelFrame(root, text="👨‍🏫 Pracownicy", padx=10, pady=10)
ramka_studenci = LabelFrame(root, text="🎓 Studenci", padx=10, pady=10)
ramka_mapa = LabelFrame(root, text="🗺️ Mapa", padx=10, pady=10)

ramka_logowanie.grid(row=0, column=0, columnspan=3, sticky="nsew")

# Ukryj pozostałe ramki na start (nie dodawaj ich do grid jeszcze jak nie jesteś zalogowany)
ramka_uczelnie.grid_remove()
ramka_pracownicy.grid_remove()
ramka_studenci.grid_remove()
ramka_mapa.grid_remove()

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

button_dodaj_uczelnie = Button(ramka_uczelnie, text="Dodaj", command=add_uczelnia)
button_dodaj_uczelnie.grid(row=4, column=0, sticky="ew")
button_usun_uczelnie = Button(ramka_uczelnie, text="Usuń", command=remove_uczelnia)
button_usun_uczelnie.grid(row=4, column=1, sticky="ew")
button_aktualizuj_uczelnie = Button(ramka_uczelnie, text="Aktualizuj", command=edit_uczelnia)
button_aktualizuj_uczelnie .grid(row=4, column=2, sticky="ew")
button_mapa_uczelnie = Button(ramka_uczelnie, text="Mapa").grid(row=4, column=3, sticky="ew")

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

button_dodaj_pracownicy = Button(ramka_pracownicy, text="Dodaj",command=add_pracownik)
button_dodaj_pracownicy.grid(row=5, column=0, sticky="ew")
button_usun_pracownicy = Button(ramka_pracownicy, text="Usuń",command=remove_pracownik)
button_usun_pracownicy.grid(row=5, column=1, sticky="ew")
button_aktualizuj_pracownicy = Button(ramka_pracownicy, text="Aktualizuj", command=edit_pracownik)
button_aktualizuj_pracownicy.grid(row=5, column=2, sticky="ew")
button_mapa_pracownicy = Button(ramka_pracownicy, text="Mapa").grid(row=5, column=3, sticky="ew")

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

Button_dodaj_studenci = Button(ramka_studenci, text="Dodaj").grid(row=4, column=0, sticky="ew")
Button_usun_studenci = Button(ramka_studenci, text="Usuń").grid(row=4, column=1, sticky="ew")
Button_aktualizuj_studenci = Button(ramka_studenci, text="Aktualizuj").grid(row=4, column=2, sticky="ew")
Button_mapa_studenci = Button(ramka_studenci, text="Mapa").grid(row=4, column=3, sticky="ew")

# MAPA
Label(ramka_mapa, text="Tu mogłaby być mapa lub wizualizacja współrzędnych...").pack(expand=True)

root.mainloop()
