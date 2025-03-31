import os
import hashlib
import csv

def getSHA1(path, blocksize = 65536):
    Targetfile = open(path, 'rb')
    HashGen = hashlib.sha1()
    buf = Targetfile.read(blocksize)
    while len(buf) > 0:
        HashGen.update(buf)
        buf = Targetfile.read(blocksize)
    Targetfile.close
    return HashGen.hexdigest()

def SHA1_test(path):
    fileHash = getSHA1(path)
    print(fileHash)


def main():
    path1 = "C:\\Users\\암호최적화연구실02\\Desktop\\유레카 프로젝트 9주차\\sha_py\\shattered-1.pdf"
    path2 = "C:\\Users\\암호최적화연구실02\\Desktop\\유레카 프로젝트 9주차\\sha_py\\shattered-2.pdf"
    print("######################################################")
    fileHash = getSHA1(path1)
    print("Path1 Hash : " , fileHash)
    fileHash = getSHA1(path2)
    print("Path2 Hash : " , fileHash)
    print("######################################################")
    path3 = "C:\\Users\\암호최적화연구실02\\Desktop\\유레카 프로젝트 9주차\\sha_py\\a.pdf"
    path4 = "C:\\Users\\암호최적화연구실02\\Desktop\\유레카 프로젝트 9주차\\sha_py\\b.pdf"    
    print("######################################################")
    fileHash = getSHA1(path3)
    print("Path3 Hash : " , fileHash)
    fileHash = getSHA1(path4)
    print("Path4 Hash : " , fileHash)
    print("######################################################")

if __name__ == '__main__':
    main()
