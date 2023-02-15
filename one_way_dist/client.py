import sys
import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB)

socket.connect("tcp://localhost:5556")
print("Connect to Server...")

zip_filter = sys.argv[1] if len(sys.argv) > 1 else "10001"
socket.setsockopt_string(zmq.SUBSCRIBE, zip_filter)


total_temp = 0
for i in range(5):
    string = socket.recv_string()
    print(string)
    zipcode, temperature, relhumidity = string.split()
    total_temp += int(temperature)

    print((f"Average temperature for zipcode "
           f"'{zip_filter}' was {total_temp / (i+1)} F"))
