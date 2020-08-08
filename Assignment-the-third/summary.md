# A brief summary of Bi622 Demultiplexing Assignment 3 - Cameron Watson

script: demultiplex.py
output: demultiplex_stats.txt
slurm script: dplex.srun
slurm standard out: dplex_slurm.out

Note: As of August, 7 2020, demultiplex.py is functional but very much a rough draft.
I plan to refactor quite a bit.

See dplex.srun for the specific options that demultiplex.py was ran with.

## Quality Cut-off justification

If either index for a given read pair contained any nucleotide with a quality score
of less than Q30, the entire read pair was parsed into the unknown/low quality file.
This was chosen partly based on the plot from Assignment 1 of index quality score 
distributions, and partly because indices should have a very stringent cut-off. 
An error in an index could potentially be the difference between a control sample
and a treatment sample. Additionally, a mean of Q30 did not seem appropriate because an
index could have a mean q-score of Q30, but still contain low confidence bases. This
decision resulted in a very high percentage of low-quality indices which would be
excluded from analysis. If I were to have done this again, I might have chosen a slightly
more lenient cut-off but I suppose this errs on the side of caution.

## Results

A brief summary of the results, for comprehensive results, see demultiplex_stats.txt
(including counts for all permutations of non-matching indices)

| Category | Percent of total read pairs |
| --- | --- |
| Matching pairs | 62.41% |
| Index Hopped Pairs | 0.09% |
| One or more unknown index | 8.47% |
| One or more low quality index | 29.02% |

| Sample Number | Percent of total matches |
| --- | --- |
| 1 | 2.55% |
| 2 | 1.87% |
| 3 | 2.04% |
| 4 | 2.81% |
| 6 | 3.15% |
| 7 | 1.06% |
| 8 | 10.81% |
| 10 | 21.92% |
| 11 | 5.75% |
| 14 | 1.14% |
| 15 | 1.9% |
| 16 | 2.62% |
| 17 | 3.37% |
| 19 | 5.05% |
| 21 | 2.73% |
| 22 | 1.17% |
| 23 | 13.27% |
| 24 | 3.06% |
| 27 | 2.09% |
| 28 | 3.29% |
| 29 | 1.27% |
| 31 | 1.16% |
| 32 | 3.35% |
| 34 | 2.59% |
