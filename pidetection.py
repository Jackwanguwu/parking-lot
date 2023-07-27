
import cv2
import csv
import socket
def Camaro_image():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        cv2.imshow("Collecting images", frame)
        k = cv2.waitKey(1)

        if k == ord('q'):
            break
        elif k == ord('s'):
            file_path='/home/pi/pythonproject/imageone/image01.jpg'
            file_name='../aigame/image01.jpg'
            cv2.imwrite(file_path, frame)

            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect(('172.20.10.13', 12345))

            with open(file_path, 'rb') as file:
                file_content = file.read()

            # 发送文件名的长度和文件名
            file_name_length = len(file_name.encode('utf-8'))
            sock.sendall(file_name_length.to_bytes(4, 'big'))
            sock.sendall(file_name.encode('utf-8'))

            # 发送文件内容
            sock.sendall(file_content)


        elif k == ord('l'):
            file_path='/home/pi/pythonproject/imagetwo/image02.jpg'
            file_name='image02.jpg'
            cv2.imwrite(file_path, frame)

            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect(('172.20.10.13', 12345))

            with open(file_path, 'rb') as file:
                file_content = file.read()

            # 发送文件名的长度和文件名
            file_name_length = len(file_name.encode('utf-8'))
            sock.sendall(file_name_length.to_bytes(4, 'big'))
            sock.sendall(file_name.encode('utf-8'))

            # 发送文件内容
            sock.sendall(file_content)

           




Camaro_image()
