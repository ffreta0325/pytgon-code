def prList(arr):
    for idx,el in enumerate(arr):
        if(idx!=len(arr)-1):
            print(el,end=",")
        else:
            print(el)
a=[10,20,30,40,50]
b=[30,4,56]
prList(a)
prList(b)

def emumList(arr):
    for idx,el in enumerate(arr):
        print(idx+1,",",el)
emumList(["apple","orange","banana"])