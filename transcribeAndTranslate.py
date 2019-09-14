#!/usr/bin/env python

from Bio.Seq import Seq
from Bio.Alphabet import generic_dna

def main():
    my_dna1 = Seq("ATGATTGGCCCGGTTTTTTAA", generic_dna)
    my_dna2 = Seq("GTGGTGGGGAAATTCCGCTGA", generic_dna)

    print("Original sequence1: ", my_dna1)
    print("Original sequence2: ", my_dna2)

    print("Transcribed Sequence1: ", my_dna1.transcribe())
    print("Transcribed Sequence2: ", my_dna2.transcribe())

    print("Translated Sequence1: ", my_dna1.translate())
    print("Translated Sequence2: ", my_dna2.translate())

if __name__ == '__main__':
    main()