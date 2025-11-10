import socket

def chatbot_response(message):
    message = message.lower()
    if "hello" in message:
        return "Hi there! How can I help you?"
    elif "your name" in message:
        return "I'm PyBot — your friendly Python chatbot"
    elif "time" in message:
        import datetime
        return f"The current time is {datetime.datetime.now().strftime('%H:%M:%S')}"
    elif "bye" in message:
        return "Goodbye! Have a great day!"
    else:
        return "I'm not sure if I understand that. Try something else!"

# Create socket
server = socket.socket()
server.bind(('localhost', 9999))
server.listen(1)

print("Chatbot Server is running... Waiting for connection...")

conn, addr = server.accept()
print(f"Connected with {addr}")

while True:
    data = conn.recv(1024).decode()
    if not data:
        break

    print(f"Client: {data}")
    
    response = chatbot_response(data)
    conn.send(response.encode())

    if "bye" in data.lower():
        break

conn.close()
server.close()
