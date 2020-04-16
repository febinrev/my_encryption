#!/usr/bin/python3
import hashlib
import readline
import os
def encrypt(filepath,outfile,keyinit1):
	if os.path.isfile(filepath):
		space={' ':"?"}
		newline={'\n':"~"}
		alpha="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890/><!@#$%^&*()-+_=[]{}?.,;:'`"
		f=open(filepath,"r+")
		text1=f.read()[::-1]
		f.close()
		keyinit=keyinit1[-1]+keyinit1+keyinit1[0]
		keyhash1=hashlib.md5(keyinit.encode())
		key1=str(keyhash1.hexdigest())
		keyhash2=hashlib.sha512(key1.encode())
		key=str(keyhash2.hexdigest())
		#print(key)
		print("")
		spacetran1=str.maketrans(space)
		text2=text1.translate(spacetran1)
		newlinetran=str.maketrans(newline)
		text3=text2.translate(newlinetran)
		text=text3
		keysum=0
		for keyletter in keyinit1:
			sumof=alpha.index(keyletter)
			keysum += sumof
		char=""
		for i in text:
			for j in key:
				try:
					stringval=(alpha.index(i)+alpha.index(j)) % len(alpha)
					string=alpha[stringval]
					char +=string
				except ValueError:
					string=i
					pass
		keylen=len(key)
		keyPos=0
		encrypted = ""
		for ch in text:
			keyChr = key[keyPos]
			newChr = ord(ch)
			newChr = chr(((newChr + ord(keyChr) + len(keyinit)) + keysum) % 301)
			encrypted += newChr
			keyPos += 1
			keyPos = keyPos % keylen
		o=open(outfile,"w+")
		o.write(encrypted)
		o.close()
		return encrypted
	else:
		return "Error : Input File not found"

def decrypt(filepath,outfile,keyinit1):
	if os.path.isfile(filepath):
		keyinit=keyinit1[-1]+keyinit1+keyinit1[0]
		keyhash1=hashlib.md5(keyinit.encode())
		key1=str(keyhash1.hexdigest())
		keyhash2=hashlib.sha512(key1.encode())
		key=str(keyhash2.hexdigest())
		keylen=len(key)
		keyPos=0
		f=open(filepath,"r+", encoding="UTF-8")
		text=f.read()
		f.close()
		keylen=len(key)
		alpha="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890/><!@#$%^&*()-+_=[]{}?.,;:'`"
		keypos=0
		keysum=0
		for keyletter in keyinit1:
			sumof=alpha.index(keyletter)
			keysum += sumof
		decrypted1=""
		for ch in text:	
			keychr=key[keypos]
			newchr=ord(ch)
			newchr=chr(((newchr - ord(keychr) - len(keyinit)) - keysum) % 301)
			decrypted1 += newchr
			keypos += 1
			keypos = keypos % keylen
		space={'?':" "}
		newline={'~':"\n"}
		spacetran1=str.maketrans(space)
		decrypted2=decrypted1.translate(spacetran1)
		newlinetran=str.maketrans(newline)
		decrypted3=decrypted2.translate(newlinetran)
		decrypted=decrypted3
		char=""
		for i in text:
			for j in key:
				try:
					stringval=(alpha.index(i)-alpha.index(j)) % len(alpha)
					string=alpha[stringval]
					char +=string
				except ValueError:
					string=i
					pass
		char=decrypted
		o=open(outfile,"w+")
		o.write(decrypted[::-1])
		o.close()
	else:
		return "Error : Input File not found"



try:
	print("""THIS IS AN ENCRYPTION ALGORITHM CREATED BY   FEBIN 
                               FEBREV ENCRYPTION STANDARD
	Encryption is Fun!!!!
	""")
	choice=input("[1] Encrypt  [2] Decrypt   Enter Your Choice :> ")
	if choice=="1":
		filein=input("Enter the path of the text file to encrypt : ")
		key=input("Enter the secretKey for encryption :")
		outfile=input("Enter the file to write crypted ciphertext : ")
		print(f"Writing to {outfile} .....")
		encrypt(filein,outfile,key)
	elif choice=="2":
		filein=input("Enter the path of the text file to decrypt : ")
		key=input("Enter the secretKey for decryption :")
		outfile=input("Enter the file to write deccrypted plaintext : ")
		print(f"Writing to {outfile} .....")
		decrypt(filein,outfile,key)



except KeyboardInterrupt:
	print("   User Exit..............")
	print("Encryption is Fun........")
except UnicodeDecodeError:
	print("  The file You given is not a proper English text file")
