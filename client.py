import socket
import json
from game_logic import place_all_ships_manual, print_board

HOST = 'localhost'
PORT = 5555

def main():
    print("🔌 Łączenie z serwerem...")
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    # 1. Rozmieść statki
    board, ships = place_all_ships_manual()

    # 2. Wyślij planszę i listę statków do serwera
    data = {
        "board": board,
        "ships": ships
    }
    client.sendall(json.dumps(data).encode())

    # 3. Odbierz info od serwera
    msg = client.recv(1024).decode()
    print("[SERVER]:", json.loads(msg)["msg"])

    # 4. Czekaj na start gry
    msg = client.recv(1024).decode()
    print("[SERVER]:", json.loads(msg)["msg"])

    while True:
        try:
            print_board(board)
            print("🔫 Twój ruch!")
            x = int(input("Podaj X (0-9): "))
            y = int(input("Podaj Y (0-9): "))

            move = json.dumps({"x": x, "y": y})
            client.sendall(move.encode())

            # Odbierz wynik
            response = client.recv(1024).decode()
            result = json.loads(response)

            if result["hit"] and result["sunk"]:
                print("🔥 Trafiony i zatopiony!")
            elif result["hit"]:
                print("🎯 Trafiony!")
            else:
                print("❌ Pudło!")

            if result["game_over"]:
                print("🏆 Wygrałeś grę!")
                break

            print("⏳ Czekaj na swoją turę...")

        except Exception as e:
            print("❌ Błąd klienta:", e)
            break

    client.close()

if __name__ == "__main__":
    main()
