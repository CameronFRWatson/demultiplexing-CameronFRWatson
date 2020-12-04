#!/usr/bin/env python

# Libraries

import argparse
import gzip
import matplotlib.pyplot as plt 

# Arguments

def get_args():
    parser = argparse.ArgumentParser(description = "A program to determine qscore mean at each base pos and return dist plot")
    parser.add_argument("-f", "--file", help = "fastq file", required = True)
    parser.add_argument("-r", "--readlen", help = "length of reads, in number of nucleotides", type = int, required = True)
    parser.add_argument("-t", "--plottitle", help = "Read 1, Read 2, Index 1, or Index 2", required = True)
    parser.add_argument("-p", "--plotfile", help = "name of plot file", required = True)
    return parser.parse_args()

args = get_args()

# Open the gzipped file

fh = gzip.open(args.file, "rt")

# Function to initialize an empty list

def init_list(array, value=0.0):
    '''This function takes an empty list and will populate it with
    the value passed in "value". If no value is passed, initializes list
    with number of elements equal to length of reads with values of 0.0.'''
    for i in range(0, args.readlen):
        array.append(value)
    return array

# convert ASCII to phred score function

def convert_phred(letter):
    """Converts a single ASCII character into a phred+33 score"""
    score = ord(letter) - 33
    return score

# Open the file, iterate through the lines, extracting qscore line, convert score, save running total in list

mean_scores = []
mean_scores = init_list(mean_scores) #creating an empty list to hold the summed scores
LN = 0
for line in fh:
    if LN%4 == 3: # only act on qscore line
        line = line.strip()
        for i in range(0, args.readlen):
            score = convert_phred(line[i])
            mean_scores[i] += score # keeping a running sum of qscores at each base position
    LN+=1
for j in range(0, args.readlen):
    mean_scores[j] = mean_scores[j]/(LN/4) #dividing each position by the number of records to obtain mean

fh.close()

# plot distribution

base_pos = list(range(0, args.readlen)) # x-axis, nucleotide position

plt.figure()
plt.bar(base_pos, mean_scores)
plt.title(f"Mean Qscore at each nucleotide position for {args.plottitle}")
plt.xlabel("Nucleotide position")
plt.ylabel("Mean quality score")

plt.savefig(f"./{args.plotfile}_distplot.png")
