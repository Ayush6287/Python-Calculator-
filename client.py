import socket

HOST = '192.168.1.100'  # Replace with SERVER's IP
PORT = 9999

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

data = client.recv(1024).decode()
filename, filesize = data.split('|')
filesize = int(filesize)

print(f"Receiving '{filename}' ({filesize} bytes)...")

with open(filename, 'wb') as f:
    received = 0
    while received < filesize:
        data = client.recv(1024)
        f.write(data)
        received += len(data)

print("File received successfully!")
client.close()
