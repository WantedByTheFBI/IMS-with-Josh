
import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 1234
print(host)# Reserve a port for your service.
s.bind((host, port))
s.listen(15)# Bind to the port
while True:
   c, addr = s.accept()     # Establish connection with client.
   print('Got connection from', addr)
   c.send('Thank you for connecting')
   c.close()                # Close the connection
