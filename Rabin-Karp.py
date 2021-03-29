import time
#cara lebih laju
'''def RabinKarp(string,searchedString,Q):
    
    M=len(searchedString)
    N=len(string)
    RM=1
    R=10
    p=0#hash for searchedstring
    t=0#hash for string
    for i in range((M-1)):#function to obtain dynamic "pow(d, M-1)%q"
        RM=(R*RM)%Q
    print("RM: "+str(RM))
    #kita pakai cara kat atas sebab kita nak pakai variable yang akan bantu cari modulo bila tambah one by one not M terus

    for j in range(0,len(searchedString)):#to obtain the hashes
        print("j: "+str(j)+" char: "+searchedString[j]+" ascii: "+str(ord(searchedString[j])))
        p=(R*p + ord(searchedString[j]))%Q #hash of searched string(correct hash)
        print("p: "+str(p))
        t=(R*t + ord(string[j]))%Q #hash of the first M chars of the string
        print("t: "+str(t))
    print("p: "+str(p))
    print("t: "+str(t))

    # where everything comes together
    
    if p==t:#if the first 5 chars(up until the 4th index) are equal
        print("awal2 dah sama")
        return "found at index "+ str(i)

    for i in range(M,N):#start searching from the Mth element
        print("i: "+str(i))
        #continue from last t in upper for loopc(line 14)
        t=(t + Q - RM*ord(string[i-M])%Q)%Q#[i-M] sebab nak amik the element yang kelima dari kanan yang dah terlepas [ni bahagian yang bracket merah]
        #t=t+(ord(string[i-M])*(Q-RM)) #boleh guna ^ atau yg ni dua dua boleh
        t=(t * R + ord(string[i]))%Q#ni ikut formula basa, yg ^ ni yang kena tambah sikit(refer gambar kedua dalam nota ipad)
        print("current t value: "+str(t))
        if p==t:
            return "found at index "+ str(i-M+1)

givenString = "3535622653589793"
searchedString = "26535"
Q=997
start =time.time()
index=RabinKarp(givenString,searchedString,Q)
end=time.time()
print(index+" with the running time of "+ str(end-start))
#test q maximum apa
#test kalau ada searched string yang terbalik, tu dia kira gak ke
#explaination, basically after the length M cara kira modulo dia lain sikit sebab nak gunakan and kekalkan interation one by one'''

#impliment loop for RM
'''def RabinKarp(string,searchedString,Q):
    
    M=len(searchedString)
    N=len(string)
    RM=1
    R=10
    p=0#hash for searchedstring
    t=0#hash for string
    for i in range((M-1)):#function to obtain dynamic "pow(d, M-1)%q"
        RM=(R*RM)%Q
    print("RM: "+str(RM))
    

    for i in range(0,M):#to obtain the initial hashes
        print("[p] i: "+str(i)+" char: "+searchedString[i]+" ascii: "+str(ord(searchedString[i])))
        p=( R * p + ord(searchedString[i]))%Q 
        print("p: "+str(p))
        print("[t] i: "+str(i)+" char: "+string[i]+" ascii: "+str(ord(string[i])))
        t=( R * t + ord(string[i]))%Q
        print("t: "+str(t))

    print("\np: "+str(p))
    print("t: "+str(t)+"\n")    
    if p==t:#if the first M chars(up until the [M-1]th index) are equal
        return "found at index 0"

    for i in range(M,N):#start searching from the Mth element
        print("[t] i: "+str(i)+" char: "+string[i]+" ascii: "+str(ord(string[i])))
        t=t+(ord(string[i-M])*(Q-RM)) 
        t=(t * R + ord(string[i]))%Q
        print("t: "+str(t))
        if p==t:
            return "found at index "+ str(i-M+1)

givenString = "algorithmisfun"
searchedString = "fun"
Q=997#divide by modulo to prevent very large hash values
start =time.time()
index=RabinKarp(givenString,searchedString,Q)
end=time.time()
print("\n"+str(index)+" with the running time of "+ str(end-start))'''

#impliment basic formula for RM.
def RabinKarp(string,searchedString,Q):
    
    M=len(searchedString)
    N=len(string)
    R=10
    RM=(R**(M-1)) % Q# Radix for numbers after the Mth number
    p=0#hash for searchedstring
    t=0#hash for string

    for i in range(0,M):#to obtain the initial hashes
        print("[p] i: "+str(i)+" char: "+searchedString[i]+" ascii: "+str(ord(searchedString[i])))
        p=( R * p + ord(searchedString[i]))%Q 
        print("p: "+str(p))
        print("[t] i: "+str(i)+" char: "+string[i]+" ascii: "+str(ord(string[i])))
        t=( R * t + ord(string[i]))%Q
        print("t: "+str(t))

    print("\np: "+str(p))
    print("t: "+str(t)+"\n")    
    if p==t:#if the first M chars(up until the [M-1]th index) are equal
        return "found at index 0"

    for i in range(M,N):#start searching from the Mth element
        print("[t] i: "+str(i)+" char: "+string[i]+" ascii: "+str(ord(string[i])))
        t = ( R * (t - ord(string[i-M])*RM) + ord(string[i])) % Q#impliment apa yang dalam video
        print("t: "+str(t))
        if p==t:
            return "found at index "+ str(i-M+1)

givenString = "algorithmisfun"
searchedString = "fun"
Q=997#divide by modulo to prevent very large hash values
start =time.time()
index=RabinKarp(givenString,searchedString,Q)
end=time.time()
print("\n"+str(index)+" with the running time of "+ str(end-start))