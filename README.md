# INF502 Project: DNA Sequence Matching

## Table of Contents

-   [Features](#features)
-   [Implementation](#implementation)
	-   [Input](#input)
	-   [Shifting Sequences](#shift)
	-   [Finding highest matches](#match)
	-   [Finding longest chain](#chain)
	-   [Exception Handling](#exception)
-   [Usage](#usage)

## Features

-   Find the highest no. of pair wise nucleotide matches of two DNA sequences
-   Find the longest contiguous chain of pair wise nucleotide matches of two DNA sequences
-   File/Console Input
-   Interactive Menu

## Implementation

### Input 

There are two way to input the DNA sequences.

-   Console Input
-   File Input

In the case of file input, user has to provide the name of the file through console (the file must be residing in the same folder, else the relative path has to be provided.). User then has to provide the maximum no. of shifts allowed for each of the sequences.

### Implementing Shift of the DNA Sequence

To implement a shift of size k, we just appended k whitespaces infront of the sequence.

``` python
sequence = ' ' * k + sequence
```

### Finding highest no. of matches across diferent shifts

The steps to find the higest no. of matches by shifting sequence1:

1.  Initilize, k = 1 and max_score = 0
2.  Set score = 0
3.  Shift the first secquence by k cells
4.  Iterate over the two sequences and make pairwise comparison.
5.  If the pair is equal, add 1 to score, score = score + 1. If score is greater than the max_score, update max_score to score.
6.  Increment k by 1. If K is less than the max_shift, go back to step 2 and repeat.

The same steps were repeated for sequence 2. We measure and report the max_score across all posible shifting.

### Finding longest contiguous chain across diferent shifts

The steps to find the longest contiguous chain by shifting sequence1:

1.  Initilize, k = 1 and longest_chain = 0
2.  Set chain = 0
3.  Shift the first secquence by k cells
4.  Iterate over the two sequences and make pairwise comparison.
5.  If the pair is identical, add 1 to chain, chain = chain + 1. If the value chain is greater than the longest_chain, update longest_chain to chain.
6.  Othersie if the pair isn't identical, reset chain to 0, chain = 0.
7.  Increment k by 1. If K is less than the max_shift, go back to step 2 and repeat.

The same steps were repeated for sequence 2. We measure and report the longest_chain across all posible shifting.

### Exception Handling

-   When working with file input, if there exists no file with the name the user has provided, a *FileNotFoundError* exception is handled and the user is asked to provided the correct filename again.
-   When taking user input for the maximum shift count, if the provided value is not a number, a *ValueError* exception handled and the user is asked again to provide a number for the max shift.

## Usage {#usage}

Just run the main.py file to get started

``` python
python3 main.py
```

It will start an interactive menu. After providing the input and max shift count, the program will display the result for various combinations of shifting of the DNA sequences.
