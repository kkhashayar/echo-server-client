import socket, time, os

os.system("clear")
time.sleep(1)

def main():
    print("simple server socket")

    host = "127.0.0.1"
    port = 5000

    print("creating a socket...")
    my_socket = socket.socket()
    time.sleep(1)
    print("socket created!")

    print("bidning socket to: ", host, "/", port)
    my_socket.bind((host, port))
    time.sleep(1)
    print("binding is done")

    my_socket.listen(1)
    print("socket is ready and listening to: ", host, "/", port)

    conn, addr = my_socket.accept()
    print("connection from: " + str(addr))

if __name__ == "__main__":
    main()

    
