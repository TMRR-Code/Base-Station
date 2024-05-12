#Program Client untuk menerima data dari server dan meneruskannya ke arduino

import socket
import serial

#inisialisasi objek serial
ser = serial.Serial('COM4', 115200)

# Inisialisasi socket TCP/IP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Alamat dan port server
server_address = ('192.168.43.209', 12345) # Ganti dengan alamat IP server dan port yang sesuai

try:
    # Mencoba terhubung ke server
    client_socket.connect(server_address)
    print("Terhubung ke server.")

    # Loop untuk menerima pesan dari server dan mengirimkannya ke Arduino
    while True:
        data = client_socket.recv(1024)
        if data:
            print("Diterima dari server:", data.decode())
            data4 = data.decode().strip()
            # Mengirim data ke Arduino melalui koneksi serial
            ser.write((data4 + '\n').encode())  # Menambahkan newline dan mengubah ke bytes sebelum mengirim

except ConnectionResetError:
  print("Koneksi dengan server terputus.")

except serial.SerialException as e:
  print("Terjadi kesalahan serial:", e) # Pernyataan print untuk menangkap kesalahan serial

finally:
  # Clean up koneksi
  ser.close()
  client_socket.close()