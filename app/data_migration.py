import spacy
import pandas as pd
import os

path = os.getcwd()


def tag_data(sentence):
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(sentence)
    new_doc = ""
    for i in range(len(doc)):
        new_doc = new_doc + doc[i].text + " " + doc[i].pos_ + " "
    return new_doc


def compile_data():
    df1 = pd.read_csv(path+'/dataset/dataset1.csv')
    df3 = pd.read_csv(path+'/dataset/dataset3.csv', header=None)
    df4 = pd.read_csv(path+'/dataset/dataset4.csv')
    df5 = pd.read_csv(path+'/dataset/dataset5.csv')
    df6 = pd.read_csv(path+'/dataset/dataset6.csv', header=None)
    df7 = pd.read_csv(path+'/dataset/dataset7.csv')
    df8 = pd.read_csv(path+'/dataset/dataset8.csv', header=None)
    with open(path+'/dataset/final_dataset.tsv', 'a') as write_csv:
        for x in list(df1['reviews.text']):
            if isinstance(x, str):
                write_csv.write(tag_data(x) + "\n")
        print("dataset1 completed")
        # for x in list(df3[0]):
        #     if isinstance(x, str):
        #         write_csv.write(tag_data(x) + "\n")
        # print("dataset3 completed")
        # for x in list(df4['reviews.text']):
        #     if isinstance(x, str):
        #         write_csv.write(tag_data(x) + "\n")
        # print("dataset4 completed")
        # for x in list(df5['reviews.text']):
        #     if isinstance(x, str):
        #         write_csv.write(tag_data(x) + "\n")
        # print("dataset5 completed")
        # for x in list(df6[0]):
        #     if isinstance(x, str):
        #         write_csv.write(tag_data(x) + "\n")
        # print("dataset6 completed")
        # for x in list(df7['Text']):
        #     if isinstance(x, str):
        #         write_csv.write(tag_data(x) + "\n")
        # print("dataset7 completed")
        # for x in list(df8[0]):
        #     if isinstance(x, str):
        #         write_csv.write(tag_data(x) + "\n")
        # print("dataset8 completed")
    return "Data compiled successfully.."

compile_data()