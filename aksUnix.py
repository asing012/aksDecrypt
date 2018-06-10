#!/usr/bin/env python
# Akshay Singh
# Decyrpts Unix Password using dictionary attack

import crypt

def testPass(encryptText): # to decrypt pass  
    passSalt = encryptText[0:2] # 2 characters to get the salt
    dictFile = open('dictionary.txt','r')
    for word in dictFile.readlines():
        word = word.strip('\n')
        dictCrypt = crypt.crypt(word,passSalt)
        if (dictCrypt == encryptText):
            print("\t\t "+"Password Found: "+word)
            return
    print("\t\t "+"Password Not Found")
    return

def main():
    passFile = open('encryptPass.txt') 
    print("\nWelcome to aksUnix \n")
    for password in passFile.readlines():
        if ":" in password: #if the txt file has user:password
            user = password.split(':')[0]
            encryptText = password.split(':')[1].strip('\n')
            print("[+] "+ "Decrypting password for: "+user)
            testPass(encryptText)
        else: #if the txt file doesn't have user:password
            encryptText = password.strip('\n')
            print("[+] "+ "Decrypting password for Unknown User: ")
            testPass(encryptText)

if __name__ == "__main__":
    main()
