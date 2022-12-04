import os
import sys
import argparse
from Bio.Seq import Seq

TRANSCRIPTION = {
    "A": "U",
    "T": "A",
    "C": "G",
    "G": "C",
}

TRANSLATION = {
    "['U', 'U', 'U']": "Phenylalanine",
    "['U', 'U', 'C']": "Phenylalanine",
    "['U', 'U', 'A']": "Leucine",
    "['U', 'U', 'G']": "Leucine",
    "['U', 'C', 'U']": "Serine",
    "['U', 'C', 'C']": "Serine",
    "['U', 'C', 'A']": "Serine",
    "['U', 'C', 'G']": "Serine",
    "['U', 'A', 'U']": "Tyrosine",
    "['U', 'A', 'C']": "Tyrosine",
    "['U', 'A', 'A']": "STOP",
    "['U', 'A', 'G']": "STOP",
    "['U', 'G', 'U']": "Cysteine",
    "['U', 'G', 'C']": "Cysteine",
    "['U', 'G', 'A']": "STOP",
    "['U', 'G', 'G']": "Tryptophan",
    "['C', 'U', 'U']": "Leucine",
    "['C', 'U', 'C']": "Leucine",
    "['C', 'U', 'A']": "Leucine",
    "['C', 'U', 'G']": "Leucine",
    "['C', 'C', 'U']": "Proline",
    "['C', 'C', 'C']": "Proline",
    "['C', 'C', 'A']": "Proline",
    "['C', 'C', 'G']": "Proline",
    "['C', 'A', 'U']": "Histidine",
    "['C', 'A', 'C']": "Histidine",
    "['C', 'A', 'A']": "Glutamine",
    "['C', 'A', 'G']": "Glutamine",
    "['C', 'G', 'U']": "Arginine",
    "['C', 'G', 'C']": "Arginine",
    "['C', 'G', 'A']": "Arginine",
    "['C', 'G', 'G']": "Arginine",
    "['A', 'U', 'U']": "Isoleucine",
    "['A', 'U', 'C']": "Isoleucine",
    "['A', 'U', 'A']": "Isoleucine",
    "['A', 'U', 'G']": "Methionine (START)",
    "['A', 'C', 'U']": "Threonine",
    "['A', 'C', 'C']": "Threonine",
    "['A', 'C', 'A']": "Threonine",
    "['A', 'C', 'G']": "Threonine",
    "['A', 'A', 'U']": "Asparagine",
    "['A', 'A', 'C']": "Asparagine",
    "['A', 'A', 'A']": "Lysine",
    "['A', 'A', 'G']": "Lysine",
    "['A', 'G', 'U']": "Serine",
    "['A', 'G', 'C']": "Serine",
    "['A', 'G', 'A']": "Arginine",
    "['A', 'G', 'G']": "Arginine",
    "['G', 'U', 'U']": "Valine",
    "['G', 'U', 'C']": "Valine",
    "['G', 'U', 'A']": "Valine",
    "['G', 'U', 'G']": "Valine",
    "['G', 'C', 'U']": "Alanine",
    "['G', 'C', 'C']": "Alanine",
    "['G', 'C', 'A']": "Alanine",
    "['G', 'C', 'G']": "Alanine",
    "['G', 'A', 'U']": "Aspartate",
    "['G', 'A', 'C']": "Aspartate",
    "['G', 'A', 'A']": "Glutamate",
    "['G', 'A', 'G']": "Glutamate",
    "['G', 'G', 'U']": "Glycine",
    "['G', 'G', 'C']": "Glycine",
    "['G', 'G', 'A']": "Glycine",
    "['G', 'G', 'G']": "Glycine",
}

def convert_input(args):
    if len(args) == 1:
        new_list = []
        new_item = ""
        counter = 0
        for letter in args[0]:
            counter += 1
            new_item += letter
            if counter == 3:
                counter = 0
                new_list.append(new_item.upper())
                new_item = ""
        if counter != 0:
            print("Wrong input, need to be n x 3 character")
        else:
            print("DNA sequence: " + ' '.join(new_list))
            return new_list
    else:
        continue_bool = True
        for protein in args:
            if len(protein) != 3:
                continue_bool = False
                break
        if not continue_bool:
            print("Wrong input, need to be n x 3 character")
        else:
            args = [element.upper() for element in args]
            print("DNA sequence: " + ' '.join(args))
            return args


def mRNA_sequence(args):
    continue_bool = True
    dna_sequence = args
    mRNA_sequence = ""
    try:
        for i in dna_sequence:
            for x in i:
                mRNA_sequence += TRANSCRIPTION[x]
            mRNA_sequence += ' '
    except:
        print("One of the letter is invalid.")
        continue_bool = False

    if continue_bool:
        print("mRNA sequence: " + str(mRNA_sequence))
        return mRNA_sequence.replace(" ", "")


def list_mRNA_sequence(mRNA_sequence):
    list_mRNA_sequence = list(mRNA_sequence)
    return list_mRNA_sequence


def formatted_mRNA_list(list_mRNA_sequence):
    formatted_mRNA_list = [
    str(list_mRNA_sequence[x:x + 3])
    for x in range(0, len(list_mRNA_sequence), 3)]
    return formatted_mRNA_list

def protein(formatted_mRNA_list):
    amino_acid_number = 0
    try:
        for i in formatted_mRNA_list:
            amino_acid_number += 1
            if TRANSLATION.get(i) == "STOP":
                print(amino_acid_number, ".", TRANSLATION.get(i), i)
                print("\n")
                sys.exit()
            else:
                print(amino_acid_number, ".", TRANSLATION.get(i), i)
    except:
        print("Please make sure that your DNA sequence is valid. Re-run this program to re-enter a valid sequence.")

def bio_python():
    #DNA
    my_dna = Seq('ATA GCG GCA ATT')
    my_dna = my_dna.replace(" ", "")
    my_dna = my_dna.complement()

    #mRNA
    my_mrna = my_dna.transcribe()
    print('my_mrna: ' + str(my_mrna))

    #Protein
    my_protein = my_mrna.translate(table=1, to_stop=True)

    print(str(my_protein))


def menu():
    parser = argparse.ArgumentParser(description='Thesis data process helper.')
    parser.add_argument('--translator', nargs="+", help='Translate from DNS to Proteins.')

    args = parser.parse_args()
    if args.translator:
        converted_input = convert_input(args.translator)
        if converted_input:
            mRNA = mRNA_sequence(converted_input)
            if mRNA:
                list_mRNA = list_mRNA_sequence(mRNA)
                formatted_mRNA = formatted_mRNA_list(list_mRNA)
                protein(formatted_mRNA)

if __name__ == "__main__":
    menu()

# ATA GCG GCA ATT
# https://parts.igem.org/Help:Protein_coding_sequences/Codon_table
# https://biopython.org/wiki/Seq