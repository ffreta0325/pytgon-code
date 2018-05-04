import sys
def readlines():
    for line in sys.stdin:
        line = line.strip()
        num=int(line)
        print(num+1)
readlines()