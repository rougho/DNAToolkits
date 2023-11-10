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

# check the sequence that its a DNA string


def seq_validation(dna_sequance):
    '''Validate a sequence of DNA'''
    temp_nucleotide = dna_sequance.upper()
    for nucleotide in temp_nucleotide:
        if nucleotide not in nucleotides:
            return False
    return temp_nucleotide

# DNA Transcription


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
            'position': i+1,
            'gc_content': subseq_gc_content
        }
    return result


def compute_max_gc_content(file_path):
    max_gc_dict = {}
    FASTA_dict = utl.FASTA_to_dict(file_path)
    calculate_values_gcc = {key: gc_content(
        value) for (key, value) in FASTA_dict.items()}
    max_gc = max(calculate_values_gcc, key=calculate_values_gcc.get)
    max_gc_full = {
        'label': max_gc[1:],
        'gc_content': calculate_values_gcc[max_gc],
        'sequence': FASTA_dict[max_gc]
    }
    return max_gc_full


def sequence_translator(sequence, initialize_position=0):
    return [DNA_Codons[sequence[position:position + 3]]
            for position in range(initialize_position,
                                  len(sequence) - 2, 3)]


def codon_frequency(sequence, aminoacid):
    temp_list = []
    for i in range(0, len(sequence) - 2, 3):
        if DNA_Codons[sequence[i:i + 3]] == aminoacid:
            temp_list.append(sequence[i:i + 3])
    frequency_dictionary = dict(collections.Counter(temp_list))
    total_wight = sum(frequency_dictionary.values())
    for seq in frequency_dictionary:
        frequency_dictionary[seq] = round(frequency_dictionary[seq]
                                          / total_wight, 2)
    return frequency_dictionary


def open_reading_frames(sequence):
    '''Generate the six reading frames of a DNA sequence'''
    frames = []
    frames.append(sequence_translator(sequence, 0))
    frames.append(sequence_translator(sequence, 1))
    frames.append(sequence_translator(sequence, 2))
    frames.append(sequence_translator(
        reverse_complement_sequence(sequence), 0))
    frames.append(sequence_translator(
        reverse_complement_sequence(sequence), 1))
    frames.append(sequence_translator(
        reverse_complement_sequence(sequence), 2))
    return frames


def proteins_from_reading_frame(aminoacid_sequnce):
    '''Compute all possibale proteins in an aminoacid sequence and return list of possible proteins'''
    current_protein = []
    proteins = []
    for aminoacid in aminoacid_sequnce:
        # stop if stop_sign was found (_)
        if aminoacid == "_":
            if current_protein:
                for p in current_protein:
                    proteins.append(p)
                current_protein.clear()
        else:
            # start if M found
            if aminoacid == "M":
                current_protein.append("")
            for i in range(len(current_protein)):
                current_protein[i] += aminoacid
    return proteins


def all_proteins_from_reading_frames(sequence, startReadingPosition=0, endReadingPosition=0, ordered=False):
    '''Compute all possibe proteins from all open reading frames'''
    if endReadingPosition > startReadingPosition:
        readingFrames = open_reading_frames(
            sequence[startReadingPosition: endReadingPosition])
    else:
        readingFrames = open_reading_frames(sequence)

    result = []
    for rf in readingFrames:
        proteins = proteins_from_reading_frame(readingFrames)
        for p in proteins:
            result.append(p)

    if ordered:
        return sorted(result, key=len, reverse=True)
    return result
