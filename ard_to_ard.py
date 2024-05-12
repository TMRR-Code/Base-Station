# program Server untuk menerima data dari client dan meneruskannya ke program arduino

import socket
import serial

# Inisialisasi socket TCP/IP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#objek serial dengan arduino
ser = serial.Serial('COM5',115200)

# Bind alamat dan port
server_address = ('0.0.0.0', 12345)  # Bind ke semua antarmuka pada port 12345
server_socket.bind(server_address)

# Mendengarkan koneksi masuk
server_socket.listen(1)

print("Menunggu koneksi...")

# Menerima koneksi
connection, client_address = server_socket.accept()

try:
    print("Koneksi dari:", client_address)

    # Loop untuk menerima pesan dari klien dan membalas
    while True:
        data = connection.recv(1024)
        if data:
            print("Diterima:", data.decode())
            data4 = data.decode().strip()
            #data_to_send = f"{data.encode()}\n"
            ser.write((data4 + '\n').encode())
            #response = input("Masukkan pesan balasan untuk client: ")
            #connection.sendall(response.encode())
        else:
            print("Tidak ada data diterima dari", client_address)
            break

finally:
    # Clean up koneksi
    ser.close()
    connection.close()
    server_socket.close()

