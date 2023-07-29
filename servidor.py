import socket
import RSA 


def criar_servidor_rsa(n, e, d):
    host = socket.gethostname()
    porta = 5000
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    endereco_origem = (host, porta)
    server.bind(endereco_origem)
    server.listen(1)
    conexao, endereco_cliente = server.accept()
    print('Conexão estabelecida com:', endereco_cliente)
    conexao.send((str(n) + " " + str(e)).encode())
    mensagem = ''
    print("Aguardando dados do cliente:")
    while mensagem != '0':
        mensagem = conexao.recv(1024).decode()
        mensagem_descifrada = RSA.decipher(mensagem.split(" "), n, d)
        if not mensagem:
            break
        print(f'Mensagem recebida do cliente: {mensagem}')
        print(f'Mensagem decriptografada: {mensagem_descifrada}')
    print('Finalizando conexão com o cliente', endereco_cliente)
    conexao.close()

p = 17
q = 13
n = p * q
x = RSA.totient(p)
y = RSA.totient(q)
totiente_de_n = x * y
e = RSA.generate_e(totiente_de_n)
chave_publica = (n, e)
print("Sua chave pública é:", chave_publica)
chave_privada = RSA.calculate_private_key(totiente_de_n, e)
print('Sua chave privada é:', chave_privada)

criar_servidor_rsa(n, e, chave_privada)
