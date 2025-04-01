# Statki (Gra w Statki)

Gra wieloosobowa w Statki zaimplementowana w Pythonie z architekturą klient-serwer. Gra pozwala dwóm graczom połączyć się, rozmieścić swoje statki i na zmianę atakować plansze przeciwnika, aż do momentu wygranej jednego z graczy.

---

## Funkcje

- **Rozgrywka wieloosobowa**: Dwóch graczy może połączyć się z serwerem i grać przeciwko sobie.
- **System turowy**: Gracze wykonują ruchy na zmianę.
- **Aktualizacje w czasie rzeczywistym**: Gra aktualizuje plansze i informuje graczy o trafieniach, pudłach i zatopionych statkach.
- **Interfejs graficzny**: Klient wykorzystuje bibliotekę `pygame` do obsługi graficznego interfejsu użytkownika.
- **Komunikacja klient-serwer**: Serwer obsługuje logikę gry i komunikuje się z klientami za pomocą wiadomości w formacie JSON.

---

## Instalacja

### Wymagania
- Python 3.8 lub nowszy
- Biblioteka `pygame`

### Klonowanie repozytorium
```bash
git clone https://github.com/M3fiUU/Statki
cd Statki
```

### Uruchamianie aplikacji
```
python3 server.py
python3 client_gui (pierwszy gracz)
python3 client_gui (drugi gracz)
```
