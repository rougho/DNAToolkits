import random
from dna_toolkits.structures import *
import collections

# generate sequance
def seq_generator(len):
    return ''.join([random.choice(nucleotides)
                    for nucleotide
                    in range(len)])

def count_nucleotide_frequency(sequence):
    try:
        return dict(collections.Counter(sequence))
    except:
        if seq_validation(sequence) is False:
           return "Wrong Sequance"
        
def print_nucleotides_frequency(sequence_dict):
    for key in sequence_dict:
        print(f"{key} : {sequence_dict[key]}")

#check the sequence that its a DNA string
def seq_validation(dna_sequance):
    '''Validate a sequence of DNA'''
    temp_nucleotide = dna_sequance.upper()
    for nucleotide in temp_nucleotide:
        if nucleotide not in nucleotides:
            return False
    return temp_nucleotide

#DNA Transcription
def transcription(sequence):
    '''Transcripting a sequence of DNA to RNA'''
    return sequence.replace("T", "U")

# DNA Raplication
def reverse_complement_sequence(sequence):
    '''Reverse the complemented sequence'''
    return complement_sequence(sequence)[::-1]

def complement_sequence(sequence):
    '''Complement a sequence of DNA'''
    mapping = str.maketrans('ATCG', 'TAGC')
    return sequence.translate(mapping)

def gc_content(sequence):
    '''percentage of nitrogenous bases in a DNA/RNA molecule that are either Guanine or Cytosine'''
    return (sequence.count('C') + sequence.count('G')) / len(sequence) * 100