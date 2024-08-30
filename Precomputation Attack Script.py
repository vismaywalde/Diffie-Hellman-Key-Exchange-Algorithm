prime=23
proot=5
private_key=2716053  # secret key
l=[]
i=0
while i<=prime-2:
    l.append(pow(proot,i,prime))
    i=i+1

# given public key
remain=14  # remainder
# challenge to find the a
i=0
while i<=prime-2:
    if l[i]==remain:
        break
    i=i+1
print(i)  # periodicity

p=1
test=21+(22*p)
while test!= private_key:
    p=p+1
    test=21+(22*p)
print(test)
