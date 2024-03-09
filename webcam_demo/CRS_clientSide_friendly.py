import socket, pickle

targetResponse = "<missionSpecificPassword>"
clientId= "5582"
isStealthModeActivated = True

class Payload:
    def __init__(self, isStealth, id, password):
        self.isStealth = isStealth
        self.id = id
        self.password = password

    def sendPayload(self):
        return pickle.dumps(self)

def clientMain():
    payload = Payload(isStealthModeActivated, clientId, targetResponse)

    print("Client started")
    hostname = socket.gethostname()  # as both code is running on same computer
    port = 9999  # socket server port number
    client_socket = socket.socket()  # instantiate
    client_socket.connect((hostname, port))  # connect to the server
    print("Sending response to server...")
    client_socket.send(payload.sendPayload())  # send message
    print("Response sent")
    client_socket.close()  # close the connection

if __name__ == "__main__":
    clientMain()