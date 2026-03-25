### Counting DNA Nucleotides
### 1st Rosalind Problem 
### https://rosalind.info/problems/dna/
### Code by adrijim18


### Create the dictionary for storing nucleotide counts

nucleotide_counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

dna_string = input("Please enter a DNA string: ")

def count_nucleotides(dna_string):
   
    for nucleotide in dna_string:
        if nucleotide in nucleotide_counts:
            nucleotide_counts[nucleotide] += 1

    return nucleotide_counts    

result = count_nucleotides(dna_string)

### First option
# print(f"A: {result['A']} C: {result['C']} G: {result['G']} T: {result['T']}")

### Exactly as Rosalind wants
print(result['A'], result['C'], result['G'], result['T'])


