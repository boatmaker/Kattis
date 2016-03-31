import sys
def main():
    ahs = sys.stdin
    ahs = ahs.split('\n')
    jon = len(ahs[0])
    dr = len(ahs[1])
    if jon >= dr:
        print("go")
    else:
        print('no')
main()
