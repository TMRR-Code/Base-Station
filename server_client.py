# Program server untuk menerima data dari arduino dan meneruskannya ke client

import socket
import serial
import time

# Inisialisasi Objek Serial
ser = serial.Serial('COM5', 9600)

# Inisialisasi socket TCP/IP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind alamat dan port
server_address = ('0.0.0.0', 12345)  # Bind ke semua antarmuka pada port 12345
server_socket.bind(server_address)

# Mendengarkan koneksi masuk
server_socket.listen(2)  # Mengizinkan hingga dua koneksi, satu untuk setiap klien

print("Menunggu koneksi...")

try:
    while True:
        # Menerima koneksi dari client pertama
        connection, client_address = server_socket.accept()
        print("Koneksi dari:", client_address)

        try:
            # Loop untuk menerima pesan dari arduino dan meneruskannya ke klien 
            while True:
                if ser.in_waiting > 0:
                    data = ser.readline().decode().strip()
                    print(data)
                    connection.sendall(data.encode())

        finally:
            # Clean up koneksi untuk klien
            connection.close()

finally:
    # Clean up koneksi untuk server
    ser.close()
    server_socket.close()
