import socket

s = socket.socket()
s.connect(('127.0.0.1',12346))
str = input("Your message: ")
s.send(str.encode());
s.close()
