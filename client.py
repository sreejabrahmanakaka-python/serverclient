import socket

host = '127.0.0.1'
port = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

username = input("Enter your name: ")
client.send(username.encode())

while True:
    message = input("You: ")
    client.send(message.encode())

    if message.lower() == 'exit':
        print("You left the chat")
        break

    reply = client.recv(1024).decode()
    print(f"Server: {reply}")

client.close()