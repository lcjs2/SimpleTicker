from urllib.request import *
from datetime import date, datetime

class ticker_day:
    def __init__(self,date=date.today(),opn=1,high=1,low=1,close=1,volume=0, adj_close=1):
        self.date=date
        self.open=opn
        self.close=close
        self.high=high
        self.low=low
        self.volume=volume
        self.adj_close=adj_close

    def __str__(self):
        output=str(self.date)
        output+=" Open "+str(self.open)
        output+=" High "+str(self.high)
        output+=" Low "+str(self.low)
        output+=" Close "+str(self.close)
        output+=" Volume "+str(self.volume)
        return output


class ticker:
    def __init__(self, symbol=""):
        self.symbol=symbol
        self.data=[]

    def add(self, date, opn, high, low, close, volume,adj_close):
        self.data.append(ticker_day(date,opn,high,low,close,volume,adj_close))
        if len(self.data)>1 and date<self.data[-2].date:
            self.data.sort(key=lambda t: t.date)

    def add_text(self, csv):
        d,o,h,l,c,v,ac=csv.rstrip().split(',')
        self.add(datetime.strptime(d,'%Y-%m-%d'),float(o),float(h),float(l),float(c),float(v),float(ac))

    def length(self):
        return len(self.data)

    def __str__(self):
        output=self.symbol
        output+=" "+str(len(self.data))+" records"
        output+=" "+str(self.data[0].date)+" to "+str(self.data[-1].date)
        return output

    def display(self):
        print(self)
        for x in self.data:
            print(x)

    #Functions that return data from a particular day
    def close(self, day=-1):
        if day<0:
            day=self.length()+day
        return self.data[day].close

    # Functions that return lists
    def close_list(self, start=0, end=None):
        if end==None:
            end=len(self.data)
        return [x.close for x in self.data[start: end]]
    def volume_list(self, start=0, end=None):
         if end==None:
            end=len(self.data)
         return [x.volume for x in self.data[start: end]]


def yahoo_string(symbol, start_y, start_m, start_d, end_y=None, end_m=None, end_d=None):
    if end_y==None: end_y=datetime.now().year
    if end_m==None: end_m=datetime.now().month
    if end_d==None: end_m=datetime.now().day

    out="http://ichart.finance.yahoo.com/table.csv?s="
    out+=symbol.upper()
    out+="&d="+str(end_m-1)
    out+="&e="+str(end_d)
    out+="&f="+str(end_y)
    out+="&a="+str(start_m-1)
    out+="&b="+str(start_d)
    out+="&c="+str(start_y)
    return out

def load_ticker(symbol, start,end):
    print("Loading",symbol,start,"to",end,"...",end="")
    t = ticker(symbol)
    url_string=yahoo_string(symbol, start.year, start.month, start.day,
      end.year, end.month, end.day)
    data=[x.decode("utf-8").rstrip() for x in urlopen(url_string).readlines()[1:]]
    for day_data in data:
        t.add_text(day_data)
    print("loaded",t.length(),"days.")
    return t
