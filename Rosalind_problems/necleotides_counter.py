from dna_toolkits import DNAToolkit
import collections

def count_nucleotide_frequency(sequance):
    try:
        return dict(collections.Counter(sequance))
    except:
        if DNAToolkit.seq_validation(sequance) is False:
           return "Wrong Sequance"
        
def count_nucleotides(sequance):
    counter = count_nucleotide_frequency(sequance)
    for key in counter:
        print(f"{key} : {counter[key]}")