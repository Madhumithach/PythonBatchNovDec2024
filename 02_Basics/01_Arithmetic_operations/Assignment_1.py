num=1234
sum=0
while num!=0:
    (quo,rem)=divmod(num,10)
    sum=sum+rem
    num=quo
print(sum)

