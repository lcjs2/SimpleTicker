from timeseries_classes import *
from timeseries_maths import *
from timeseries_utility import *
from urllib.request import *
from datetime import date, datetime, timedelta
import sys

#Load one year by default
end_date=date.today()
start_date=end_date-timedelta(days=365)

tickers=[]

def main():
    #a=[690, 650,560,550,540,530,520,490,460,340]
    #b=[0.05,0.2,33, 42, 52, 62, 72, 102,132,252]
    #plot(a,[implied_vol(592,a[i],0,5,b[i]) for i in range(len(a))])
    while(True):
        line=input(">")
        command, line=next_word(line)
        commands.get(command,do_default)(line)


    #print("Mean closing price: ", mean(t.close_list()))
    #print("Mean volume: ", mean(t.volume_list()))
    #alpha, beta = linear_regression(t.close_list())
    #print("Alpha: ",alpha," Beta: ",beta)
    #mu, sigma = estimate_mu_sigma(t.close_list(),251)
    #print("mu",mu,"sigma",sigma)
    #bs_out=BS(t.close(-1),290,0,sigma,10)
    #print("BS",bs_out)


def get_ticker(symbol):
    symbol=symbol.strip().upper()
    for t in tickers:
        if t.symbol==symbol:
            return t
    t = load_ticker(symbol, start_date, end_date)
    tickers.append(t)
    return t

def do_print(line):
    print(line)

def do_quit(line):
    sys.exit(0)

def do_default(line):
    print("What!?")

def do_load(line):
    while(line):
        symbol, line=next_word(line)
        get_ticker(symbol)
    do_show("")

def do_show(line):
    print('Currently loaded:')
    for t in tickers:
        print(t)

def do_mean(line):
    symbol, line=next_word(line)
    t=get_ticker(symbol)
    print("Mean closing price:", mean(t.close_list()))

def do_vol(line):
    symbol, line=next_word(line)
    t=get_ticker(symbol)
    mu, sigma=estimate_mu_sigma(t.close_list())
    print(symbol,"mu:",mu,"sigma:",sigma)

def do_bs_call(line):
    s,k,r,sigma,t=get_bs_data(line)
    print("Call option:", bs(s,k,r,sigma,t))

def do_bs_put(line):
    s,k,r,sigma,t=get_bs_data(line)
    print("Put option:", bs(s,k,r,sigma,t))

def do_lsr(line):
    symbol, line=next_word(line)
    t=get_ticker(symbol)
    alpha, beta = linear_regression(t.close_list())
    print('Least squares regression', symbol,'closing price')
    print("Alpha: ",alpha)
    print("Beta: ",beta)

def do_default(line):
    print("What!?")

commands={
'print':do_print,
'load':do_load,
'show':do_show,
'quit':do_quit,
'q':do_quit,
'lsr': do_lsr,
'mean':do_mean,
'call':do_bs_call,
'put':do_bs_put,
'vol':do_vol
}

if __name__ == '__main__':
    main()