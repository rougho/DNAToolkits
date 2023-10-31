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
