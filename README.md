
# Assignment 1 - Extracting linguistic features using spaCy

## Github repo link 

This assignment can be found at my github [repo](https://github.com/ameerwald/cds_lang_exam_assignment1).  

## The data

The data is from The Uppsala Student English Corpus and more information can be found [here](https://ota.bodleian.ox.ac.uk/repository/xmlui/handle/20.500.12024/2457).

## Assignment description

This assignment asked for us to write one script that loops over every text file in the data, found in the ```in``` folder. From the data we were to extract the following:
    - Relative frequency of Nouns, Verbs, Adjective, and Adverbs per 10,000 words
    - Total number of *unique* PER, LOC, ORGS

Then save it in the following format:
- For each sub-folder (a1, a2, a3, ...) save a table which shows the following information:

|Filename|RelFreq NOUN|RelFreq VERB|RelFreq ADJ|RelFreq ADV|Unique PER|Unique LOC|Unique ORG|
|---|---|---|---|---|---|---|---|
|file1.txt|---|---|---|---|---|---|---|
|file2.txt|---|---|---|---|---|---|---|
|etc|---|---|---|---|---|---|---|


## Repository 

| Folder         | Description          
| ------------- |:-------------:
| In      | Data from The Uppsala Student English Corpus 
| Notes | Jupyter notebook notes to create scripts      
| Out  | Table for each sub folder   
| Src  | Py script plus in progress subfolder of script updates 
| Utils | Script of functions used in the src code |        


## To run the scripts 

1. Clone the repository, either on ucloud or something like worker2
2. From the command line, at the /cds_vis_exam_assignment1/ folder level, run the following lines of code. 

This will create a virtual environment, install the correct requirements.
``` 
bash setup.sh
```
While this will run the scripts and deactivate the virtual environment when it is done. 
```
bash run.sh
```

This has been tested on an ubuntu system on ucloud and therefore could have issues when run another way.

## Discussion of Results 
Each subfolder has a csv file with the requested table. Each table is quite long though and with 14 subfolders and therefore 14 tables it is too much to compare simply by visually comparing. Here is a very small sample from one of the tables to evaluate. 

|Filename|RelFreq NOUN|RelFreq VERB|RelFreq ADJ|RelFreq ADV|Unique PER|Unique LOC|Unique ORG|
|---|---|---|---|---|---|---|---|
|0135.a4.txt|1670.28|1008.68|715.84|574.84|8|0|2|
|2061.a4.txt|1317.31|1019.23|730.77|355.77|8|1|3|
|1067.a4.txt|1450.22|995.67|606.06|432.9|5|2|0|
|0216.a4.txt|1447.03|1300.6|473.73|292.85|8|0|4|
|3042.a4.txt|1289.34|1350.25|558.38|598.98|6|0|0|
|1032.a4.txt|1158.42|1287.13|683.17|554.46|7|1|1|

From this sample it appears that nouns are the most frequent word type followed by verbs, adverbs, and lastly adjectives per 1,000 words in these texts. There are also more unique person's and few locations and organizations. 