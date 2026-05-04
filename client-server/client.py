import const
import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)  # create request socket

socket.connect(f"tcp://{const.HOST}:{const.PORT}")  # block until connected
socket.send(b"araraaa")  # send message
message = socket.recv()  # block until response
socket.send(b"STOP")  # tell server to stop
print(message.decode())