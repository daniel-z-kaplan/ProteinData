from Bio import SeqIO
import json

filename = 'uniref100.fasta'
output_file = "fasta_parsed.txt" 


fasta_sequences = SeqIO.parse(open(filename),'fasta')

with open(output_file, "w") as out_file:
    for fasta in fasta_sequences:
        name, sequence = fasta.id, str(fasta.seq)         
        output = ""
        for char in sequence:
            output += char + " "
        output = output.rstrip()
        output = {"seq":output}
        output = json.dumps(output)
        out_file.write(str(output))
        out_file.write("\n")


from tokenizers import ByteLevelBPETokenizer

tokenizer = ByteLevelBPETokenizer()
tokenizer.train(files=["./"+output_file], vocab_size=50257, min_frequency=2, special_tokens=[
    "<s>",
    "<pad>",
    "</s>",
    "<unk>",
    "<mask>",
    '<|endoftext|>',
])

# Save files to disk
tokenizer.save_model(".", "model")