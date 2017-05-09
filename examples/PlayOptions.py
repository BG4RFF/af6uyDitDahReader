import getopt
import itertools
import sys


class PlayOptions:
    def printUsage(self):
        print(self.desc)
        print('Usage: ' + self.progName)
        print('  -h --help                          : help')
        print('  -i <file> --infile=<input file>    : input file ('
              + self.wfile + ')')
        print('  -w <N> --wpm=<words per minute>    : words per minute ('
              + str(self.wpm) + ')')
        print('  -f <N> --farnsworth=<N>            : Farnsworth in wpm ('
              + str(self.farns) + ')')
        print('  -n <N> --nwords=<N>                : words to play ('
              + str(self.n) + ')')
        print('  -r <N> --repeat=<N>                : repeat each word ('
              + str(self.repeatN) + ')')
        print('  -H <float> --Hz=<float>            : tone in Hz ('
              + str(self.hz) + ')')

    def __init__(self, desc):
        self.desc = desc
        self.progName = sys.argv[0]
        self.wfile = "data/2-grams-1-to-50.txt"
        self.n = 20
        self.wpm = 30.0
        self.farns = 30.0
        self.repeatN = 1
        self.hz = 600.
        try:
            opts, args = getopt.getopt(sys.argv[1:], "hi:w:f:n:r:H:",
                                       ["help",
                                        "infile=",
                                        "wpm=",
                                        "farnsworth=",
                                        "nwords=",
                                        "repeat=",
                                        "Hz="])
        except:
            self.printUsage()
            sys.exit()
        for opt, arg in opts:
            if opt in ("-h", "--help"):
                self.printUsage()
                sys.exit()
            elif opt in ("-i", "--ifile"):
                self.wfile = arg
            elif opt in ("-w", "--wpm"):
                self.wpm = float(arg)
            elif opt in ("-f", "--farnsworth"):
                self.farns = float(arg)
            elif opt in ("-n", "--nwords"):
                self.n = int(arg)
            elif opt in ("-r", "--repeat"):
                self.repeatN = int(arg)
            elif opt in ("-H", "--Hz"):
                self.hz = float(arg)
