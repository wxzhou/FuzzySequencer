# FuzzySequencer
Code for A fuzzy sequencer for rapid DNA fragment counting and genotyping

## Required softwares

|Software|Tested version|
|----|----|
|BWA|0.7.12-r1039|
|Samtools|1.10|
|Python|3.7.7|

## Files

* `genome/lambda_phage.fasta`: Reference genome sequence of lambda phage downloaded from: https://www.ncbi.nlm.nih.gov/nuccore/NC_001416.1
* `genome/bMK.fasta`: The BitSeq version of lambda phage genome (MK mode).
* `genome/bRY.fasta`: The BitSeq version of lambda phage genome (RY mode).
* `data/fasta`: Simulated sequencing reads of lambda phage genomic DNA. It is simulated that the same 100 DNA molecules are sequenced by all three sequencing methods: the conventional 4-base sequencing, BitSeq in MK mode, and BitSeq in RY mode. The header of each read is their starting sites on the genome.
* `data/sam`: Mapping results of the simulated sequencing reads in the SAM format.
* `genome_encoding.py`: The code that encode lambda phage genome into BitSeq formats.
* `build_genome_index.sh`: Build index for the three FASTA files in the `genome` folder using BWA.
* `mapping.sh`: Map the simulated sequencing reads, including BitSeq reads, to their corresponding genomes.

## How to run the demo

1. Run `genome_encoding.py` and it will encode `genome/lambda_phage.fasta` into `genome/bMK.fasta` and `genome/bRY.fasta` (already provided in the directory).
2. Run `build_genome_index.sh` and it will build the genome index for the three fasta files in the `genome` directory (already provided in the directory).
3. Run `mapping.sh` and it will map the simulated sequencing reads in the `data/fasta` directory to their corresponding genomes. The resulting SAM files are already provided in the `data/sam` directory. From the SAM files we can see that they are all mapped to the sites where they originated.
