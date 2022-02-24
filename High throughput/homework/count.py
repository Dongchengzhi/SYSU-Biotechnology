# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 12:39:55 2022

@author: pc
"""

import os 
os.chdir("D:/desk/高通量与数据分析/上机实验/Second")

# Question 1
def percent_Cal_1_1(DNA_seq):
    count_A = 0
    count_T = 0 
    count_C = 0
    count_G = 0
    for i in DNA_seq:
        if i == "A":
            count_A += 1
        elif i == "T":
            count_T += 1
        elif i == "C":            
            count_C += 1
        elif i == "G":
            count_G += 1
    all_count = len(DNA_seq)
    precent_A = count_A*100/all_count
    precent_T = count_T*100/all_count
    precent_C = count_C*100/all_count
    precent_G = count_G*100/all_count    

    print("A | Frequency:{0} | Percentage:{1:.2f}%".format(count_A,precent_A))
    print("T | Frequency:{0} | Percentage:{1:.2f}%".format(count_T,precent_T))
    print("C | Frequency:{0} | Percentage:{1:.2f}%".format(count_C,precent_C))
    print("G | Frequency:{0} | Percentage:{1:.2f}%".format(count_G,precent_G))

def percent_Cal_1_2(DNA_seq):
    count_ls = set(DNA_seq)
    all_count = len(DNA_seq)/100
    for x in count_ls:
        frequency = DNA_seq.count(x)
        percent = frequency/all_count
        print("{0} | Frequency:{1} | Percentage:{2:.2f}%".format(x,frequency,percent))

def percent_Cal_1_3(DNA_seq):
    count_ls = dict()
    all_count = len(DNA_seq)/100
    for x in DNA_seq:
        if x in count_ls:
            count_ls[x] += 1
        else:
            count_ls[x] = 1
    for key in count_ls:
        count = count_ls[key]
        percent = count/all_count
        print("{0} | Frequency:{1} | Percentage:{2:.2f}%".format(key,count,percent))
    

def text_to_DNA(text_file_name):
    text_file = open(text_file_name)
    lines = text_file.readlines()
    text_file.close()
    line = [x.strip() for x in lines[1:]]
    lines = ''.join(line)
    DNA_seq = lines.upper()
    return DNA_seq

text_file_name = "chrM.fa"
DNA_seq = text_to_DNA(text_file_name)
print("Question1: Calculate the percentage of each base of ATCG in the chrM chromosome by Funtion1.1:")
percent_Cal_1_1(DNA_seq)
print("Question1: Calculate the percentage of each base of ATCG in the chrM chromosome by by Funtion1.2:")
percent_Cal_1_2(DNA_seq)
print("Question1: Calculate the percentage of each base of ATCG in the chrM chromosome by by Funtion1.3:")
percent_Cal_1_3(DNA_seq)

# Question 2 
insulin = "GIVEQCCTSICSLYQLENYCNFVNQHLCGSHLVEALYLVCGERGFFYTPKT"
print("Question2: Calculate insulin = GIVEQCCTSICSLYQLENYCNFVNQHLCGSHLVEALYLVCGERGFFYTPKT amino acid frequency in insulin sequence by Funtion1.2:")
percent_Cal_1_2(insulin)
print("Question2: Calculate insulin = GIVEQCCTSICSLYQLENYCNFVNQHLCGSHLVEALYLVCGERGFFYTPKT amino acid frequency in insulin sequence by Funtion1.3:")
percent_Cal_1_3(insulin)

# Question 3
def percent_Cal_3_1(DNA_seq):
    count_ls = dict()
    for i in range(len(DNA_seq)-4):
        seq_short = DNA_seq[i:i+5]
        if seq_short in count_ls:
            count_ls[seq_short] += 1
        else:
            count_ls[seq_short] = 1
    for key in count_ls:
        count = count_ls[key]
        print("{0} | Count:{1}".format(key,count))

print("Question3: Run 5bp windows in the sequence PRQTEINSEQWENCE and count the number of occurrences of each window in the sequence by Funtion3.1:")
sequence = "PRQTEINSEQWENCE"
percent_Cal_3_1(sequence)

# Question4
print("Question4: Calculate GC percentage in chrM.fa:")
count_GC = (DNA_seq.count("G")+DNA_seq.count("C"))/len(DNA_seq)
print("GC percentage in chrM: {0:.2f}".format(count_GC))
