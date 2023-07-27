import threading
import socket

def receive_data(conn, filename):
    with open(filename, "wb") as file:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            file.write(data)

def main():
    host = "172.20.10.13"
    port = 12345


    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print("等待连接...")

    while True:
        conn, addr = server_socket.accept()
        print("连接已建立：", addr)


        file_name_length_bytes = conn.recv(4)
        file_name_length = int.from_bytes(file_name_length_bytes, 'big')

        # 接收文件名并解码
        file_name_bytes = conn.recv(file_name_length)
        file_name = file_name_bytes.decode('utf-8')

        # 在新的线程中接收数据
        thread = threading.Thread(target=receive_data, args=(conn, file_name))
        thread.start()

if __name__ == "__main__":
    main()
