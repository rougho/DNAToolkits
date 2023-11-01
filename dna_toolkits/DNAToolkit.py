import random
from dna_toolkits.structures import *
import collections
import utilities as utl

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

def subsequence_gc_content(sequence, section=20):
    result = {}
    for i in range(0, len(sequence) - section + 1, section):
        sub_sequence = sequence[i:i+section]
        subseq_gc_content = gc_content(sub_sequence)
        result[sub_sequence] = {
            'position': i,
            'gc_content': subseq_gc_content
        }
    return result

def compute_max_gc_content(file_path):
    max_gc_dict = {}
    FASTA_dict = utl.FASTA_to_dict(file_path)
    calculate_values_gcc = {key: gc_content(value) for (key, value) in FASTA_dict.items()}
    max_gc = max(calculate_values_gcc, key=calculate_values_gcc.get)
    max_gc_full = {
        'Label' : max_gc[1:],
        'GC-Content' : calculate_values_gcc[max_gc],
        'Sequence ' : FASTA_dict[max_gc]
        }
    return max_gc_full

