# ex: http://rosalind.info/problems/rna/
def translate_dna_into_rna(dna: str):
        dna=dna.replace("T", "U")
        return dna
    

assert translate_dna_into_rna("GATGGAACTTGACTACGTAAATT")=="GAUGGAACUUGACUACGUAAAUU", "test failed"

print(translate_dna_into_rna("GAT"))
