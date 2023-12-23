<h1>avmterm - a command line filtering tool for AVM (Aerosol-transmitted Virus Mutations)</h1>
<p>can grab:</p>
<ul>
 <li>mutation site</li>
 <li>mutation level</li>
 <li>mutation type</li>
 <li>virus gene</li>
 <li>protein</li>
 <li>region</li>
 <li>NCBI ID virus genotype</li>
 <li>subtype</li>
 <li>clade</li> 
 <li>drug</li>
 <li>antibody</li>
 <li>vaccine</li> 
 <li>virus associated disease</li>
 <li>available clinical information</li>
 <li>virus sample</li>
 <li>country</li>
 <li>virus variants</li>
 <li>reference sequence</li>
 <li>transmissibility</li>
 <li>pathogenicity</li>
 <li>RT-PCR primers probes</li>
 <li>immune escape</li>
 <li>evidence</li>
 <li>protein introduction</li>
 <li>literature information</li>
 </ul>
 ...all based off of a query with a specified virus.

<h2>installation</h2>
 install requirements: 

 ```
 pip install -r requirements.txt
 ```
 run avmterm-setup to grab all necessary files and create necessary directories
 ```
 python avmterm-setup.py  
 ```
 ```
usage: avmterm.py [-h] [-v virus] [-f [filter ...]] [--verbose] [-o OUTPUT OUTPUT]

Command Line web scraper tool for AVM

options:
  -h, --help            show this help message and exit
  -v virus, --virus virus
                        Specify the virus to get information from(viruslist will return the list of viruses)
  -f [filter ...], --filter [filter ...]
                        Specify the filter category(s) to display information from(clist will return the list of categories)
  --verbose             Specify whether to print out all the results of the search
  -o OUTPUT OUTPUT, --output OUTPUT OUTPUT
                        Specify the filter output filetype(xlsx or csv) and filename
```

<h2>example:</h2> 
Grabs all Norovirus mutations which have a nonsynonymous mutation type,prints out the filtered data, and outputs the filtered data into a excel file called "data.xlsx"
<h3>input:</h3>

```
python3 avmterm.py -v noro -f muttype 'nonsynonymous mutation' --output xlsx 'data' 
```
All input data files are downloaded inside of ``./avmterm/data``as default
<h3>output:</h3>

```
 Mutation site    Mutation level  ... Transmissioin  The description of transmission mechanism
1     293-294delDV  Amino acid level  ...             -                                          -
2    358_360delGHY  Amino acid level  ...             -                                          -
3     295-296delHQ  Amino acid level  ...             -                                          -
4          384delQ  Amino acid level  ...             -                                          -
68           A104S  Amino acid level  ...             -                                          -
..             ...               ...  ...           ...                                        ...
404          Y452A  Amino acid level  ...             0                                          -
405          Y458Q  Amino acid level  ...             -                                          -
406          Y463H  Amino acid level  ...             -                                          -
407          Y480H  Amino acid level  ...             -                                          -
408          Y517H  Amino acid level  ...             -                                          -

[345 rows x 13 columns]
data.xlsx Successfully created

```
All outputted files are placed inside of ``./avmterm/output``as default


