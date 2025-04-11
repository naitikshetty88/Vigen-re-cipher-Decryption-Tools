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
            x = (ord(cipher[i])-ord(key[i])-32+126)%127
            if x<32:
              x=x-32+126
        plaintext.append(chr(x))
    return("".join(plaintext))
#Input Function
ciphertext=input("Provide the ciphertext here: ")
#have made certain adjustments to the ciphertext since some of the ciphertext characters are python commands and hence were giving an error. Final answer adjusted accordingly.
Key=input("Provide the key here: ")
print(Key)
key1 = RepeatKey(ciphertext, Key)
print(" For Key: " +  Key + " Decrypted text: " + decryption(ciphertext, key1))