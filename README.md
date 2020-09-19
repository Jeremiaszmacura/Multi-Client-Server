<!-- Heading -->
## Multi-Client-Server in Python
<!-- Links -->
#### Jeremiasz Macura
[Multi-Client-Server in Python on github](https://github.com/Jeremiaszmacura/Multi-Client-Server-in-Python)
### Opis
<!-- UL -->
* Projekt został napisany samodzielnie w Pythonie używając modułów takich jak min.: socket, threading, PyQt5.
Serwera z klientami komunikuje się za komocą socketów, a każdy nowy klient jest obsługiwany na nowym wątku. 
GUI zostało stworzone przy pomocy nakładki na bibliotekę Qt - PyQt5.
* Po uruchomieniu programu, pokaże nam się okno głowne stworzone przy pomocy PyQt5
* W oknie głownym programu mamy 4 sekcje: włączania/wyłączania serwera, listy aktywnych połączeń, wysyłania wiadomości
 do klientów, przepływu informacji
* W pierwszej sekcji po naciśnieciu przycisku, z ikoną włącznika, serwer zostanie uruchomiony i zacznie nasłuchiwanie.
* W drugiej sekcji wyświetla się lista użytkowników połączonych do serwera, przedstawijąc ich IP i numer portu
* W trzeciej sekcji posiadamy możliwość wysłania wiadomości do konkretnego klienta połączonego z serwerem poprzez
 podanie jego IP i numeru portu.
* W czwartej sekcji widzimy wiadomości, które sa wysyłane pomiędzy klientami, a serwerem.
