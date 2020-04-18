# ex: http://rosalind.info/problems/prot/

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


def translate_rna_into_protein(seq: str):
    protein = ""
    for i in range(0, len(seq), 3):
        codon = seq[i:i+3]
        amino_acid = rna_codon_table[codon]
        if amino_acid == "Stop":
            break
        protein = protein + amino_acid
    return protein

assert translate_rna_into_protein(
    "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA") == "MAMAPRTEINSTRING", "test failed"

