import os
import sys

def main():
    Target = sys.argv[1]
    backup = "." + Target + ".bak"
    os.system("rm " + Target)
    os.system("cp " + backup + " " + Target)
    os.system("rm " + backup)
main()

