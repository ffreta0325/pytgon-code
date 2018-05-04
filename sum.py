import sys
def summ():
 for line in sys.stdin:
    line = line.strip()
    print(line)
    tokens = line.split()
    print(tokens)
    print(len(tokens))
    
    total = sum([float(tokens) for tokens in tokens])
    total = 0
    for i in range(0, len(tokens)):
         total+= float(tokens[i])
    print(total)
summ()