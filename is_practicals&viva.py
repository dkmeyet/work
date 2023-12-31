# -*- coding: utf-8 -*-
"""IS_Practicals&Viva

# **Ceasar Cipher**
"""

def encrypt (pt,k):
    result = ""
    for char in pt :
      if char.isalpha():
        start = ord('A') if char.isupper() else ord('a')
        result += chr((ord(char)-start+k)%26 + start)
      else:
          result += char
    return result

pt = input("Enter the message to encrypt: ")
k = int(input("Enter the shift value: "))
encrypted_message = encrypt(pt, k)
print("Encrypted message:", encrypted_message)

def brute_force_caesar_cipher(ciphertext):
    for shift in range(26):
        decrypted_text = ""
        for char in ciphertext:
            if char.isalpha():
                start = ord('A') if char.isupper() else ord('a')
                decrypted_text += chr((ord(char) - start - shift) % 26 + start)
            else:
                decrypted_text += char
        print(f"Shift {shift}: {decrypted_text}")

encrypted_text = "dubdqq"
brute_force_caesar_cipher(encrypted_text)

"""# Vignere Cipher"""

def Vignere(pt, key):
  pt = pt.upper()
  key = key.upper()

  diff = len(pt) - len(key)
  if diff > 0:
    for i in range(diff):
      key += key[i % len(key)]
  # print(pt, key)
  ct = ''
  for i in range(len(pt)):
    temp = 65 + (ord(pt[i]) + ord(key[i])) % 26
    # print(temp)
    ct = ct + chr(temp)
  return ct

ct = Vignere("ARYANNNN", "AYUSH")
print(ct)

"""# Product Cipher"""

#product cipher

def ceaser_cipher (pt, key) :
    ct = ""
    for char in pt:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            ct += chr((ord(char) - start + key) % 26 + start)
        else :
            ct += char
    return ct

def rail_fence (pt, r):
    matrix = [['' for _ in range(len(pt))] for _ in range(r)]
    direction = 1
    row,col = 0,0

    for char in pt :
        matrix[row][col] = char
        row += direction

        if row == 0 or row == r-1:
            direction *= -1

        col += 1

    et = ''.join(''.join(row) for row in matrix)
    return et

def encrypt_product_cipher(plain_text, caesar_key, rail_fence_key):
    encrypted_text = rail_fence(ceaser_cipher(plain_text, caesar_key), rail_fence_key)
    return encrypted_text

plain_text = input("Enter the plain text: ")
caesar_key = int(input("Enter the Caesar key: "))
rail_fence_key = int(input("Enter the Rail Fence key: "))

encrypted_text = encrypt_product_cipher(plain_text, caesar_key, rail_fence_key)
print("Encrypted Text:", encrypted_text)

"""# Rail Fence"""

def rail_fence(pt, r) :
    cipher_matrix = [['' for _ in range(len(pt))] for _ in range(r)]
    direction = 1
    row, col = 0,0

    for char in pt :
        cipher_matrix[row][col] = char
        row += direction

        if row == r - 1 or row == 0 :
            direction *= -1

        col += 1

    encrypted_text = ''.join(''.join(row) for row in cipher_matrix)
    return encrypted_text

pt = "123456789"
r = 3

encrypted_text = rail_fence(pt, r)

print("Original Text:", pt)
print("Encrypted Text:", encrypted_text)

"""# Euclidean algorithms"""

def euclidean_algo(a,b):
    while b:
        a,b = b,a%b
    return a

