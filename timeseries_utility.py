from datetime import date, datetime, timedelta

def input_date(prompt=""):
    out=date()
    if(prompt): print(prompt)
    out.year=input("Enter year:")
    out.month=input("Enter month:")
    out.day=input("Enter day:")
    return out

def next_word(line):
    out=line.split(" ",1)
    while(len(out)<2): out.append('')
    return out