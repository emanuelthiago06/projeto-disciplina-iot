import socket
import argparse
import matplotlib.pyplot as plt
import requests

# Construct the argument parser


def check_if_int(value):
    try:
        value_int = float(value)
    except:
        return False
    VAL_LIST.append(value_int)
    return True
    

def get_med(val: list):
    return sum(val)/len(val)

def plot_graph(val: list):
    plt.plot(val)
    plt.show()

VAL_LIST = []
HOST = "playback.laced.com.br"
PORT = 50000
device_id = 20211610015

# Create a socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the remote host and port
sock.connect((HOST, PORT))

print("conectado")

# Send a request to the host
sock.send("app\n".encode()[:-1])

# Get the host's response, no more than, say, 1,024 bytes
response_data = sock.recv(1024)

sresponse = response_data.decode("utf-8") 
print(sresponse)

if(sresponse == "fail"):
   sock.close()
   exit()

# Send a request to the host
while True:
    try:
        sock.send((str(device_id)+"\n").encode()[:-1])

        # Get the host's response, no more than, say, 1,024 bytes
        response_data = sock.recv(1024)

        # sresponse = response_data.decode("utf-8") 
        # print(sresponse)

        if(sresponse == "fail"):
            sock.close()
            exit()

        # Get the host's response, no more than, say, 1,024 bytes
        response_data = sock.recv(1024).decode("utf-8")

        if check_if_int(response_data):
            print(f"enviando o dado {response_data}")
            data = {
                "value": response_data
            }
            response = requests.post(url="http://127.0.0.1:8000/api/add-point", data=data)
            print(response)
    except:
        print("Erro detecado, terminando conexão")
        break

# Terminate
sock.close( )
