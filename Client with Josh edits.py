import socket
import logging
import threading
def readincomingtext(name):  #a function that is basically instructions for the thread to recieve and log messages from the server
    while True:
        data = s.recv(buffer_size)  #makes the variable "data" equal to the data from the server up to the size of the buffer
        data = data.decode()  #decodes the data from it's byte typing into a string
        logging.info("s% i - From Server: " + data, name)  #logs the data with the timestamp of when it was logged

host = "DESKTOP-IK94OT8"  #the hostname of our machine
port = 9447  #the port on the host machine for us to connect to
buffer_size = 1024  #the limit of how much data we will recieve from the server at once

s = socket.socket()  #creates a socket using the default parameters
s.connect((host, port))  #connects the the socket at our port at host machine
s.send(b"Connection with Client Established")  #sends a message to the server saying that this code connected

format = "%(asctime)s: %(message)s"  #sets the format for how the logging info will happen
logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")  #sets the configuration for logging info

x = threading.Thread(target=readincomingtext, args=(1,), daemon=True)  #creates the thread object that will run our readincomingtext function
#takes in the arguement (1,) because otherwise the function take in no parameters and gets annoyed, and then sets it to be
# a daemon thread so that the thread will close when the rest of the code does
x.start()  #tells the thread to start doing it's job

print("\nEnter a message, or [close] to break connection.\n")
print("\n")
while True:
    text = input().encode("utf-8") #encodes the information into a byte so it can be sent to the server
    if text.decode() == "[close]":
        s.send(("The Client has closed the application.").encode("utf-8")) #tells the server that they are closing their application
        break
    s.send(text)
s.close()  #closes the socket so it can be reused