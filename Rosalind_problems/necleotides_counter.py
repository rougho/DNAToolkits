from dna_toolkits import DNAToolkit
import collections

def count_nucleotide_frequency(sequence):
    try:
        return dict(collections.Counter(sequence))
    except:
        if DNAToolkit.seq_validation(sequence) is False:
           return "Wrong Sequance"
        
def print_nucleotides_frequency(sequence_dict):
    for key in sequence_dict:
        print(f"{key} : {sequence_dict[key]}")