people={}
def School(name):
    if people.get(name):
        print(name, people.get(name))
    else:
        print("haha")
def test():
    num = int(input())
    #print(num)
    for i in range(0,num):
        line = input()
        tokens=line.strip().split()
       # print(tokens)
        people[tokens[0]+"-1"]= int(tokens[1])
        people[tokens[0]+"-2"]= int(tokens[2])
        people[tokens[0]+"-3"]= int(tokens[3])
        people[tokens[0]+"-4"]= int(tokens[4])
        # for j in range(1, 5):  people[tokens[0]+"-"+str(j)]= int(tokens[j])
    #print(people)
    num= int(input())
    for i in range(0, num) :
        line = input()
        #print(line)
        print(line, people[line])
        print("people-1",people.get("people-1"))
  
    
test()