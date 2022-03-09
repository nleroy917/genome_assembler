#!/usr/bin/env python

"""
    usage:
        shortest_common_superstring.py [options] sequences.txt
    where the options are:
        -h,--help : print usage and quit

    sequences.txt is a file with one sequence to be included in each row.
"""

from sys import argv, stderr
from getopt import getopt, GetoptError
import itertools

def read_sequences(filename):
    '''Read the sequences (one per line) from the filename and return a list
    '''
    sequences = []
    with open(filename, 'r') as f:
        for line in f:
            sequences.append(line.strip())
    return sequences

def calculate_scs(reads):
    """
    Implement the greedy shortest-common-superstring strategy discussed in 
    class. From the reads, find two string with the maximal overlap and merge 
    them. Keep doing this until you have only 1 string left
    """
    scs = ""

    return scs

def main(filename):
    # read the sequences from the file
    sequences = read_sequences(filename)
    print("Read the sequences", file=stderr)

    # calculate the shortest common superstring
    superstring = calculate_scs(sequences)

    # print the result
    print(superstring)

if __name__ == "__main__":
    try:
        opts, args = getopt(argv[1:], "h", ["help"])
    except GetoptError as err:
        print(err)
        print(__doc__, file=stderr)
        exit(1) 

    for o, a in opts:
        if o in ("-h", "--help"):
            print(__doc__, file=stderr)
            exit()
        else:
            assert False, "unhandled option"

    if len(args) != 1:
        print(__doc__, file=stderr)
        exit(2)

    main(args[0])
