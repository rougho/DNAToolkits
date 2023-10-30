# Main Toolkits

from dna_toolkits import DNAToolkit as toolkit
from Rosalind_problems import necleotides_counter as nc

my_seq = toolkit.seq_generator(50)
counter = nc.count_nucleotide_frequency(my_seq)
for key in counter:
    print(f"{key} : {counter[key]}")