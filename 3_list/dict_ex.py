ages={}
def prAge(name):
    if ages.get(name):
        print(name, ages.get(name))
    else:
        print("haha")
def test():
    num = int(input())
    for i in range(0,num):
        line = input()
        tokens=line.strip().split()
        name= tokens[0]
        age = int(tokens[1])
        ages[name]=age
    print(ages)
    num = int(input())
    for i in range(0,num):
        line = input()
        #print(line)
        prAge(line)
test()