import sys
def main():
    log1 = []
    correct = 0
    score = 0
    for i in sys.stdin:
        log1.append(i)
    total = len(log1)
    # print(log1)
    for i in log1[0:total-1]:
        temp = []
        temp.append(i.split(' '))
        if temp[0][2] == 'right\n':
            score += int(temp[0][0])
            correct += 1
            for x in log1:
                if (temp[0][1] + ' ' + 'wrong') in x:
                    score += 20
    print(correct, score)
main()
