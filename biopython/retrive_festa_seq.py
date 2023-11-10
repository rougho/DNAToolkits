import Bio
from Bio import SeqIO
from Bio import Entrez
from biopython import ncbi_api


databases = Entrez.einfo()
Entrez.email = 'rohi@rgho.de'
# print(Entrez.read(databases))


db = Entrez.einfo(db='nuccore')
descr = Entrez.read(db)
# print(descr["DbInfo"].keys())
# print(descr["DbInfo"]["Count"])
idlist = ncbi_api.extract_ids('Homo sapiens ins')
# print(descr["DbInfo"]["LastUpdate"])
handle = Entrez.esearch(
    db='nucleotide', term='Homo sapiens insulin (INS), transcript variant 1, mRNA', retmax='100')
handle2 = Entrez.efetch(db="nucleotide", id=idlist,
                        rettype='gb', retmode='text')

data = {}

for seq_record in SeqIO.parse(handle2, "gb"):
    try:
        ncbiReference = seq_record.id
        source = seq_record.annotations["source"]
        length = len(seq_record)
        sequence = str(seq_record.seq)

        data[ncbiReference] = {
            "reference": ncbiReference,
            "source": source,
            "length": length,
            "sequence": sequence
        }
    except KeyError:
        print(f"Source annotation not found for record {ncbiReference}!")
    except Bio.Seq.UndefinedSequenceError:
        print(f"Sequence not found for record {ncbiReference}!")


def find_record(recordID):
    if recordID in data:
        record = data[recordID]
        # print(f"Record found: {record}")
    else:
        # print(f"Record with ID {recordID} not found.")
        pass

    return record
