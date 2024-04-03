# In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". Your function receives one side of the DNA (string, except for Haskell); you need to return the other complementary side. DNA strand is never empty or there is no DNA at all (again, except for Haskell).

def DNA_strand(dna):
    COMPLEMENTS = {
        'A': 'T',
        'T': 'A',
        'C': 'G',
        'G': 'C'
    }

    # return ''.join(COMPLEMENTS[l] for l in dna)
    return dna.translate(str.maketrans('ATCG', 'TAGC'))

print(DNA_strand('ATTGC') == 'TAACG')
print(DNA_strand('GTAT') == 'CATA')
