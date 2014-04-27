from timeseries_classes import *
from timeseries_maths import *
from urllib.request import *
from datetime import date, datetime, timedelta

#Load one year by default
end_date=date.today()
start_date=end_date-timedelta(days=365)

def main():
    t = load_ticker("AAPL", start_date, end_date)

    print("Mean closing price: ", mean(t.close()))
    print("Mean volume: ", mean(t.volume()))
    alpha, beta = linear_regression(t.close())
    print("Alpha: ",alpha," Beta: ",beta)
    m, sd = estimate_m_sd(t.close(),251)
    print("mu",m,"sigma",sd)



if __name__ == '__main__':
    main()