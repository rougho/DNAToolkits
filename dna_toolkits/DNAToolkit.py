import random

nucleotides = ["A", "C", "G", "T"]


def seq_generator(len):
    return ''.join([random.choice(nucleotides)
                    for nucleotide
                    in range(len)])


#check the sequence that its a DNA string
def seq_validation(dna_sequance):
    temp_nucleotide = dna_sequance.upper()
    for nucleotide in temp_nucleotide:
        if nucleotide not in nucleotides:
            return False
    return temp_nucleotide

