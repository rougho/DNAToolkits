from dna_toolkits import DNAToolkit
import collections

def count_nucleotide_frequency(sequance):
    try:
        # temp_seq_dict = { "A" : 0, "C" : 0, "G" : 0, "T" : 0,}
        # for nucleotide in sequance:
        #     temp_seq_dict[nucleotide] += 1
        # return temp_seq_dict
        return dict(collections.Counter(sequance))
    except:
        if DNAToolkit.seq_validation(sequance) is False:
           return "Wrong Sequance"