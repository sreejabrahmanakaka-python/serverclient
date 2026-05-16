import socket

host = '127.0.0.1'
port = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

print("Server is running... Waiting for connection...")

conn, addr = server.accept()
print(f"Connected to {addr}")

username = conn.recv(1024).decode()
print(f"{username} joined the chat")

while True:
    message = conn.recv(1024).decode()

    if message.lower() == 'exit':
        print(f"{username} left the chat")
        break

    print(f"{username}: {message}")

    reply = input("You: ")
    conn.send(reply.encode())

conn.close()
server.close()