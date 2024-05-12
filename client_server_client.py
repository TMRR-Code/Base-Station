#Program Server Untuk Menerima data dari client1 dan meneruskannya ke client2

import socket

# Inisialisasi socket TCP/IP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind alamat dan port
server_address = ('0.0.0.0', 12345)  # Bind ke semua antarmuka pada port 12345
server_socket.bind(server_address)

# Mendengarkan koneksi masuk
server_socket.listen(2)  # Mengizinkan hingga dua koneksi, satu untuk setiap klien

print("Menunggu koneksi...")

# Menerima koneksi dari client pertama
connection1, client_address1 = server_socket.accept()
print("Koneksi dari:", client_address1)

# Menerima koneksi dari client kedua
connection2, client_address2 = server_socket.accept()
print("Koneksi dari:", client_address2)

try:
    # Loop untuk menerima pesan dari klien ppertama dan meneruskannya ke klien kedua
    while True:
        data = connection1.recv(1024)
        if data:
            print("Diterima dari client 1:", data.decode())
            connection2.sendall(data)
        else:
            print("Tidak ada data diterima dari client 1")
            break

finally:
    # Clean up koneksi
    connection1.close()
    connection2.close()
    server_socket.close()
