from pickle import STRING
from socket import*
import hashlib
from DH import*
from internet import*
from Crypto.Cipher import AES

prime = 0
DH_secret = 0
Generate = 0
Server_cal = 0
Client_cal = 0
Shared_key = 0
strings = '[Client] DH key exchange request?[Yy/Nn]'
def server_socket():
    server_sock = socket(AF_INET, SOCK_STREAM) # 소켓 생성
    servername = gethostname() # 네트워크상에 보이는 내 이름
    server_sock.bind(('', 1234)) # 소켓에 주소할당
    server_sock.listen(1) # 소켓에 동시접속자수 할당 및 연결대기
    print("[Server] Wating for Connect")
    sock_connection, addr = server_sock.accept() # 클라이언트의 연결요청 받기(클라이언트와 연결)
    print("[Server] connecting!", str(addr))
    ###########################################################################################

    #################### DH key exchange string send ####################
    sock_connection.send(strings.encode('utf-8'))
    #################### DH key exchange string recv ####################
    data = sock_connection.recv(1024)
    data = data.decode('utf-8')
    ###########################################################################################
    if data == 'y' or data == 'Y':
        print("[Server] DH KEY EXCHANGE START")
        #DH Key Exchange Parameter Gen
        prime = primeGen(512)
        Generate = Gengenerate(32)
        DH_secret = GenSecret(512)
        Server_cal = CalDH(DH_secret, Generate, prime)

        #DH Key Exchange Option, Parameters SEND
        A = str(prime)
        sock_connection.send(A.encode('utf-8'))
        A = str(Generate)
        sock_connection.send(A.encode('utf-8'))
        A = str(Server_cal)
        sock_connection.send(A.encode('utf-8'))

        #Client Cal value RECV
        data = sock_connection.recv(1024)
        data = data.decode('utf-8')
        ##Decryption
        Client_cal = int(data)
        #Shared Key Cal
        Shared_key = Cal_sharedkey(Client_cal, DH_secret, prime)
###########################################################################################
######################################## key 압축 #########################################
        data = str(Shared_key)
        hash = hashlib.sha256()
        hash.update(data.encode('utf-8'))
        data = hash.hexdigest()
        Shared_key = int(data, 16)
        print("[Server] SHA256(Shared_key) = ", Shared_key)
    
        recv_encrypted = sock_connection.recv(1024)
        recv_encrypted = recv_encrypted.decode('utf-8')
        print("[server] client에서 암호화시킨 문자열")
        print(recv_encrypted)

        
        decrypted = AES256Decrypt(Shared_key, encrypted['iv'], encrypted['cipher'])
        print(decrypted)

    server_sock.close() # 소켓 닫기

def main():
    server_socket()

if __name__ == '__main__':
    main()