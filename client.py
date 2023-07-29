import socket
import RSA

def criar_cliente():
    host = socket.gethostname()
    porta = 5000
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    destino = (host, porta)
    client.connect(destino)
    dados = client.recv(1024).decode().split(" ")
    print("Você recebeu a chave pública do servidor: n = " + dados[0] + ", e = " + dados[1])
    print('Para sair, digite 0.\n') 
    mensagem = ''
    while mensagem != '0':
        mensagem = input("Digite uma nova mensagem:")
        criptografado = RSA.cipher(mensagem, int(dados[1]), int(dados[0]))
        criptografado_str = " ".join(criptografado)
        client.send(criptografado_str.encode())
        print("Seu texto criptografado é:", criptografado)
    client.close()

criar_cliente()
