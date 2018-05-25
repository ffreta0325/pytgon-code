import sys
birth={}
def test():
    for line in sys.stdin:
        line = line.strip()
        #print(line)
        tokens = line.split()
        #print(tokens)
        m = int(tokens[1])
        if birth.get(m):
            birth[m] += 1
        else:
            birth[m] = 1
    #print(birth)
    for i in range (1, 13):
        print(i, birth.get(i))

test()