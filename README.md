# Harry Potter MapReduce – Assignment

This project implements the MapReduce model using Python.

## Tasks completed

1. Extracted required pages from the Harry Potter PDF based on my DOB.
2. File1 – Word count using MapReduce.
3. File2 – Count of non-English words using MapReduce.

## How it works

Mapper:
Reads the text and emits (word, 1)

Shuffle:
Groups same words together

Reducer:
Adds the counts and gives final result

## Files

File1.txt – Extracted text for wordcount  
File2.txt – Extracted text for non-English detection  

file1_wordcount_output.txt – Output for File1  
file2_non_english_output.txt – Output for File2  

SNP_Assignment_2.ipynb – Complete implementation
