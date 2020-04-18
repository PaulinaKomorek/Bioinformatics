# ex: http://rosalind.info/problems/mrna/
rna_codon_table = {"UUU": "F",      "CUU": "L",      "AUU": "I",      "GUU": "V",
                   "UUC": "F",      "CUC": "L",      "AUC": "I",      "GUC": "V",
                   "UUA": "L",      "CUA": "L",      "AUA": "I",      "GUA": "V",
                   "UUG": "L",      "CUG": "L",      "AUG": "M",      "GUG": "V",
                   "UCU": "S",      "CCU": "P",      "ACU": "T",      "GCU": "A",
                   "UCC": "S",      "CCC": "P",      "ACC": "T",      "GCC": "A",
                   "UCA": "S",      "CCA": "P",      "ACA": "T",      "GCA": "A",
                   "UCG": "S",      "CCG": "P",      "ACG": "T",      "GCG": "A",
                   "UAU": "Y",      "CAU": "H",      "AAU": "N",      "GAU": "D",
                   "UAC": "Y",      "CAC": "H",      "AAC": "N",      "GAC": "D",
                   "UAA": "Stop",   "CAA": "Q",      "AAA": "K",      "GAA": "E",
                   "UAG": "Stop",   "CAG": "Q",      "AAG": "K",      "GAG": "E",
                   "UGU": "C",      "CGU": "R",      "AGU": "S",      "GGU": "G",
                   "UGC": "C",      "CGC": "R",      "AGC": "S",      "GGC": "G",
                   "UGA": "Stop",   "CGA": "R",      "AGA": "R",      "GGA": "G",
                   "UGG": "W",      "CGG": "R",      "AGG": "R",      "GGG": "G"}

def number_of_rna_combinations(protein: str):
    combinations=1
    for i in protein:
        count=0
        for j in rna_codon_table:
            if i==rna_codon_table[j]:
                count=count+1
        combinations=combinations*count
    combinations=combinations*3             #3 STOP codons
    return combinations%1000000

assert number_of_rna_combinations("MA")==12, "test failed"

#print(number_of_rna_combinations("RRSSAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"))