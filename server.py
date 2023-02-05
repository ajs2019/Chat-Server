import socket
import threading

IP = 'localhost'
PORT = 5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((IP, PORT))
server_socket.listen(5)

print(f'Server listening on {IP}:{PORT}')

clients = []

def handle_client(client_socket, client_address):
    client_socket.send(b'Welcome to the chatroom!')
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        for c in clients:
            if c != client_socket:
                c.send(data)
    client_socket.close()
    clients.remove(client_socket)

while True:
    client_socket, client_address = server_socket.accept()
    print(f'Accepted connection from {client_address[0]}:{client_address[1]}')
    clients.append(client_socket)
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()

server_socket.close()