avmterm - A command line web scrapper tool for AVM (Aerosol-transmitted Virus Mutations) 

features: 
-Can grab:
 -mutation site
 -mutation level
 -mutation type
 -virus gene 
 -protein 
 -region 
 -NCBI ID virus genotype
 -subtype
 -clade, 
 -drug, 
 -antibody, 
 -vaccine, 
 -virus associated disease
 -available clinical information
 -virus sample
 -country
 -virus variants
 -reference sequence 
 -transmissibility 
 -pathogenicity 
 -RT-PCR primers probes 
 -immune escape 
 -evidence 
 -protein introduction 
 -literature information 
 
 ...all based off of a query with a specified virus.
 
usage: avmterm.py [-virus] [-filter] [-verbose] [-output] [-ft] [-filename]
setup: avmterm-setup.py  

python dependencies: argparse, requests, pandas (run pip install -r requirements.txt)
