bwa index -p genome/lambda_phage.fasta genome/lambda_phage.fasta
bwa index -p genome/bMK.fasta genome/bMK.fasta
bwa index -p genome/bRY.fasta genome/bRY.fasta

samtools faidx genome/lambda_phage.fasta
samtools faidx genome/bMK.fasta
samtools faidx genome/bRY.fasta
