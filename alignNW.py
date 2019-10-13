#! /usr/bin/env python


import numpy as np

map ={'match': 1, 'mismatch': -1, 'gap': -2}

def check_match(arg1, arg2):    
    if arg1 == '-' or arg2 == '-':
        return map['gap']
    elif arg1 == arg2:
        return map['match']
    else:
        return map['mismatch']

def needleman_wunsch(s1, s2):
    m, n = len(s1), len(s2)
    score = np.zeros((m+1, n+1))
    
    #Initializing the score matrix with gap penalties   
    for j in range(n+1):
        score[0][j] = map['gap'] * j
        
    for i in range(m+1):
        score[i][0] = map['gap'] * i
    
    
    #Filling the values
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            horizontal_gap = score[i][j-1] + map['gap']           
            vertical_gap = score[i-1][j] + map['gap']
            diagonal = score[i-1][j-1] + check_match(s1[i-1], s2[j-1])
            
            score[i][j] = max(diagonal, vertical_gap, horizontal_gap)

    i,j = m,n
    seq1, seq2 = '', ''
    
    
    #Traceback
    while i > 0 and j > 0:
        score_current = score[i][j]
        score_diagonal = score[i-1][j-1]
        score_left = score[i][j-1]
        score_up = score[i-1][j]
        if score_current == score_diagonal + check_match(s1[i-1], s2[j-1]):
           k1,k2 = s1[i-1],s2[j-1]
           i,j = i-1,j-1
        elif score_current == score_up + map['gap']:           
           k1,k2 = s1[i-1],'-'
           i -= 1
        elif score_current == score_left + map['gap']:
           k1,k2 = '-',s2[j-1]
           j -= 1
        
        seq1 +=k1
        seq2 += k2
            

    while i > 0:
       k1,k2 = s1[i-1],'-'     
       seq1 +=k1
       seq2 += k2
       i -= 1
        
    while j > 0:
       k1,k2 = '-',s2[j-1]       
       seq1 +=k1
       seq2 += k2
       j -= 1
    
    seq1 = seq1[::-1]
    seq2 = seq2[::-1]
    seqN = len(seq1)
    sym = ''
    seq_score = 0
    ident = 0
    for i in range(seqN):
       k1 = seq1[i]
       k2 = seq2[i]
       if k1 == k2:
           sym +=k1
           ident += 1
           seq_score += check_match(k1, k2)    
       else: 
           seq_score += check_match(k1, k2)
           sym += ' '
        
    ident = ident/seqN * 100
    
    print('Score = %d\n'% seq_score)
  
    print(seq1)
    aligning_sequences(seq1, seq2)
    print(seq2)
    
    
def aligning_sequences(str1, str2):
    str = ''
    for i in range(len(str1)):
        if str1[i] == str2[i]:
            str += '|'
        else:
            str += ' '
    print(str)        
    
   
   

if __name__ == '__main__':
    needleman_wunsch("TATCGCGCTTT","ATTACCGCCGTT")


    
