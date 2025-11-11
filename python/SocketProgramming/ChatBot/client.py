import socket

client = socket.socket()
client.connect(('localhost', 9999))
print("Connected to Chatbot! Type 'bye' to exit.\n")

while True:
    msg = input("You: ")
    client.send(msg.encode())

    if msg.lower() == "bye":
        break

    response = client.recv(1024).decode()
    print("Bot:", response)

client.close()
