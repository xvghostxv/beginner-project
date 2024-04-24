import socket
from _thread import start_new_thread

server = "127.0.0.1"
port = 5555

def threaded_client(conn):
    conn.send(str.encode('connected'))
    reply =""
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode('utf-8')

            if not data:
                print('disconnected')
                break
            else:
                print('received: ', reply)
                print('sending : ', reply)

            conn.sendall((str.encode(reply)))
        except Exception as e:
            print('Exception occurred:', str(e))
            break

    print('lost connection')
    conn.close() 

def start_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.bind((server, port))
    except socket.error as e:
        print('Socket error occurred:', str(e))

    s.listen(2)
    print('waiting for a connection, Server Started')
    
    while True:
        conn, addr = s.accept()
        print('connected to:', addr)

        start_new_thread(threaded_client, (conn,))

if __name__ == "__main__":
    start_server()
