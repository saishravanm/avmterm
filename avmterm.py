import argparse 
import requests
from avmtermsetup import setupDone

##test out if virus grabber works
if(setupDone == -1):
    print("The set up has not been run yet. Please run avmterm-setup.py")
else:
    parser = argparse.ArgumentParser(description='Command Line web scraper tool for AVM')
    parser.add_argument('virus', metavar='virus', type=str, help='Specify the virus to get information from')
    args = parser.parse_args()
    virus = args.virus  

#if(virus == "cov2"):