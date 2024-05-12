# program client untuk menerima data dari server dan meneruskannya ke arduino 

import socket
import serial


# Inisialisasi koneksi serial
ser = serial.Serial('COM5', 9600)

# Inisialisasi socket TCP/IP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Alamat dan port server
server_address = ('192.168.43.209', 12345)  # Ganti dengan alamat IP server dan port yang sesuai

try:
    # Mencoba terhubung ke server
    client_socket.connect(server_address)
    print("Terhubung ke server.")

    # Loop untuk menerima pesan dari server dan mengirimkannya ke Arduino
    while True:
        data = client_socket.recv(1024)
        if  data:
            data4 = data.decode().strip()
            print(data4)
            ser.write((data4 + '\n').encode())
            #time.sleep(0.5)
            #ser.flush()

except ConnectionResetError:
    print("Koneksi dengan server terputus.")

finally:
    # Clean up koneksi
    ser.close()
    client_socket.close()
