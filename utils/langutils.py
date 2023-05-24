# import packages 
import spacy
import os
import re
import pandas as pd


# creating a function to clean each text - *** might be issue with this cleaning ***
def clean_text(text):
    """
    A function to clean each text making it easier and limiting issues later
    Args:
        text (string): Cleaning the texts, replacing the \n - new lines and \t - tabs and the text between the <> characters with just a character of white space 

    Returns:
        text (string): the cleaned text  
    """
    text = re.sub("[\n\t]", " ", text)
    text = re.sub("<.*?>", " ", text)
    return text 


def rel_freq(doc):
    """ Finds the relative frequencies of specified parts of speech (POS) 

    Args:
        doc (nlp object):
        Creating a counter for each POS
        For loop which will add 1 to each counter for the specified POS 
        Calculating the relative frequency per 10,000 words, rounding it to 2 decimals points for ease 
    Returns:
        _type_(float): four floats 
    """ 
    noun_count = 0
    verb_count = 0
    adjective_count = 0
    adverb_count = 0
    for token in doc:
        if token.pos_ == "NOUN":
            noun_count +=1
        if token.pos_ == "VERB":
            verb_count +=1
        if token.pos_ == "ADJ":
            adjective_count +=1
        if token.pos_ == "ADV":
            adverb_count +=1
    relative_freq_n = round((noun_count/len(doc)) * 10000,2)
    relative_freq_v = round((verb_count/len(doc)) * 10000, 2)
    relative_freq_adj = round((adjective_count/len(doc)) * 10000, 2)
    relative_freq_adv = round((adverb_count/len(doc)) * 10000, 2)
    return relative_freq_n, relative_freq_v, relative_freq_adj, relative_freq_adv


def unique_ent(doc): 
    """
    Calculates the amount of unique entities in an nlp object
    Args:
        doc (nlp object): creates an empty list
        for each of the three entities, adds them to their specified list
        counts the total of unique entities of each type specified 

    Returns:
        doc (nlp object): integers for each entity type 
    """
    person = []
    loc = []
    orgs = []
 
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            person.append(ent.text)
        if ent.label_ == "LOC":
            loc.append(ent.text)
        if ent.label_ == "ORG":
            orgs.append(ent.text)
    # give the unique NER per each category 
    unique_person_count = len(set(person))
    unique_loc_count = len(set(loc))
    unique_orgs_count = len(set(orgs))
    return unique_person_count, unique_loc_count, unique_orgs_count


    if __name__=="__main__":
        pass
