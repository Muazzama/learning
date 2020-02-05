import pandas as pd
import os
import random
import re
from collections import OrderedDict

path = os.getcwd()


def load_data(sample_size):
    filename = '/app/dataset/final_dataset.tsv'
    df = pd.read_csv(path+filename, sep='\t', header=None, error_bad_lines=False)
    print(len(set(df[0])))
    print(set(df[0]))
    return random.sample(set(df[0]), sample_size)


def clean_data(data):
    filtered_data = []
    for d in data:
        new_d = d.replace("<br />", "").replace("\n", "").replace('\'', "").replace(r".*", ".")
        filtered_data.append(new_d)
    return filtered_data


def generate_combinations(data_size, choice):
    data = load_data(data_size)
    sample_data = clean_data(data)
    combinations_list = []
    if choice == 'Noun-Verb':
        for sentence in sample_data:
            match = re.findall(r'((?:\w+ DET )?(?:\w+ NOUN )(?:\w+ VERB ))', sentence)
            if match:
                combinations_list.append(match)
    elif choice == 'Adjective-Noun':
        for sentence in sample_data:
            match = re.findall(r'((?:\w+ DET )?(?:\w+ ADJ )(?:\w+ NOUN ))', sentence)
            if match:
                combinations_list.append(match)
    else:
        for sentence in sample_data:
            match = re.findall(r'((?:\w+ DET )?(?:\w+ ADJ )(?:\w+ NOUN )(?:\w+ VERB ))', sentence)
            if match:
                combinations_list.append(match)
    return combinations_list


def compile_final_results(sample_size, choice):
    final_list = []
    while len(final_list)<sample_size:
        combo_list = generate_combinations(sample_size, choice)
        for combo in combo_list:
            for c in combo:
                words = iter(c.split())
                results = OrderedDict({})
                for i in words:
                    results[next(words)] = i
                final_list.append(results)
    return random.sample(final_list, sample_size)


# def generate_nv(sample_size, choice):
#     data = load_data(sample_size)
#     sample_data = clean_data(data)
#     nv_list = []
#     for d in sample_data:
#         if generate_combinations(d, choice):
#             nv_list.append(generate_combinations(d, choice))
#     return nv_list

# def generate_nv_combo(sentences):
#     match = re.findall(r'((?:\w+ DET )?(?:\w+ NOUN )(?:\w+ VERB ))', sentences)
#     return match
#     # nlp = spacy.load('en_core_web_sm')
#     # doc = nlp(sentences)
#     # new_doc = ""
#     # for i in range(len(doc)):
#     #     new_doc = new_doc + doc[i].text + " " + doc[i].pos_ + " "
#     # print(match.findall(new_doc))
#     # noun_adj_pairs = []
#     # for i in range(len(doc)):
#     #     j = i+1
#     #     if j < len(doc):
#     #         if (doc[i].pos_ == "NOUN" and doc[j].pos_ == "VERB"):
#     #             noun_adj_pairs.append((doc[i].text, doc[j].text, doc[i].pos_, doc[j].pos_))
#
#
# def generate_na_combo(sentences):
#     match = re.findall(r'((?:\w+ DET )?(?:\w+ ADJ )(?:\w+ NOUN ))', sentences)
#     return match
#     # nlp = spacy.load('en_core_web_sm')
#     # doc = nlp(sentences)
#     # new_doc = ""
#     # for i in range(len(doc)):
#     #     new_doc = new_doc + doc[i].text + " " + doc[i].pos_ + " "
#     # print(new_doc)
#     # noun_adj_pairs = []
#     # print(match.findall(new_doc))
#     # for i in range(len(doc)):
#     #     j = i+1
#     #     if j < len(doc):
#     #         if (doc[i].pos_ == "ADJ" and doc[j].pos_ == "NOUN"):
#     #             noun_adj_pairs.append((doc[i].text, doc[j].text, doc[i].pos_, doc[j].pos_))
#
#
# def generate_anv_combo(sentences):
#     match = re.findall(r'((?:\w+ DET )?(?:\w+ ADJ )(?:\w+ NOUN )(?:\w+ ADJ ))', sentences)
#     return match
#     # nlp = spacy.load('en_core_web_sm')
#     # doc = nlp(sentences)
#     # noun_adj_pairs = []
#     # for i in range(len(doc)):
#     #     j = i+1
#     #     k = i+2
#     #     if j < len(doc) and k < len(doc):
#     #         if (doc[i].pos_ == "NOUN" and doc[j].pos_ == "VERB" and doc[k].pos_ == "ADJ") or (doc[i].pos_ == "ADJ" and doc[j].pos_ == "NOUN" and doc[k].pos_ == "VERB"):
#     #             noun_adj_pairs.append((doc[i].text, doc[j].text, doc[i].pos_, doc[j].pos_))
#
#     # for i, token in enumerate(doc):
#     #     if token.pos_ not in ('NOUN', 'PROPN'):
#     #         continue
#     #     for j in range(i + 1, len(doc)):
#     #         if doc[j].pos_ == 'VERB':
#     #             for k in range(j + 1, len(doc)):
#     #                 if doc[k].pos_ is 'ADJ':
#     #                     noun_adj_pairs.append((token, doc[j], doc[k]))
#     #                     break
#
#     # for i, token in enumerate(doc):
#     #     if token.pos_ not in ('ADJ'):
#     #         continue
#     #     for j in range(i + 1, len(doc)):
#     #         if doc[j].pos_ == 'NOUN':
#     #             for k in range(j + 1, len(doc)):
#     #                 if doc[k].pos_ is 'VERB':
#     #                     noun_adj_pairs.append((token, doc[j], doc[k]))
#     #                     break

# def generate_an():
#     data = load_data(10)
#     sample_data = clean_data(data)
#     na_list = []
#     for d in sample_data:
#         na_list.append(generate_na_combo(d))
#     final_na_list = []
#     for combo in na_list:
#         final_na_list.append(x for x in combo)
#     return final_na_list
#
#
# def generate_anv():
#     data = load_data(10)
#     sample_data = clean_data(data)
#     anv_list = []
#     for d in sample_data:
#         anv_list.append(generate_anv_combo(d))
#     return anv_list


# nv = generate_nv()
# an = generate_an()
# anv = generate_anv()

# print("************NOUN-VERB LIST****************", "\n")
# print(compile_final_results(1000, "NOUN-VERB")[0:1000])
# print("************NOUN-ADJ LIST****************", "\n")
# print(an)
# print(len(an))
# print("************ADJ-NOUN-VERB LIST****************", "\n")
# print(anv)
# print(len(anv))


# compile_data()