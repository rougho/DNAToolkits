from .bio_struct import *
from utilities import light_blue as lb


class BioSeq:
    """Dfault value: ACTG, DNA,No label"""

    def __init__(self, sequence="ATCG", sequence_type="DNA", label="No Label"):
        self.sequence = sequence.upper()
        self.label = label
        self.sequence_type = sequence_type
        self.is_valid = self.seq_validation()
        assert self.is_valid, "Sequence is not valid!"

    def seq_info(self):
        return f"{lb('Label')}: {self.label}\n{lb('Sequence')}: {self.sequence}\n{lb('Type')}: {self.sequence_type}\n{lb('Length')}: {len(self.sequence)}"

    def seq_validation(self):
        '''Validate a sequence of DNA'''
        return set(dna_nucleotides).issuperset(self.sequence)
