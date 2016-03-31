import sys
import math
def main():
    oddlyeven = []
    for i in sys.stdin:
        oddlyeven.append(int(i))
    del oddlyeven[0]
    for i in oddlyeven:
        if i % 2 == 0:
            print(i, 'is even')
        else:
            print(i, 'is odd')
main()
