# import packages 
import spacy
import os
import re
import pandas as pd
import sys
sys.path.append(".")
# import preprocessing file 
from utils.langutils import clean_text
from utils.langutils import rel_freq
from utils.langutils import unique_ent 

# load spacy as an nlp object 
nlp = spacy.load('en_core_web_md')

# define the path and directory for the data 
path = os.path.join("in", "USEcorpus")
dir = os.listdir(path)

for folder in dir:
    # going into every folder within the USEcorpus directory 
    folder_path = os.path.join("in", "USEcorpus", f'{folder}') 
    # saves the list of all files and directories in the path we just named above 
    folder_dir = os.listdir(folder_path)
    # making a large empty dataframe with the columns specified  
    df = pd.DataFrame(columns=["Filename", "RelFreq NOUN", "RelFreq VERB", "RelFreq ADJ", "RelFreq ADV", "Unique PERSON", "Unique LOC", "Unique ORG"])
    # for loop of what to do with each file using the above functions 
    for file in folder_dir:
        # selelcting each file in each folder 
        file_path = folder_path = os.path.join("in", "USEcorpus", f'{folder}', f'{file}') 
        # reading each file 
        with open(file_path, "r", encoding="latin-1") as f:
            raw_text = f.read() 
        # cleaning function
        text = clean_text(raw_text) 
        # making nlp object
        doc = nlp(text)  
        # relative frequency function
        relative_freq_n, relative_freq_v, relative_freq_adj, relative_freq_adv = rel_freq(doc) 
        # unique entity function
        unique_person_count, unique_loc_count, unique_orgs_count = unique_ent(doc) 
        # creating a new object with all the variables 
        new_dat = (file, relative_freq_n, relative_freq_v, relative_freq_adj, relative_freq_adv, unique_person_count, unique_loc_count, unique_orgs_count)
        # creating a pandas data frame with the new_dat object we just created for each file to fill 
        file_df = pd.DataFrame([new_dat],columns=["Filename", "RelFreq NOUN", "RelFreq VERB", "RelFreq ADJ", "RelFreq ADV", "Unique PERSON", "Unique LOC", "Unique ORG"])
        # concatenating the empty df data frame with the new file_df data frame and assigning it all to the df data frame; ignoring index to avoid issues with indexing them incorrectly 
        df = pd.concat([df, file_df], ignore_index=True)  
    # creating an outpath for each folder 
    outpath = os.path.join("out", f"{folder}.csv")
    # turning each data frame into a .csv file and saving it to each folder it belongs to 
    df.to_csv(outpath)

