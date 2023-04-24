import socket

resp = "S"

while(resp == "S"):
    url = input("Digite uma url: ")
    ip = socket.gethostbyname(url)
    print(ip)
    resp=input("Digite <s> para continuar: ").upper()
