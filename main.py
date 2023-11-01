# Main Toolkits

from dna_toolkits import DNAToolkit as toolkit
import utilities as utl
file = "/home/rohi/Home/B/bioinformatics/data/computing_gc_contanct_test_data.txt"
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
# gc_content_max = toolkit.compute_max_gc_content(file)
# print(f"- Maximum GC-Content:\n\t\t\tLabel: {gc_content_max['label']}'\n\t\t\tPercentage: {gc_content_max['gc_content']}\n\t\t\tSequence: ")
# sequence_chunks = [gc_content_max['sequence'][i:i+50] for i in range(0, len(gc_content_max['sequence']), 50)]
# for chunk in sequence_chunks:
#     print(f"\t\t\t\t\t{chunk}")

print(f"- Aminoacids Sequence: {toolkit.sequence_translator(dna_sequence,0)}")
print(toolkit.codon_frequency(toolkit.compute_max_gc_content(file)['sequence'],"V"))