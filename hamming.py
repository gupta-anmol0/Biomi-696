
#! /usr/bin/env python

def hamming(str1, str2):    
    if len(str1) != len(str2):
        print("Strings length do no match")
    hamming_count = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            hamming_count += 1
    print("The hamming distance is", hamming_count)


if __name__ == '__main__':
    hamming('TTATCGCGCTTTCTTCCAA', 'ATACCGCGCGTTCGACCAA')        