import random

def prime_numbers():
    j=0
    while j<100:
        odd_number = generate_odd_number()
        i=0
        while i<=10000:
            (variable) flag: Literal[0]
            if pow(a,odd_number-1,odd_number) != 1:  # primality test
                break
            flag=1
            i=i+1
        if flag==1:
            #print(odd_number)
            return odd_number
        j=j+1

prime1=prime_numbers()
print(prime1)
