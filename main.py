# Main Toolkits

from dna_toolkits import DNAToolkit as toolkit
from Rosalind_problems import necleotides_counter as nc
import utilities as ult

dna_sequence = toolkit.seq_validation(toolkit.seq_generator(50)) 
counted_sequence_dict = nc.count_nucleotide_frequency(dna_sequence)

print(f"\n- Sequence: {ult.colored(dna_sequence)}")
print(f"- Sequence Lenght: {len(dna_sequence)}")
print(f"- Sequence Frequency: {nc.count_nucleotide_frequency(dna_sequence)}")
print(f"- DNA -> RNA Transcription: {ult.colored(toolkit.transcription(dna_sequence))}\n")
print(f"- DNA Helix:")
print(f"\t\t5' {ult.colored(dna_sequence)} 3'")
print(f"\t\t   {''.join(['|' for i in range(len(dna_sequence))])}")
print(f"\t\t3' {ult.colored(toolkit.reverse_sequence(dna_sequence))} 5'")