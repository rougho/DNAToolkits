import dna_toolkits.DNAToolkit as toolkit

def colored(seq):
    bcolors = {
        'A': '\033[92m',
        'C': '\033[94m',
        'G': '\033[93m',
        'T': '\033[91m',
        'U': '\033[91m',
        'reset': '\033[0;0m'
    }

    tmpStr = ""

    for nuc in seq:
        if nuc in bcolors:
            tmpStr += bcolors[nuc] + nuc
        else:
            tmpStr += bcolors['reset'] + nuc

    return tmpStr + '\033[0;0m'

def print_subseq_gc_content(subseq_gc_content_dict):
    formatted_str = ""
    for subseq, info in subseq_gc_content_dict.items():
        formatted_str += f"\t\t\tSubsequence: {subseq} | Position: {info['position']:<2} | GC Content: {info['gc_content']:.2f}%\n"
    return formatted_str.strip()

def read_file(path):
    '''Reading a file and return lines as a list'''
    with open(path, "r") as file:
        return [l.strip() for l in file.readlines()]

def FASTA_validator(FASTA_dict):
    '''Validate the sequence in a dict'''
    try:
        for key, value in FASTA_dict.items():
            if not toolkit.seq_validation(value):
                print(f"Invalid DNA sequence found:\nLabel: {key}\nSequence: {value}")
                return False
        return True
    except Exception as e:
        print("An error occurred during FASTA validation:", e)
        return False

def FASTA_to_dict(path):
    '''Read FASTA formatted file and validate the sequence and return a dictionary'''
    FASTA_file = read_file(path)
    FASTA_dict = {}
    FASTA_label = ""

    for line in FASTA_file:
        line = line.strip()
        if line.startswith('>'):
            FASTA_label = line
            FASTA_dict[FASTA_label] = ""
        else:
            FASTA_dict[FASTA_label] += line.replace(" ","")

    if FASTA_validator(FASTA_dict):
        return FASTA_dict
    else:
        return None