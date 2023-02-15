import zmq

context = zmq.Context()

print("Server Connecto")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

print(f"Current libzmq version is {zmq.zmq_version()}")
print(f"Current  pyzmq version is {zmq.__version__}")

# Do 10 requests
for request in range(10):
    print(f"Sending request {request} ...")
    socket.send(b"Hello")
   # Get reply
    message = socket.recv()
    print(f"Received Reply {request} [{message}]")
