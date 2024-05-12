# program Client untuk mengirimkan data dari arduino ke server

import socket
import serial 
#import time 

# Inisialisasi socket TCP/IP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Inisialisasi koneksi serial
ser = serial.Serial('COM4', 115200) # Sesuaikan 'COM3' dengan port Arduino yang Anda gunakan
#time.sleep(2) # Tunggu 2 detik untuk koneksi serial stabil

# Alamat dan port server
server_address = ('192.168.43.209', 12345)  # Ganti dengan alamat IP server dan port yang sesuai

# Mencoba terhubung ke server
client_socket.connect(server_address)

try:
    # Kirim pesan ke server
    while True:
        if ser.in_waiting > 0:
            data = ser.readline().decode().strip()
            client_socket.sendall(data.encode())

        # Menerima balasan dari server
        #data = client_socket.recv(1024)
        #print("Server:", data.decode())
except KeyboardInterrupt:
    # Menekan Ctrl+C untuk keluar dari program
    ser.close() # Tutup koneksi serial saat program berhenti
    print("Program berhenti.")
finally:
    # Clean up koneksi
    client_socket.close()
