from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import socket
import threading
import hashlib

#tao server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(5)

#tao khoa
server_key = RSA.generate(2048)

#danh sach client da ket noi
clients = []

#Ham ma hoa thong diep
def encrypt_message(key, message):
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(message.encode(), AES.block_size))
    return cipher.iv + ciphertext

#Ham giai ma thong diep
def decrypt_message(key, encrypt_message):
    iv = encrypt_message[:AES.block_size]
    ciphertext = encrypt_message[AES.block_size:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_message = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return decrypted_message.decode()

#Ham bat tin hieu ket noi den client
def handle_client(client_socket, client_address):
    print(f"Connected with {client_address}")
    
    #Gui khoa cong khai tu server den client
    client_socket.send(server_key.publickey().export_key(format='PEM'))
    
    #Nhan khoa cong khai cua client
    client_received_key = RSA.import_key(client_socket.recv(2048))
    
    #Tao khoa AES cho thong diep ma hoa
    aes_key = get_random_bytes(16)
    
    #Ma hoa khoa AES dang su dung khoa cua client
    cipher_rsa = PKCS1_OAEP.new(client_received_key)
    encrypted_aes_key = cipher_rsa.encrypt(aes_key)
    client_socket.send(encrypted_aes_key)
    
    #them client vao danh sach ket noi
    clients.append((client_socket, aes_key))
    
    while True:
        encrypted_message = client_socket.recv(1024)
        decrypted_message = decrypt_message(aes_key, encrypted_message)
        print(f"Received from {client_address}: {decrypted_message}")
        
        #Gui thong diep da nhan den tat cac ca client con lai
        for client, key in clients:
            if client != client_socket:
                encrypted = encrypt_message(key, decrypted_message)
                client.send(encrypted)
                
        if decrypted_message == "exit":
                break
    
    clients.remove((client_socket, aes_key))
    client_socket.close()
    print(f"Connection with {client_address} closed")
    
#Chap nhan va giu ket noi voi cac client
while True:
    client_socket, client_address = server_socket.accept()
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()