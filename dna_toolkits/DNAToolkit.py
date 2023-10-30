import random, collections

nucleotides = ["A", "C", "G", "T"]


def seq_generator(len):
    return ''.join([random.choice(nucleotides)
                    for nucleotide
                    in range(len)])


#check the sequence that its a DNA string
def seq_validation(dna_sequance):
    temp_nucleotide = dna_sequance.upper()
    for nucleotide in temp_nucleotide:
        if nucleotide not in nucleotides:
            return False
    return temp_nucleotide

def count_nucleotide_frequency(sequance):
    try:
        # temp_seq_dict = { "A" : 0, "C" : 0, "G" : 0, "T" : 0,}
        # for nucleotide in sequance:
        #     temp_seq_dict[nucleotide] += 1
        # return temp_seq_dict
        return dict(collections.Counter(sequance))
    except:
        if seq_validation(sequance) is False:
           return "Wrong Sequance"