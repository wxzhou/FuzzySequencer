bMK_trans = ''.maketrans('ACGT', 'AATT')
bRY_trans = ''.maketrans('ACGT', 'ATAT')

with open('genome/lambda_phage.fasta') as src, open('genome/bMK.fasta', 'w') as bMK, open('genome/bRY.fasta', 'w') as bRY:
    for line in src:
        if line.startswith('>'):
            bMK.write(line)
            bRY.write(line)
        else:
            bMK.write(line.upper().translate(bMK_trans))
            bRY.write(line.upper().translate(bRY_trans))