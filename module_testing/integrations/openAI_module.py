import openai
import pandas as pd 
import csv
from typing import List
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

openai_key = os.getenv('OPENAI_KEY')
from tenacity import (
    retry,
    stop_after_attempt,
    wait_random_exponential,
)  # for exponential backoff

# create Models class that stores the user declared models and settings configurations
class Models:

    def __init__(self, _config_name, _engine, _prompt, _temperature, _max_tokens, _top_p, _frequency_penalty, _presence_penalty):
        self.config_name = _config_name
        self.engine = _engine
        self.prompt = _prompt
        self.temperature = _temperature
        self.max_tokens = _max_tokens
        self.top_p = _top_p
        self.frequency_penalty = _frequency_penalty
        self.presence_penalty = _presence_penalty

# file_check() checks if the file meets our standardization to be parsed.  Specifically, it needs a column header "prompts", "Prompts", or "PROMPTS"
def file_check(file_name, promptColumn):
    with open(file_name, 'r') as file:
        try:
            prompts = pd.read_csv(file_name, usecols= [promptColumn])
        except:
            print("Prompt column not found in file.")
            return pd.DataFrame()
        return prompts

#create_copy() takes in user's file and creates a copy that we can append our completions to
def write_to_copy(file_name, dataframe):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    dataframe.to_csv(file_name+"_Completions_"+timestamp+".csv", index=False)

# add_columns() takes in a file and appends a column with rows of data for each model
def add_columns(dataframe, new_column, data):
    dataframe[new_column] = data

# this function will use exponential backoff to retry requests if rate limit is exceeded
@retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(6))
def completion_with_backoff(**kwargs):
    return openai.Completion.create(**kwargs)

# Main Function openAI_function():
# Purpose: Run user's .csv file through various openAI models; models and settings are chosen by the user and passed in as arguments to this function
# Inputs: 
# key - API key used by openAI to grant access to models
# FILEPATH - csv user file with X rows of prompts to be run through model(s)
# models - object with each model and deisgnated settings
# Outputs:
# NEWFILEPATH - appended file with completions (new column for each model settings configuration run)

def openAI_function(key, FILEPATH, models: List[Models], promptColumn):

    # assign openai.api_key to key input; hardcoding this with Mac's key for now
    # openai.api_key = key
    openai.api_key = openai_key

    # Check if file is compatible; if compatible, store prompts as dataframe
    with open(FILEPATH, 'r') as file:
        try:
            prompts = pd.read_csv(FILEPATH, usecols= [promptColumn])
        except:
            print("ERROR: Prompt column not found in file.")
            return
    
    # print("file is compatible. Feeding prompts to model configurations....")

    # Create outer for loops to iterate through each model; initialize CompletionsList to be emptied at the start of each new model; create inner for loop to iterate through prompts
    for model in models:
        CompletionsList = []
        for index, row in prompts.iterrows():
            completion = completion_with_backoff(engine=model.engine, prompt=row[promptColumn], temperature=model.temperature, max_tokens=model.max_tokens, 
                                                 top_p=model.top_p, frequency_penalty=model.frequency_penalty, presence_penalty=model.presence_penalty)
            CompletionsList.append(completion.choices[0].text)
            # print(f"{index+1}")
        add_columns(prompts, model.config_name, CompletionsList)
    
    # After all columns are writen to dataframe, write to a new copy of the user's .csv file called FILEPATH_Completions.csv
    write_to_copy(FILEPATH, prompts)
    # print("success.  new file created with model completions")



    