alphabets = " !#$%&'()*+,-./0123456789:;<>?@ABCDEFGHIJKLMNOPQRSTUVWXYZUVWXYZ[]^`abcdefghijklmnopqrstuvwxyz{|}~"
#Keygeneration
def RepeatKey(cipher, key):
    key=list(key)
    if len(cipher)==len(key):
        return(key)
    else:
        for i in range(len(cipher)-len(key)):
            key.append(key[i%len(key)])
    return("".join(key))
#DecrytionFunction
def decryption(cipher, key):
    plaintext = []
    for i in range(len(cipher)):
        if(ord(cipher[i])>ord(key[i])):
            x=(ord(cipher[i])-ord(key[i]))%127
            if x<32:
                x=x-32+126
        else:
            x = (ord(cipher[i])-ord(key[i])-31+126)%127
            if x<32:
              x=x-32+126
        plaintext.append(chr(x))
    return("".join(plaintext))
#Input
ciphertext=input("Provide the ciphertext here: ")
#Bruteforce
for i in range(97):
  for j in range(97):
    for k in range(97):      
          key=alphabets[i]+alphabets[j]+alphabets[k]
          key1 = RepeatKey(ciphertext, key)
          print("For Key:", key + " Decrypted text:", decryption(ciphertext, key1))