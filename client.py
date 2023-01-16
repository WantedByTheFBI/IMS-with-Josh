import socket
host = "Lab120-04"
port = 9440
buffer_size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
while True:
    text = input("What would you like to send?(or enter [close] if you want to stop messaging: ").encode("utf-8")
    if text.decode() == "[close]":
        s.send(("The client has closed the application.").encode("utf-8"))
        break
    s.send(text)
    data = s.recv(buffer_size)
    print("received data:", data)
s.close()
