import time
from multiprocessing.connection import Listener

class Server:

    def __init__(self, name, data):

        # Name of this module as defined in flow: { name: ... }
        self.name = name

        # Get own settings defined in settings: { name: { ... } }
        self.message = data['settings']['message']

        # We can also access items from the global ctx
        self.sock_path = data['ctx'].conf['settings']['socket']

    def run_server(self):

        self.listener = Listener(self.sock_path, 'AF_UNIX')
        print(f"Server: started listener at {self.sock_path}")

        while True:
            conn = self.listener.accept()
            print(f"Server: connection accepted")

            msg_id = 1

            while True:
                message = (f'msg id: {msg_id}, from: {self.name}, msg: {self.message}')
                print(f'Server: sending messge "{message}"')
                conn.send(message)

                msg_id += 1

                time.sleep(2)

            time.sleep(2)
