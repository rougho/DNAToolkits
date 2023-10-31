# Main Toolkits

from dna_toolkits import DNAToolkit as toolkit
import utilities as ult

dna_sequence = toolkit.seq_validation(toolkit.seq_generator(50)) 
counted_sequence_dict = toolkit.count_nucleotide_frequency(dna_sequence)

print(f"\n\n\n\n- Sequence: {ult.colored(dna_sequence)}")
print(f"- Sequence Lenght: {len(dna_sequence)}")
print(f"- Sequence Frequency: {toolkit.count_nucleotide_frequency(dna_sequence)}\n")
print(f"- DNA -> RNA Transcription: {ult.colored(toolkit.transcription(dna_sequence))}\n")
print(f"- DNA Compelement reversed: 5' {ult.colored(toolkit.reverse_complement_sequence(dna_sequence))} 3'\n")
print(f"- DNA Helix:")
print(f"\t\t5' {ult.colored(dna_sequence)} 3'")
print(f"\t\t   {''.join(['|' for i in range(len(dna_sequence))])}")
print(f"\t\t3' {ult.colored(toolkit.complement_sequence(dna_sequence))} 5'\n")
print(f"- GC-Content: {toolkit.gc_content(dna_sequence)}%\n\n\n")
