import socket

def cliente():
    protocolo = input("Digite o protocolo (TCP ou UDP): ").strip().upper()
    mensagem = input("Digite a mensagem a ser enviada: ")

    if protocolo == "TCP":
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tcp_socket:
            tcp_socket.connect(('localhost', 5000))
            tcp_socket.sendall(mensagem.encode())
            resposta = tcp_socket.recv(1024).decode()
            print("Resposta do servidor:", resposta)

    elif protocolo == "UDP":
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as udp_socket:
            udp_socket.sendto(mensagem.encode(), ('localhost', 5001))
            resposta, _ = udp_socket.recvfrom(1024)
            print("Resposta do servidor:", resposta.decode())

    else:
        print("Protocolo inválido. Escolha TCP ou UDP.")

if __name__ == "__main__":
    cliente()
