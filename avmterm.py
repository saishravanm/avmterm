import argparse 
import requests
from avmtermsetup import setupDone
import pandas as pd


##Map each provided virus to the given spreadsheet
virusData ={
    'influenza':'./data/Influenzavirus A H1N1.xlsx',
    'measles':'./data/Measles virus.xlsx',
    'mers':'./data/MERS-COV.xlsx',
    'noro':'./data/Norovirus.xlsx',
    'hrsv':'./data/Human rhinovirus.xlsx',
    'mcov':'./data/MERS-COV.xlsx',
    'scov1':'./data/SARS-COV.xlsx',
    'scov2':'./data/SARS-COV-2.xlsx',
    'vzv':'./data/Varicella-Zoster virus.xlsx'
}
##Map each given category filter to the filter on the table
categoriesData={
    'msite':'Mutation site',
    'mlevel':'Mutation level',
    'gorp':'Gene/Protein/Region Type',
    'ncbi':'NCBI Gene ID',
    'country':'Country',
    'muttype':'Mutation type',
    'gsc':"Genotype/Subtype/Clade",
    'sample':'Sample',
    'variants':'Variants',
    'mav':'Medicine/Antibody/Vaccine',
    'transmission':'Transmissioin',
    'vrs':'Viral reference sequence',
    'transmech':'The description of transmission mechanism'
    
}

##check if the setup script has been run 
if(setupDone == -1):
    print("The setup has not been run yet. Please run avmterm-setup.py")
else:
    ##Set up the arguments
    parser = argparse.ArgumentParser(description='Command Line web scraper tool for AVM')
    
    parser.add_argument('-v','--virus',metavar='virus', action='store',type=str, help='Specify the virus to get information from(viruslist will return the list of viruses)')
    parser.add_argument('-f','--filter',nargs='*',metavar='filter',action='store',type=str,help='Specify the filter category(s) to display information from(clist will return the list of categories)')
    parser.add_argument('--verbose',action='store_true',help='Specify whether to print out all the results of the search')
    parser.add_argument('-o','--output',action='store', nargs=2,type=str,help='Specify the filter output filetype(xlsx or csv) and filename')
    args = parser.parse_args()

#if the user wants to list either the viruses or categories -> process it
if(args.virus == 'viruslist'):
    print("Human rhinovirus (rhino)\nInfluenzavirus A (influenza)\nMeasles virus (measles)\nMERS-COV (mers)\nNorovirus (noro)\nHuman respiratory syncytial virus (hrsv)\nMERS-COV (mcov)\nSARS-COV1 (scov1)\nSARS-COV2 (scov2)\nVaricella-Zoster virus (vzv)")
if(args.filter == 'clist'):
    print("Mutation Site (msite)\nMutation Level(mlevel)\nGene/Protein(gorp)\nNCBI(ncbi)\nCountry(country)\nMutation Type(muttype)\nGenotype/Subtype/Clade(gsc)\nSample(sample)\nVariants(variants)\nMedicine/Antibody/Vaccine(mav)\nTransmission(transmission)\nViral Transmission Mechanism (vrs)\nTransmission Mechanism(transmech)")
else: 
    cols = []
    #add all the categories present in the spreadsheet
    for key in categoriesData:
        cols.append(categoriesData.get(key))
    
    #read the actual spreadsheet
    df = pd.read_excel(virusData.get(args.virus),usecols=cols)
   # print(args.filter[0])
   # print(args.filter[1])
   
   #set the default conditions to itself
    conditions = ((df[categoriesData.get(args.filter[0])]) == args.filter[1])
    x = 0
    
    #loop through all the provided arguments and use "&&" to filter
    while x < (len(args.filter)):
     conditions = conditions & ((df[categoriesData.get(args.filter[x])]) == args.filter[x+1])
     #print(args.filter[x] + " " + args.filter[x+1])
     x = x + 2
#check if verbose is true     
if(args.verbose is True):
    print(df[conditions])
#check if we're outputting to a file, if so, create the file
if(args.output != None):
    if(len(args.output) != 0):
        if(args.output[0] == 'xlsx'):
           df[conditions].to_excel('./output/'+args.output[1]+'.xlsx',index=False)    
           print(args.output[1] + '.xlsx ' + "Successfully created")
    if(args.output[0] == 'csv'):
        df[conditions].to_csv('./output/'+args.output[1]+'.csv',index=None,header=True)
        print(args.output[1] + '.csv ' + "Successfully created")

        
        