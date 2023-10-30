import random
from .structures import *

# generate sequance
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

#DNA Transcription
def transcription(sequence):
    return sequence.replace("T", "U")

# DNA Raplication
def reverse_sequence(sequence):
    return ''.join([dna_reverse_complement[nuc] for nuc in sequence])

