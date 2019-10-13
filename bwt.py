#! /usr/bin/env python

def bwt(s):  
    s = s + "$"     
    matrix = (s[i:] + s[:i] for i in range(len(s)))
    matrix_final = sorted(matrix)
    transform_column = [row[-1:] for row in matrix_final]  
    print("".join(transform_column))                 



if __name__ == "__main__":
    bwt('AATTGCGCGG')