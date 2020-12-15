## Demultiplexing and Index hopping

*Cameron Watson*

This repository contains demultiplex.py, a tool for demultiplexing paired-end Illumina reads with dual matched indices. 

demultiplex.py can be called from the command line with the following arguments:

```
--read_one         R1 Fastq file (forward reads)
--read_two         R2 Fastq file (forward indices)
--read_three       R3 Fastq file (reverse indices)
--read_four        R4 Fastq file (reverse reads)
--indices_file     Plain text file with a list of indices used
```

Reads are demultiplexed by index pair, with matching pairs outputted to separate forward and reverse files (file names and read header are appended with their indices). Read pairs with non-matching indices (index-hopped) will be outputted to separate forward and reverse index-hopped files. Finally, a forward and a reverse file for read pairs with at least one unknown (N-containing) or low-quality index will also be outputted separately. 

demultiplex.py also outputs a convenient summary file containing the proportion of matched pairs, index hopped pairs, low quality index pairs, and unkown index pairs. An example of this summary file can be found in the demult_supp subdirectory. 

## Quality score distribution

qscore_dist.py generates a per-base distribution of quality scores for a fastq file. The quality score at each position is averaged across all reads in the file and a histogram of this distribution is returned. 

qscore_dist.py has the following arguments that can be called from the command-line:

```
--file  fastq file
--readlen   length of reads, in number of nucleotides
--plottitle plot title
--plotfile  name of file for plot (names is prepended to "_distplot.png")
```

Sample inputs, outputs, and supplemental files for both of these scripts can be found in the remaining subdirectories in this repository. Bash scripts for running the Python scripts as batch jobs on an HPC can also be found here.
