def count(seq):
    '''Count frequency of the nucleotides and return a dictionary, DNA sequence as attribute(String)'''
    tmp = {'A':0, 'C':0, 'G':0, 'T':0}
    for nuc in seq:
        tmp[nuc] += 1
    return tmp

seq = "Replace Your Sequence Here!"
result = count(seq)
print(' '.join([str(val) for key, val in result.items()]))