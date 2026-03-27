### 3rd Rosalind Problem
### Complementing a Strand of DNA
### https://rosalind.info/problems/revc/

print("Hi! Welcome to this DNA complementing program :)")

dna_strand = input("Please enter a DNA strand: ")

### A - T
### G - C
### And then flip the whole string

def comp_string(dna_strand):
    comp_string = ""

    for base in dna_strand:
        if base == "A":
            comp_string += "T"
        elif base == "T":
            comp_string += "A"
        elif base == "G":
            comp_string += "C"
        elif base == "C":
            comp_string += "G"

    return comp_string

new_string = comp_string(dna_strand)

final_string = new_string[::-1] ### Just flip the whole thing


print(f"This is your complementary string! {final_string}")

