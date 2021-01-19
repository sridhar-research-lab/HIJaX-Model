import socket
import threading

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
cookie_arr = []
counter = 1
call_cnt = 0
cnt_flag = True

def handle_client(conn, addr):
    global counter
    global call_cnt
    call_cnt += 1
    if call_cnt % 2 == 0:
        call_cnt = 0
        counter += 1

    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True

    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            if 'PHPSESSID=' in str(msg_length):
                start_idx = str(msg_length).find('PHPSESSID=') + 10
                cookie_arr.append(str(msg_length)[start_idx:])
            else:
                connected = False
            '''msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"[{addr}] {msg}")
            conn.send("Msg received".encode(FORMAT))'''

    print('len:',counter)
    conn.close()

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

print("[STARTING] server is starting...")
start()
