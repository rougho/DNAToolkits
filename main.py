# Main Toolkits

from dna_toolkits import DNAToolkit as toolkit
from Rosalind_problems import necleotides_counter as nc

my_seq = toolkit.seq_generator(50)
nc.count_nucleotides(my_seq)