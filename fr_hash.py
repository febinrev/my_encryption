#!/bin/python3
#######################################################
#        This Algorithm is created by FEBIN           #
#######################################################
def fr_hash(password2):
	password1=password2
	password=password1
	alpha="Í .abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ@#$!^&*{}%/?><[]~_-=:;'1234567890"
	a="@#$!^&*{}%/?><[]~abcdef PQRST_-'"
	b="f3brEV14AB90FRLx623758UZabcdeQYD"
	trans=str.maketrans(a,b)
	if len(password) in range(36,1000):
		password=password
	elif len(password) >= 5:
			password += password * 5
	elif len(password) == 4:
		password += password * 9
	elif len(password) == 3:
		password += password * 12
	elif len(password) == 2:
		addstr=(alpha[alpha.index(password[-1]) % len(alpha)] + password + alpha[alpha.index(password[0]) % len(alpha)] + password[::-1] + alpha[(alpha.index(password[-1]) *  (alpha.index(password[0]) % len(alpha))) ]) + alpha.split(password[0])[0] * 10
		password += addstr[::-1]
	elif len(password) == 1:
		hasher=""
		for i in password:
			pass1=alpha[alpha.index(password)-1:]
			pass2=alpha[:alpha.index(password)+2]
			hasher = pass2 + password + pass1
			password = hasher
	else:
		return "no password given"

	char=""
	for i in password:
		for j in password1:
			try:
				stringval=(alpha.index(i)+alpha.index(j)) % len(alpha)
				string=alpha[stringval]
				char +=string
			except ValueError:
				string=i
				pass
	crypted=""
	for k in char[36:].upper():
		for j in char[:36]:
			x=(alpha.index(k)+alpha.index(j)) % len(alpha)
			y=alpha[x]
			crypted += y
			
		
	
	hashed=crypted.lower().translate(trans)
	c='ABXMLQN". '
	d="2378079105"
	trans2=str.maketrans(c,d)
	hashin=hashed[:36].upper()[::-1].translate(trans2)
	hashall=""
	for i in hashin:
		if i.isdigit():
			i=str((int(i) + 7) % 9)
		else:	
			i=i
		hashall += i
	e="012345678908976018340257109657"
	f="ABCDEFGHIJKLM:;=NOPQRSTUVWXYZa"
	trans3=str.maketrans(f,e)
	hashint1=hashall.translate(trans3)
	hashint2=hashall.translate(trans3)[::-1]
	the_hash=(int(hashint1) * int(hashint2)) % 100000000000000000000000000000000000000000000000000
	g="135792"
	h="4La0Fe"
	trans4=str.maketrans(g,h)
	frhash = str(the_hash)[-1]+str(the_hash)[::-1].translate(trans4).lower()+str(the_hash)[17]
	if len(frhash) < 52:
		frhash = str(frhash) + ("0" * (52-len(frhash)))
	else:
		frhash=frhash
	return frhash
import sys
passwd=sys.argv[1]
if passwd.isascii():
	print(fr_hash(passwd))
else:
	print("Invalid Password!")
