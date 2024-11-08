import os
import sys

def main():
    target = sys.argv[1]
    backup = "." + target + ".bak"
    os.remove(backup)
main()
