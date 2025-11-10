import socket

c = socket.socket()
c.connect(('localhost', 9999))

name = input("Enter your name: ")

c.send(name.encode())       

response = c.recv(1024).decode()  
print(response)

c.close()
