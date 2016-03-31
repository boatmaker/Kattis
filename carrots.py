import sys
def main():
    log = []
    total1 = []
    for i in sys.stdin:
        log.append(i)
    total1 = log[0].split(' ')
    total = total1[1]
    print(total)
main()
