import time 
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    # wait for req from client
    message = socket.recv()
    print(f"Received request: {message}")

    time.sleep(1)

    socket.send(b"World")