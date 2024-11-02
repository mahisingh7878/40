#check if number is prime

num=int(input("enter the number "))
flag=False
for i in range(2,num):
    if num%i==0:
        flag=True
        break

if flag:
    print(num,"is not prime number ")
else:
    print(num,"ye it is a prime number ")

