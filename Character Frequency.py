
ciphertext = input("Enter your input prompt here : ")
charfreq = {} 
for i in ciphertext:
    if i in charfreq:
        charfreq[i] = charfreq[i] + 1
    else:
        charfreq[i] = 1
print( "Output\n"+ str(charfreq))