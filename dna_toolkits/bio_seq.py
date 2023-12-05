from .bio_struct import *
from random import choice
from utilities import light_blue as lb


class BioSeq:
    """Dfault value: ACTG, DNA,No label"""

    def __init__(self, sequence="ATCG", sequence_type="DNA", label="No Label"):
        """Initialization"""
        self.sequence = sequence.upper()
        self.label = label
        self.sequence_type = sequence_type
        self.is_valid = self.__seq_validation()
        assert self.is_valid, "Sequence is not valid!"

    def __seq_validation(self):
        '''Helper Function, Validate a sequence of DNA'''
        return set(dna_nucleotides).issuperset(self.sequence)

    def seq_biotype(self):
        """Returns sequence bio type"""
        return self.sequence_type

    def seq_info(self):
        """Returns 4 strings on information about the sequence"""
        return f"{lb('Label')}: {self.label}\n{lb('Sequence')}: {self.sequence}\n{lb('Type')}: {self.sequence_type}\n{lb('Length')}: {len(self.sequence)}"

    def seq_generator(self, length=20, sequence_type="DNA"):
        """Generate (DNA as default) sequence randomly by given default length of 20"""
        temp_seq = ''.join([choice(dna_nucleotides)
                            for nucleotide
                            in range(length)])
        self.__init__(temp_seq, sequence_type, "Randomly generated sequence")
