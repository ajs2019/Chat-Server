import socket
import threading

IP = 'localhost'
PORT = 5000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP, PORT))

def receive_data():
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        print(f'Received: {data.decode()}')

receive_thread = threading.Thread(target=receive_data)
receive_thread.start()

while True:
    message = input('Enter message: ')
    if not message:
        break
    client_socket.send(message.encode())

client_socket.close()