import socket

def servidor_udp():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(('0.0.0.0', 5001))

    print("Servidor UDP escutando na porta 5001...")

    while True:
        mensagem, addr = udp_socket.recvfrom(1024)
        print(f"Mensagem UDP recebida de {addr}")
        resposta = "UDP: " + mensagem.decode()
        udp_socket.sendto(resposta.encode(), addr)

if __name__ == "__main__":
    servidor_udp()
