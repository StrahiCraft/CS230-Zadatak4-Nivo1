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
    server_socket.connect((hostname, port))

    server2_data = []
    server2_data = server_socket.recv(1024).decode()

    data = []
    with open('data.txt', 'r') as file:
        for line in file:
            data.append(line.strip())

    for line in data:
        if not server2_data.__contains__(line):
            print(line)

    server_socket.close()

if __name__ == "__main__":
    main()