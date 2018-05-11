num=list(range(5,0,-1))
print(num) 
num[2]=100
print(num)

a=[1,2,3]
total=0
for el in a:
    total+=el
print(total)
total2=sum(a)
print(total2)


b=range(5,0,-1)
total3=sum(b)
print(total3)
'''strA="stone"
strA[0]="Y"
print(strA)這裡是錯誤的 str不能亂動'''

strA="stone"
strA=list(strA)
strA[0]="Y"
print(strA)
print(str(strA))

print(','.join(strA))