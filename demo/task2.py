import time
from multiprocessing.connection import Client

def client_function(data):

    wait = data['settings']['wait']
    sock = data['ctx'].conf['settings']['socket']

    print(f'Client: waiting for {wait} seconds for server to become ready')

    time.sleep(wait)

    with Client(sock, 'AF_UNIX') as conn:

        print(f'Client: connected')

        while True:
            msg = conn.recv()
            print(f'Client: received message "{msg}"')