def extended_euclidean_algorithm(a,b):
    if b == 0 :
        return a,1,0
    else :
        gcd,x,y = extended_euclidean_algorithm(b,a%b)
    return gcd,y,x - (a//b)*y

n1 = int(input("Enter number 1 (bigger) : "))
n2 = int(input("Enter number 2 (smaller) : "))

gcd_result = euclidean_algo(n1,n2)
print(f"GCD of {n1} and {n2} is: {gcd_result}")

ex_gcd_result,x,y = extended_euclidean_algorithm(n1,n2)
print(f'Extended GCD of {n1} and {n2} is : {ex_gcd_result}')
print(f"Coefficients (x, y) are: ({x}, {y})")

"""# RSA"""

# Encryption and Decryption
def euclidean_algo(a,b):
    while b:
        a,b = b,a%b
    return a

p = 17
q = 11
n = p*q
phi = (p-1)*(q-1)
e = 7

while e < phi :
    if euclidean_algo(e,phi) == 1:
        break
    else :
        e += 1
d = pow(e , -1 , phi)
M = 88
print(f'original message : {M}')
C = pow (M,e,n)
print(f'Encrypted message : {C}')
m = pow (C,d,n)
print(f'Decrypted message : {m}')

# RSA - signature
def gcd (a,b) :
    if b== 0:
        return a
    else :
        return gcd(b, a%b)

def hash(message):
    return sum(ord(char) for char in str(message))

p, q = 13, 11
n = p * q
phi = (p - 1) * (q - 1)
e = 13

while e < phi:
    if gcd(e, phi) == 1:
        break
    else:
        e  = e + 1

d = pow(e,-1,phi)
M = 13
print("Message : " ,M)

h = hash(M);
print("Hash value :",h)

signature = pow(h,d,n)
print("Signature : ", signature)

say = pow(signature,e,n) == h
if (say):
    print("Signature valid")
else :
    print("not valid")

"""# Diffie Hellman"""

import math
def diffie_hellman (p,g,a,b):
    ax = pow(g,a) % p
    bx = pow(g,b) % p
    ka = pow(bx,a) % p
    kb = pow(ax,b) % p
    print ( int (ka), int (kb))

diffie_hellman(23,9,4,3)

def diffie_hellman(p, g, b, a):
    Xa = pow(g, a) % p
    Xb = pow(g, b) % p
    Ka = pow(Xb, a) % p
    Kb = pow(Xa, b) % p
    return Xa, Xb, Ka, Kb

# Parameters
p = 23
g = 9

private_d = 11
private_c = 13
# Alice and Bob's private keys
private_a = 4
private_b = 3
# Perform key exchange between Alice and Bob
Xa, Xb, Ka, Kb = diffie_hellman(p, g, private_b, private_a)

# Display the exchanged values
print("Alice sends Xa to Bob:", Xa)
print("Bob sends Xb to Alice:", Xb)

# Malory intercepts communication and pretends to be Alice to Bob
intercepted_Xa = Xa
Darth_sends = intercepted_Xa

# Bob thinks he's talking to Alice, but he's actually talking to Darth
Xb_fake, Xd_fake, Kb_fake, Kd_fake = diffie_hellman(p, g, private_b, private_d)

# Display the exchanged values (Darth's perspective)
print("Darth intercepts Xa:", intercepted_Xa)
print("Darth sends intercepted Xa to Bob:", Darth_sends)
print("Bob sends Xb to Darth:", Xb)
print("Darth sends Xd to Bob:", Xd_fake)

# Alice and Bob calculate their shared secrets, unaware of the attack
shared_secret_alice = pow(Xb_fake, private_a) % p
shared_secret_bob = pow(Darth_sends, private_b) % p

# Display the shared secrets (Darth's perspective)
print("Darth calculates shared secret with Alice:", Kb_fake)
print("Darth calculates shared secret with Bob:", Kd_fake)



"""# Columnar Transposition

"""

import math

def ColumnarTransformation(msg, key):
    col = len(key)
    msg_len = len(msg)
    row = int(math.ceil(msg_len / col))
    fill_null = row * col - msg_len
    msg += '_' * fill_null
    matrix = [list(msg[i: i + col]) for i in range(0, len(msg), col)]
    cipher = ''.join([row[key.index(k)] for k in sorted(key) for row in matrix])
    return cipher, matrix

message = "TWICE 2ND ENGLISH SINGLE"
key = "JANUARY"
cipher ,matrix = ColumnarTransformation(message,key)
for i in matrix:
  print(i)
print(f"Cipher text is :{cipher}")

"""#Row Transposition"""

#row transposition

import math

def row(msg, key):
    col = len(key)
    msg_len = len(msg)
    row = int(math.ceil(msg_len / col))
    fill_null = row * col - msg_len
    msg += '_' * fill_null
    matrix = [list(msg[i:i + row]) for i in range(0, len(msg), row)]
    cipher = ''.join([matrix[key.index(k)][i] for k in sorted(key) for i in range(row)])
    return cipher, matrix

message = "TWICE 2ND ENGLISH SINGLE"
key = "JANUARY"
cipher, matrix = row(message, key)
for i in matrix:
    print(i)
print("Cipher text is:", cipher)



"""# PlayFair

"""

# Plair Fair

def Diagraph(text):
	return [text[i:i+2] for i in range(0, len(text), 2)]

def FillerLetter(text):
	if len(text) % 2 == 0:
		for i in range(0, len(text), 2):
			if text[i] == text[i+1]:
				new_word = text[0:i+1] + str('x') + text[i+1:]
				new_word = FillerLetter(new_word)
				break
			else:
				new_word = text
	else:
		for i in range(0, len(text)-1, 2):
			if text[i] == text[i+1]:
				new_word = text[0:i+1] + str('x') + text[i+1:]
				new_word = FillerLetter(new_word)
				break
			else:
				new_word = text
	return new_word


list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def generateKeyTable(word, list1):
	key_letters = []
	for i in word:
		if i not in key_letters:
			key_letters.append(i)
	compElements = []
	for i in key_letters:
		if i not in compElements:
			compElements.append(i)
	for i in list1:
		if i not in compElements:
			compElements.append(i)

	matrix = []
	while compElements != []:
		matrix.append(compElements[:5])
		compElements = compElements[5:]

	return matrix


def search(mat, element):
	for i in range(5):
		for j in range(5):
			if(mat[i][j] == element):
				return i, j


def encrypt_RowRule(matr, e1r, e1c, e2r, e2c):
	char1 = ''
	if e1c == 4:
		char1 = matr[e1r][0]
	else:
		char1 = matr[e1r][e1c+1]

	char2 = ''
	if e2c == 4:
		char2 = matr[e2r][0]
	else:
		char2 = matr[e2r][e2c+1]

	return char1, char2


def encrypt_ColumnRule(matr, e1r, e1c, e2r, e2c):
	char1 = ''
	if e1r == 4:
		char1 = matr[0][e1c]
	else:
		char1 = matr[e1r+1][e1c]

	char2 = ''
	if e2r == 4:
		char2 = matr[0][e2c]
	else:
		char2 = matr[e2r+1][e2c]
	return char1, char2

def encrypt_RectangleRule(matr, e1r, e1c, e2r, e2c):
	char1 = ''
	char1 = matr[e1r][e2c]

	char2 = ''
	char2 = matr[e2r][e1c]

	return char1, char2


def encryptByPlayfairCipher(Matrix, plainList):
	CipherText = []
	for i in range(0, len(plainList)):
		c1 = 0
		c2 = 0
		ele1_x, ele1_y = search(Matrix, plainList[i][0])
		ele2_x, ele2_y = search(Matrix, plainList[i][1])

		if ele1_x == ele2_x:
			c1, c2 = encrypt_RowRule(Matrix, ele1_x, ele1_y, ele2_x, ele2_y)
		elif ele1_y == ele2_y:
			c1, c2 = encrypt_ColumnRule(Matrix, ele1_x, ele1_y, ele2_x, ele2_y)
		else:
			c1, c2 = encrypt_RectangleRule(
				Matrix, ele1_x, ele1_y, ele2_x, ele2_y)

		cipher = c1 + c2
		CipherText.append(cipher)
	return CipherText


text_Plain = 'attack'
text_Plain = text_Plain.lower().replace(" ", "")
PlainTextList = Diagraph(FillerLetter(text_Plain))
if len(PlainTextList[-1]) != 2:
    PlainTextList[-1] = PlainTextList[-1] + 'z'

key = "MONARCHY"
print("Key text:", key)
key = key.lower()
Matrix = generateKeyTable(key, list1)

print("\nDiagraph:")
print(PlainTextList)

print("\nMatrix:")
for row in Matrix:
    print(row)

CipherList = encryptByPlayfairCipher(Matrix, PlainTextList)

CipherText = ""
for i in CipherList:
    CipherText += i
print("\nCipherText:", CipherText)



"""#"""
