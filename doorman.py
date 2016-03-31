import sys
def main():
    log = []
    # for line in sys.stdin:
    logfile = open('/Users/hgoscenski/Desktop/doorman.2.in', 'r')
    for line in logfile:
        log.append(line)
    men = 0
    women = 0
    maxdiff = int(log[0])
    
main()
