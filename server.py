import socket
import os

HOST = '0.0.0.0'  # Listen on all interfaces
PORT = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)
print(f"Server listening on port {PORT}...")

conn, addr = server.accept()
print(f"Client connected from {addr}")

filename = input("Enter filename to send: ")
if os.path.exists(filename):
    filesize = os.path.getsize(filename)
    conn.send(f"{filename}|{filesize}".encode())
    
    with open(filename, 'rb') as f:
        sent = 0
        while sent < filesize:
            data = f.read(1024)
            conn.send(data)
            sent += len(data)
    print(f"File '{filename}' sent successfully!")
else:
    print("File not found!")

conn.close()
server.close()
