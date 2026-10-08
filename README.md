# E. coli K-12 MG1655 GC Content Calculator
A Python project for calculating GC content from the complete genome of E. coli K-12 MG1655.

## About the Project

GC content is the percentage of guanine (G) and cytosine (C) bases present in a DNA sequence.
This project uses Python to read a FASTA sequence file and calculate the GC content of the *E. coli* K-12 MG1655 genome.

## 🦠 Organism

- Organism: *Escherichia coli*
- Strain: K-12 MG1655
- Sequence: Complete genome
- NCBI Accession: NZ_CP010444.1
 

## Method

The program:

1. Reads the DNA sequence from a FASTA file.
2. Removes the FASTA header and line breaks.
3. Counts the number of G and C nucleotides.
4. Calculates the total number of nucleotides.
5. Calculates GC content using:

FORMULA: GC Content (%) = ((G + C) / Total nucleotides) × 100



## 📁 Files

- `gc_content.py` – Python program for calculating GC content.
- `sequence.fasta` – FASTA sequence of *E. coli* K-12 MG1655.
- `README.md` – Project description and methodology.
  

## 💻 Technologies Used

- Python
- FASTA sequence data
  

## 🎯 Learning Objective

This project was created as an introductory bioinformatics project to practice Python file handling, string operations, and basic DNA sequence analysis.


## 🧬 Result

The calculated GC content is approximately 50.8%.


## 🔗 Data Source

NCBI Nucleotide Database
Accession: NZ_CP010444.1


## 🚀 Future Improvements

- Accept FASTA files provided by the user.
- Calculate GC content for multiple sequences.
- Add analysis of GC content in different regions of a genome.


