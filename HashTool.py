import hashlib                                          # HASH TOOL
print("""
          _______  _______            _________ _______  _______  _
|\     /|(  ___  )(  ____ \|\     /|  \__   __/(  ___  )(  ___  )( 
| )   ( || (   ) || (    \/| )   ( |     ) (   | (   ) || (   ) || (
| (___) || (___) || |      | (___) |     | |   | |   | || |   | || |
|  ___  ||  ___  || |      |  ___  |     | |   | |   | || |   | || |
| (   ) || (   ) || |      | (   ) |     | |   | |   | || |   | || |
| )   ( || )   ( || (____/\| )   ( |     | |   | (___) || (___) || (____/
|/     \||/     \|(_______/|/     \|     )_(   (_______)(_______)(_______/
""")
print("""
Hash Tool v0.0.1 by Youssef /dark-lime-0 \n
==========================================================================================================
 Hash Checker [1] , Hash Length [2] , Hash Type [3] , Text Encryption [4] , Hash Decryption [5] , Exit [0]
==========================================================================================================
""")
def encryption(text,type):
    if(type=='md5'):
        hl = hashlib.md5()
    elif(type == 'sha1'):
        hl = hashlib.sha1()
    elif(type == 'sha224'):
        hl = hashlib.sha224()
    else:
        hl = hashlib.sha256()
    hl.update(text.encode("utf-8"))
    b = hl.hexdigest()
    return b
def hash_type(hash):
    if (len(hash) == 32):
        tp = 'md5'
    elif (len(hash) == 40):
        tp = 'sha1'
    elif (len(hash) == 56):
        tp = 'sha224'
    elif (len(hash) == 64):
        tp = 'sha256'
    else:
        tp = 'Unknown'
    return tp
try:
    while (True):
        a = int(input(" >> Enter a number : "))
        c = ['md5', 'sha1', 'sha224', 'sha256']
        if (a == 1):
            print(" You Choose [1]:[The Hash Checker]")
            h1 = input("1# ")
            h2 = input("2# ")
            if (h1 == h2):
                print("The Hash is clean !")
            else:
                print("The Hash isn't clean !")
        elif (a == 2):
            print(" You Choose [2]:[Hash Length]")
            h = input("# ")
            print("The Hash Length is : ", len(h))
        elif (a == 3):
            print(" You Choose [3]:[Hash Type]")
            h = input("# : ")
            print(f'The Hash Type is : [{hash_type(h)}]')
        elif (a == 4):
            print(" You Choose [4]:[Text Encryption]")
            t = input("Enter The Text : ")
            h = input("Enter The Hash Type :[MD5 - SHA1 - SHA224 - SHA256]: ").lower()
            if (h in c):
                print(encryption(t, h))
            else:
                print("Invalid Hash type Please Try Again!!")
        elif (a == 5):
            print("You choose [5]:[Hash Decryption]; Req: hash & WordList :")
            hash = input("# ")
            h_type=hash_type(hash)
            if (h_type=='Unknown'):
                print("Invalid Hash !!")
                exit(1)

            wordlist = input("Enter The wordlist : ")
            try:
                with open(wordlist, 'r') as f:
                    for word in f.readlines():
                        word = word[:-1]
                        enc = encryption(word, h_type)
                        if (hash == enc):
                            print("the hash is decrypted : ", word)
                            exit(0)
                    print("the hash is not decrypted ")
            except Exception as e:
                print(f"An error occurred: {str(e)}")
        elif (a == 0): exit(0)
        else:
            print("Invalid Input !!")
except Exception :
    print("\n Error PLEASE TRY AGAIN !!")
    exit(1)

# dark : a82fd95db10ff25dfad39f07372ebe37