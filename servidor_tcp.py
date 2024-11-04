import socket

def servidor_tcp():
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.bind(('0.0.0.0', 5000))
    tcp_socket.listen()

    print("Servidor TCP escutando na porta 5000...")

    while True:
        conn, addr = tcp_socket.accept()
        print(f"Conexão TCP recebida de {addr}")
        mensagem = conn.recv(1024).decode()
        resposta = "TCP: " + mensagem
        conn.sendall(resposta.encode())
        conn.close()

if __name__ == "__main__":
    servidor_tcp()

