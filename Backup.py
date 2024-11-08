import os
import sys

def main():
    inFile = sys.argv[1]
    outFile = "." + inFile + ".bak"
    os.system("cp " + inFile + " " + outFile)


main()

