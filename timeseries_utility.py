from datetime import date, datetime, timedelta
from timeseries import *

def input_date(prompt=""):
    out=date()
    if(prompt): print(prompt)
    out.year=input("Enter year:")
    out.month=input("Enter month:")
    out.day=input("Enter day:")
    return out

def next_word(line):
    out=line.split(" ",1)
    while(len(out)<2): out.append('') #Always return two (possibly empty) things
    return out

def parse_line_pairs(line):
    #Return a list of word pairs x=y
    pairs={}
    while(line):
        word, line=next_word(line)
        if('=' in word):
            pair=word.split("=")
            pairs[pair[0]]=pair[1]
    return pairs

def parse_line(line, vars={}):
    #takes a line and produces a dictionary of line pairs x:y
    #also accepts a dictionary of symbol:prompt and prompts, if necessary,
    #for missing ones.

    line_pairs=parse_line_pairs(line)
    print(line_pairs)
    for x in vars:
        if x not in line_pairs:
            line_pairs[x]=input(vars[x]+':')
    return line_pairs



def get_bs_data(line):
    vars={
    's':'Spot price',
    'k':'Strike price',
    'r':'Risk-free rate',
    'sigma':'Volatility',
    't':'Time to expiry'
    }
    pairs=parse_line(line, vars)
    s=float(pairs['s'])
    k=float(pairs['k'])
    r=float(pairs['r'])
    sigma=float(pairs['sigma'])
    t=float(pairs['t'])
    return s,k,r,sigma,t