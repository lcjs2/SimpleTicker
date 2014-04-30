from timeseries_classes import *
from timeseries_maths import *
from urllib.request import *
from datetime import date, datetime, timedelta

#Load one year by default
end_date=date.today()
start_date=end_date-timedelta(days=365)

def main():
    t = load_ticker("AAPL", start_date, end_date)

    print("Mean closing price: ", mean(t.close_list()))
    print("Mean volume: ", mean(t.volume_list()))
    alpha, beta = linear_regression(t.close_list())
    print("Alpha: ",alpha," Beta: ",beta)
    mu, sigma = estimate_mu_sigma(t.close_list(),251)
    print("mu",mu,"sigma",sigma)
    print("BS data",t.close(-1),500,0.02,sigma,10)
    bs_out=BS(t.close(-1),290,0,sigma,10)
    print("BS",bs_out)



if __name__ == '__main__':
    main()