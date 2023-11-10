# Main Toolkits
from biopython import retrive_festa_seq as ncbi
from dna_toolkits import DNAToolkit as toolkit
import utilities as utl
from biopython import ncbi_api

file = "/home/rohi/Home/B/bioinformatics/data/computing_gc_contanct_test_data.txt"
dna_sequence = toolkit.seq_validation(toolkit.seq_generator(50))
counted_sequence_dict = toolkit.count_nucleotide_frequency(dna_sequence)

# print(f"\n\n\n\n- Sequence: {utl.colored(dna_sequence)}")
# print(f"- Sequence Lenght: {len(dna_sequence)}")
# print(
#     f"- Sequence Frequency: {toolkit.count_nucleotide_frequency(dna_sequence)}\n")
# print(
#     f"- DNA -> RNA Transcription: {utl.colored(toolkit.transcription(dna_sequence))}\n")
# print(
#     f"- DNA Compelement reversed: 5' {utl.colored(toolkit.reverse_complement_sequence(dna_sequence))} 3'\n")
# print(f"- DNA Helix:")
# print(f"\t\t5' {utl.colored(dna_sequence)} 3'")
# print(f"\t\t   {''.join(['|' for i in range(len(dna_sequence))])}")
# print(f"\t\t3' {utl.colored(toolkit.complement_sequence(dna_sequence))} 5'\n")
# print(f"- GC-Content: {toolkit.gc_content(dna_sequence)}%\n")
# print(
#     f"- Sub Sequence: \n\t\t\t{utl.print_subseq_gc_content(toolkit.subsequence_gc_content(dna_sequence, 5))}\n\n\n")
# gc_content_max = toolkit.compute_max_gc_content(file)
# print(
#     f"- Maximum GC-Content:\n\t\t\tLabel: {gc_content_max['label']}'\n\t\t\tPercentage: {gc_content_max['gc_content']}\n\t\t\tSequence: ")
# sequence_chunks = [gc_content_max['sequence'][i:i+50]
#                    for i in range(0, len(gc_content_max['sequence']), 50)]
# for chunk in sequence_chunks:
#     print(f"\t\t\t\t\t{chunk}")

# print(
#     f"\n- {utl.light_blue('Aminoacids Sequence')}: {toolkit.sequence_translator(toolkit.compute_max_gc_content(file)['sequence'],0)}\n")
# print(
#     f"- {utl.light_blue('Codon Frequency (L)')}: {toolkit.codon_frequency(toolkit.compute_max_gc_content(file)['sequence'],'L')}\n")
# print(f"- {utl.light_blue('Reading Frames')}:")
# for frame in toolkit.open_reading_frames(toolkit.compute_max_gc_content(file)['sequence']):
#     print(frame)

# test_rf = ['I', 'R', 'Y', 'L', 'D', 'R', 'A', 'S', 'L', 'P', 'R', 'P', 'R', 'H', 'R', 'R', 'N', 'E', 'K', 'G', 'W', 'T', 'S', 'R', 'L', 'T', 'E', 'L', 'T', 'R', 'H', 'T', 'L', 'N', 'A', 'G', 'R', 'G', 'A', 'P', 'I', 'S', 'L', 'N', 'P', 'L', 'M', 'E', 'V', 'V', 'S', 'D', 'M', 'V', 'Q', '_', 'C', 'V', 'G', 'V', 'S', 'P', 'Y', 'Y', 'P', 'T', 'M', 'L', 'D', 'I', 'W', 'S', 'V', 'P', 'E', 'C', 'V', 'R', 'A', 'C', 'W', 'I', 'P', 'G', 'A', 'K', 'S', 'R', 'S', 'E', 'M', 'T', 'P', 'C', 'R', 'V', 'I', 'A', 'W', 'S', 'L', 'G', 'A', 'H', 'T', 'V', 'Y', 'Q', 'S', 'D', 'L', 'K', 'D', 'L', '_', 'C', 'S', 'N', 'R', 'F', 'E', 'L', 'A', 'G', 'W', 'R', 'G', 'G', 'K', 'I', 'R', 'L', 'D', 'A', 'P', 'V', 'H',
#            'S', 'V', 'L', 'Q', 'C', '_', 'R', 'I', 'Q', 'L', 'T', 'H', 'A', 'V', 'L', 'S', 'P', 'R', 'V', 'R', 'R', 'L', 'R', 'R', 'G', 'R', 'K', 'Q', 'D', 'A', 'A', 'C', 'L', 'S', 'P', 'L', 'L', 'Q', 'F', 'D', 'V', 'P', 'R', 'R', 'R', 'S', 'Q', 'I', 'V', 'E', '_', 'T', '_', 'I', 'S', '_', 'I', 'G', 'G', 'G', 'P', 'E', 'P', 'H', 'L', 'T', 'G', 'T', 'R', 'V', 'R', 'L', 'S', 'P', 'P', 'P', 'S', 'P', 'Q', 'A', 'S', 'I', 'P', 'S', 'R', 'T', 'P', 'T', 'G', 'E', 'C', 'E', 'T', 'T', 'E', 'L', 'G', 'T', 'R', 'S', 'V', 'P', 'Q', 'C', 'G', 'Q', 'M', 'T', 'F', 'L', 'G', 'L', 'I', 'K', 'V', 'L', 'R', 'W', 'C', 'V', 'R', 'D', 'C', 'A', 'K', 'G', 'G', 'I', 'A', 'N', 'Y', 'W', 'R', 'R', 'H', 'W', 'N', 'R']

# print(toolkit.proteins_from_reading_frame(test_rf))

# ids = ncbi_api.extract_ids('Homo sapiens insulin')
# print(ids)

# print(api.api_call('Homo sapiens insulin', 'nuccore'))
# print(ncbi_api.extract_fasta('Homo sapiens ins', 'nuccore'))


# record = ncbi.find_record('NM_000207.3')
# ncbiSequence = record['sequence']

# print(ncbiSequence)
for protein in toolkit.all_proteins_from_reading_frames('AGCCCTCCAGGACAGGCTGCATCAGAAGAGGCCATCAAGCAGATCACTGTCCTTCTGCCATGGCCCTGTGGATGCGCCTCCTGCCCCTGCTGGCGCTGCTGGCCCTCTGGGGACCTGACCCAGCCGCAGCCTTTGTGAACCAACACCTGTGCGGCTCACACCTGGTGGAAGCTCTCTACCTAGTGTGCGGGGAACGAGGCTTCTTCTACACACCCAAGACCCGCCGGGAGGCAGAGGACCTGCAGGTGGGGCAGGTGGAGCTGGGCGGGGGCCCTGGTGCAGGCAGCCTGCAGCCCTTGGCCCTGGAGGGGTCCCTGCAGAAGCGTGGCATTGTGGAACAATGCTGTACCAGCATCTGCTCCCTCTACCAGCTGGAGAACTACTGCAACTAGACGCAGCCCGCAGGCAGCCCCACACCCGCCGCCTCCTGCACCGAGAGAGATGGAATAAAGCCCTTGAACCAGC', 0, 0, True):
    print(f'{protein}')


# print(toolkit.all_proteins_from_reading_frames(ncbiSequence, 0, 0, True))

# print(type(ncbiSequence))
