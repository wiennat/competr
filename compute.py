import sys
import pprint

pp = pprint.PrettyPrinter(indent=4)
rl = lambda: sys.stdin.readline().strip()

def compute():
    """ Code implementation """
    pass

if __name__ == '__main__':
    for i in range(int(rl())):  # The first line is usually # of cases
        print "Case #%d: %s" % (i+1, compute())