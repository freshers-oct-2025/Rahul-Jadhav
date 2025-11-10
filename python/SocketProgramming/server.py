import socket

s = socket.socket()
print("Socket Created")

s.bind(('localhost', 9999))
s.listen(3)
print("Waiting for connections.......")

while True:
    c, addr = s.accept()
    print("Connected with", addr)

    name = c.recv(1024).decode()
    print("Client name:", name)

    message = f"Hello {name}, welcome to the network!"
    c.send(message.encode())

    c.close()
