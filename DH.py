import secrets

##################################################################
#prime section#
##################################################################
#소수인지 확인하는 함수
def isprime(n):
    if n == 1:
        return False
    rot = int(n**(1/2))
    for i in range(2, rot+1):
        if n%i == 0:
            return False
        return True
#정해진 길이(primeLen)을 입력받아 해당 길이만큼 소수를 만드는 함수
def primeGen(primeLen):
    while 1:
        buffer = secrets.randbits(primeLen)
        if isprime(buffer) == True:
            break
    return int(buffer)
##################################################################

##################################################################
#prime section#
##################################################################

#DH에서 개인 키를 생성하는 함수
def GenSecret(GenLen):
    buffer = secrets.randbits(GenLen)
    return (buffer)

#DH에서 Generate를 생성하는 함수
def Gengenerate(GenLen):
       buffer = secrets.randbits(GenLen)
       return (buffer)

#DH에서 상대방에게 전송할 값 (g^x mod p)을 계산하는 함수
def CalDH(Asecret, Generate, prime):
    buffer = pow(Generate, Asecret, prime)
    return (buffer)

#DH에서 상대방에게 받은 키와 자신의 키를 이용하여 (g^{xy} mod p)를 계산하는 함수
def Cal_sharedkey(Bsecret, secret, prime):
    buffer = pow(Bsecret, secret, prime)
    return (buffer)

#메인함수
def main():
    Asecret = GenSecret(256)
    Bsecret = GenSecret(256)
    Generate = GenSecret(32)
    prime = primeGen(512)

    print("A secret = ", hex(Asecret))
    print("B secret = ", hex(Bsecret))
    print("Generator = ", hex(Generate))
    print("prime = ", hex(prime))
    print("============================================================================================================================")
    ACal = CalDH(Asecret, Generate, prime)
    BCal = CalDH(Bsecret, Generate, prime)

    print("A_calculator = ", hex(ACal))
    print("B_calculator = ", hex(BCal))
    print("============================================================================================================================")
    Asharedkey = Cal_sharedkey(BCal, Asecret, prime)
    Bsharedkey = Cal_sharedkey(ACal, Bsecret, prime)
    print("Asharedkey = ", hex(Asharedkey))
    print("Bsharedkey = ", hex(Bsharedkey))
    print("============================================================================================================================")
    if Asharedkey != Bsharedkey:
        print("DH Key exchange Error!")
    else:
        print("DH Key exchange END")

if __name__ == '__main__':
    main()