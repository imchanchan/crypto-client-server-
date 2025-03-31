from pickle import*# 이용하면 좋습니다.
from socket import*# 소켓 내장함수 이용하기 위한 import
from DH import*
import hashlib
from internet import*
from Crypto.Cipher import AES

client_sock = socket(AF_INET, SOCK_STREAM) # 소켓 생성
DH_flag = 0
prime = 0
DH_secret = 0
Generate = 0
Server_cal = 0
Client_cal = 0
Shared_key = 0
## 서버와 달리 bind, listen, accept 함수는 없음
def client_socket():
    client_sock.connect(('127.0.0.1', 1234)) # 서버에 연결하는 함수
    ## DH key request
    data = client_sock.recv(1024)
    data = data.decode('ut-f8')
    print(data)
    print("[Client]", end = " ")
    ###########################################################################################
    push = input()
    if push == 'y' or push == 'Y':
        DH_flag = 1
    else :
        DH_flag = 0
    ###########################################################################################
    client_sock.send(push.encode('utf-8')) # 데이터 전송(인코딩해서)
    ###########################################################################################
    if DH_flag == 1:
        print("[Client] DH KEY EXCHANGE START")
        DH_secret = GenSecret(512)

        data = client_sock.recv(1024) #prime
        data = data.decode('utf-8')
        prime = int(data)
        print("Prime Recieve")

        data = client_sock.recv(1024) #Generate
        data = data.decode('utf-8')
        Generate = int(data)
        print("Generate Recieve")

        data = client_sock.recv(1024) #Server_cal
        data = data.decode('utf-8')
        Server_cal = int(data)
        print("Server_cal Recieve")

        Client_cal = CalDH(DH_secret, Generate, prime)
        data = str(Client_cal)
        client_sock.send(data.encode('utf-8'))
        ##Encryption() 
        Shared_key = Cal_sharedkey(Server_cal, DH_secret, prime)
        ###########################################################################################
        ######################################## key 압축 #########################################
        data = str(Shared_key)
        hash = hashlib.sha256()
        hash.update(data.encode('utf-8'))
        data = hash.hexdigest()
        Shared_key = bytes.fromhex(data)
        print("[Client] SHA256(Shared_key) = ", Shared_key)
        #Shared_key = bytes(Shared_key)
        print(len((Shared_key)))
        cipher = AES.new(Shared_key, AES.MODE_ECB)

        text = input()
        plaintext = str(text)

        aes_encrypted = AES256Encrypt(Shared_key, plaintext)
        client_sock.send(aes_encrypted.encode('utl-8'))
        
###########################################################################################
    client_sock.close() # 소켓 닫기

def main():
    client_socket()

if __name__ == '__main__':
    main()