# ex: http://rosalind.info/problems/revc/

def complement_a_strand_of_dna(dna: str):
    rev_seq = list(dna[::-1])
    for i in range(0, len(rev_seq)):
        if rev_seq[i] == "C":
            rev_seq[i] = "G"
        elif rev_seq[i] == "G":
            rev_seq[i] = "C"
        elif rev_seq[i] == "A":
            rev_seq[i] = "T"
        elif rev_seq[i] == "T":
            rev_seq[i] = "A"
    return "".join(rev_seq)


assert complement_a_strand_of_dna("AAAACCCGGT") == "ACCGGGTTTT", "test failed"

print(complement_a_strand_of_dna("ATGC"))
