key_=[[0]*3 for i in range(3)]
plain_text_matrix=[[0] for i in range(3)]
res=[[0] for i in range(3)]
dic = {
    'a': 0,'b': 1,'c': 2,'d': 3,'e': 4,
    'f': 5,'g': 6,'h': 7,'i': 8,'j': 9,
    'k': 10,'l': 11,'m': 12,'n': 13,'o': 14,
    'p': 15,'q': 16,'r': 17,'s': 18,'t': 19,
    'u': 20,'v': 21,'w': 22,'x': 23,'y': 24,
    'z': 25
}
def hillcipher():
    x=""
    cipher=[]
    for i in range(3):
        for j in range(1):
            res[i][j]=0
            for k in range(3):
                res[i][j]+=key_[i][k]*plain_text_matrix[k][j]
            res[i][j]%=26
    for i in range(len(res)):
        value=res[i][0]
        for k,v in dic.items():
            if v==value:
                cipher.append(k)
    for i in cipher:
        x+=i
    return x
should_continue=True
while should_continue:
    direction = input("Type 'e' to encrypt, type 'd' to decrypt: ").lower()
    plain_text = input("Type your message: ").lower()
    key=input("Type your key:").lower()
    k=0
    for i in range(3):
        for j in range(3):
            key_[i][j]=dic[key[k]]
            k+=1
    print("Key matrix")        
    for row in key_:
        print(row)
    for i in range(3):
        plain_text_matrix[i][0]=dic[plain_text[i]]
    print("Plain text matrix")
    for row in plain_text_matrix:
        print(row)
    res=hillcipher()
    print("Encrypted matrix")
    for row in res:
        print(row)
    print(res)
    repeat = input("Do you want to go again? Y or N\n").lower()
    if repeat == 'n':
        should_continue = False