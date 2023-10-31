# Main Toolkits

from dna_toolkits import DNAToolkit as toolkit
import utilities as utl

dna_sequence = toolkit.seq_validation(toolkit.seq_generator(50)) 
counted_sequence_dict = toolkit.count_nucleotide_frequency(dna_sequence)

# print(f"\n\n\n\n- Sequence: {utl.colored(dna_sequence)}")
# print(f"- Sequence Lenght: {len(dna_sequence)}")
# print(f"- Sequence Frequency: {toolkit.count_nucleotide_frequency(dna_sequence)}\n")
# print(f"- DNA -> RNA Transcription: {utl.colored(toolkit.transcription(dna_sequence))}\n")
# print(f"- DNA Compelement reversed: 5' {utl.colored(toolkit.reverse_complement_sequence(dna_sequence))} 3'\n")
# print(f"- DNA Helix:")
# print(f"\t\t5' {utl.colored(dna_sequence)} 3'")
# print(f"\t\t   {''.join(['|' for i in range(len(dna_sequence))])}")
# print(f"\t\t3' {utl.colored(toolkit.complement_sequence(dna_sequence))} 5'\n")
# print(f"- GC-Content: {toolkit.gc_content(dna_sequence)}%\n")
# print(f"- Sub Sequence: \n\t\t\t{utl.print_subseq_gc_content(toolkit.subsequence_gc_content(dna_sequence, 5))}\n\n\n")

print(toolkit.compute_max_gc_content("/home/rohi/Home/B/bioinformatics/data/computing_gc_contanct_test_data.txt"))
