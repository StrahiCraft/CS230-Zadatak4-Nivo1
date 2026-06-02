# 1. Napraviti program u kojem Server1 i Server2 imaju fajl data.txt
# sa više redova teksta. Server1 proverava koje redove Server2 nema
# (na osnovu poređenja sadržaja fajla red po red). Server1 ispisuje u
# konzolu spisak redova koje treba da pošalje, ali ih ne šalje.
# Server2 samo čeka vezu i potvrđuje da je spreman za replikaciju.

import socket

def main():
    hostname = socket.gethostname()
    port = 5000

    server_socket = socket.socket
    server_socket.bind((hostname, port))

    server_socket.listen(1)
    print("Waiting for server 1...")
    conn, adress = server_socket.accept()

    data = []
    with open('data.txt', 'r') as file:
        for line in file:
            data.append(line.strip())

    conn.send(data)
    print("Sent data to server 1...")
    conn.close()

if __name__ == "__main__":
    main()