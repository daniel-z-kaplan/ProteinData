import os

metaclust = "https://metaclust.mmseqs.org/current_release/metaclust_all.gz"
uniref = "https://ftp.uniprot.org/pub/databases/uniprot/uniref/uniref100/uniref100.fasta.gz"

#MGNIFY
#http://ftp.ebi.ac.uk/pub/databases/metagenomics/peptide_database/current_release/
#http://ftp.ebi.ac.uk/pub/databases/metagenomics/peptide_database/current_release/README.txt


os.system("wget https://ftp.uniprot.org/pub/databases/uniprot/uniref/uniref100/uniref100.fasta.gz")
os.system("tar -xvf uniref100.fasta.gz")
