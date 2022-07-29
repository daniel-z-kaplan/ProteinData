First run download-data
Then run read_fasta (may want to change file names or not). Read fasta parses fasta file & does the tokenization stuff.
Cd to tools and run:
python3 preprocess_data.py --input ../fasta_parsed.txt --output-prefix my-gpt --vocab ../model-vocab.json --dataset-impl mmap --tokenizer-type GPT2BPETokenizer --merge-file ../model-merges.txt --workers 6 --chunk-size 100 --append-eod --json-key "seq"
