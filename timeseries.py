from timeseries_classes import *
from timeseries_maths import *
from timeseries_utility import *
from urllib.request import *
from datetime import date, datetime, timedelta

#Load one year by default
end_date=date.today()
start_date=end_date-timedelta(days=365)

def main():
    while(True):
        line=input(">")
        command, line=next_word(line)
        commands.get(command,do_default)(line)

    t = load_ticker("AAPL", start_date, end_date)

    print("Mean closing price: ", mean(t.close_list()))
    print("Mean volume: ", mean(t.volume_list()))
    alpha, beta = linear_regression(t.close_list())
    print("Alpha: ",alpha," Beta: ",beta)
    mu, sigma = estimate_mu_sigma(t.close_list(),251)
    print("mu",mu,"sigma",sigma)
    bs_out=BS(t.close(-1),290,0,sigma,10)
    print("BS",bs_out)

def do_blah(line):
    print("OK",line)

def do_default(line):
    print("What!?")

commands={
'blah':do_blah
}

if __name__ == '__main__':
    main()