import socket
from bwt import riordina_bwt
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect(("127.0.0.1", 5000))

frase=input("Scrivi una frase: ")
client.sendall(frase.encode())
risposta=client.recv(1024).decode()

if "$" in risposta:
    print("BWT ricevuto dal server: ", risposta)

    frase_originale=riordina_bwt(risposta)
    print("Frase ricostruita",frase_originale)
else:
    print("Risposta del server: ",risposta)