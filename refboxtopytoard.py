#Program untuk menerima data berupa karakter di refbox dan meneruskannya ke arduino

import socket
import serial
#import time

#objek serial dengan arduino
ser = serial.Serial('COM5',9600)

def terima_pesan(s):
    while True:
        pesan_balasan = s.recv(1024)
        if not pesan_balasan:
            print("Koneksi terputus secara tak terduga.")
            break
        print("Pesan Diterima: " + pesan_balasan.decode().strip())
        data = pesan_balasan.decode().strip()
        ser.write((data + '\n').encode())
        #time.sleep(2)



# buat objek socket
s = socket.socket()
# tentukan alamat IP dan port Tujuan
ip_address = '192.168.43.209'
port = 28097 

# hubungkan ke alamat IP dan port Tujuan
s.connect((ip_address,port))
print("Terhubung ke: " + ip_address)
terima_pesan(s)

ser.close()
s.close()