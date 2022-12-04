from Bio.Seq import Seq

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
