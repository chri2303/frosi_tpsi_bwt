import socket
from bwt import calcolo_bwt

with socket.socket(socket.AF_INET, socket.SOCK_STREAM)as server:

    server.bind(("127.0.0.1", 5000))
    server.listen()

    print("Il server e' in ascolto")
    print("Il socket di ascolto e' : ", server.getsocketname())

    conn, addr = server.accept()
    with conn:
        print("Il Client connesso e': ",addr)

        dati= conn.recv(1024)
        frase= dati.decode()
        print("La frase ricevuta e' ", frase)

        if "$"in testo:
            risposta ="ERRORE! nel testo non ci puo' essere il simbolo del dollaro"
        else:
            risposta= calcolo_bwt(frase)
