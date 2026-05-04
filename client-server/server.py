import const
import zmq

def isPalindrom(string):
  return string == string[::-1]

context = zmq.Context()
socket = context.socket(zmq.REP)  # create reply socket
socket.bind(f"tcp://*:{const.PORT}")  # bind socket to address

while True:
    message = socket.recv()  # wait for incoming message
    if "STOP" in str(message):  break
    string = str(message.decode())
    reply = "PALINDROM" if isPalindrom(string) else "NOT PALINDROM"
    socket.send(reply.encode())  # send it away (encoded)