#! /bin/bash

fastq-dump -I SRR1544654 --split-files --gzip

sickle pe -f SRR1544654_1.fastq.gz -r  SRR1544654_2.fastq.gz -t sanger -o SRR1544654_1_trimmedOutput.fastq -p SRR1544654_2_trimmedOutput.fastq -s SRR1544654_trimmed_singles_file.fastq

bowtie2 -x /pylon5/mc5pl1p/anmolg/assignment2/PhiX/Illumina/RTA/Sequence/Bowtie2Index/genome -1 SRR1544654_1_trimmedOutput.fastq -2 SRR1544654_2_trimmedOutput.fastq --un SRR1544654_un_unaligned.fastq --al SRR1544654_un_aligned.fastq --un-conc SRR1544654_pair_aligned.fastq --al-conc SRR1544654_pair_conc_aligned.fastq -p 4