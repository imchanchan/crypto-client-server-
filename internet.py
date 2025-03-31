import hashlib

import Crypto

import Crypto.Random

from Crypto.Cipher import AES



def gen_sha256_hashed_key_salt(key):

	salt1 = hashlib.sha256(key).digest()

	return hashlib.sha256(salt1+key).digest()



def gen_random_iv():

	return Crypto.Random.OSRNG.posix.new().read(AES.block_size)



def AES256Decrypt(key, iv, cipher):

	encryptor = AES.new(gen_sha256_hashed_key_salt(key), AES.MODE_CBC, IV=iv)

	plain = encryptor.decrypt(cipher)

	plain = plain[0:-ord(plain[-1])]

	return plain



def AES256Encrypt(key, plain):

	length = AES.block_size - (len(plain) % AES.block_size)

	plain += chr(length)*length

	iv = gen_random_iv()

	encryptor = AES.new(gen_sha256_hashed_key_salt(key), AES.MODE_CBC, IV=iv)

	return {'cipher': encryptor.encrypt(plain), 'iv': iv}


if __name__ == '__main__':
    
    key = 'password123qwe'

    encrypted = AES256Encrypt(key, 'Let me tell you the huge secret! The king has a donkey ear')

    decrypted = AES256Decrypt(key, encrypted['iv'], encrypted['cipher'])

    print (decrypted)



