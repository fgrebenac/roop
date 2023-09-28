#!/usr/bin/env python3

from roop import core
import sys

def main():
    # core.run()
    input = sys.stdin
    output = sys.stdout.buffer
    while True:
        command = input.readline().strip()
        if command != "":
            core.run(command)
            output.flush()
        else:
            output.write("didn't get start\n")
            output.flush()

if __name__ == '__main__':
    main()
    
