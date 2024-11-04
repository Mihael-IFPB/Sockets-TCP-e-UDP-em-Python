import socket
from threading import Thread

def handle_tcp_client(conn, addr):
    print(f"[TCP] Conectado a {addr}")
    data = conn.recv(1024)
    if data:
        response = f"TCP: {data.decode()}"
        conn.sendall(response.encode())
    conn.close()
    print(f"[TCP] Conexão com {addr} encerrada")

def tcp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 5000))
    server_socket.listen()
    print("Servidor TCP escutando na porta 5000...")

    while True:
        conn, addr = server_socket.accept()
        thread = Thread(target=handle_tcp_client, args=(conn, addr))
        thread.start()

def udp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('localhost', 5001))
    print("Servidor UDP escutando na porta 5001...")

    while True:
        data, addr = server_socket.recvfrom(1024)
        print(f"[UDP] Mensagem recebida de {addr}: {data.decode()}")
        response = f"UDP: {data.decode()}"
        server_socket.sendto(response.encode(), addr)

if __name__ == "__main__":
    Thread(target=tcp_server).start()
    Thread(target=udp_server).start()
