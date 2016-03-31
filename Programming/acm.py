import sys
def main():
    log1 = []
    correct = 0
    score = 0
    #for i in sys.stdin:
    logfile = open('C:/Users/HGoscenski/Downloads/samples (2)/2.in', 'r')
    for i in logfile:
        log1.append(i)
    for i in log1:
        temp = []
        temp.append(i.split(' '))
        print(temp)
        if temp[0][2] == 'right':
            score += temp[0][0]
            correct += 1
    print(correct, score)
main()
