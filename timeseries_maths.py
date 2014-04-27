from math import *

def mean(x):
    total=0
    for i in x: total+=i
    return total/len(x)

def cov(x,y):
    mx=mean(x)
    my=mean(y)
    return mean([(x[i]-mx)*(y[i]-my) for i in range(len(x))])

def var(x):
    return cov(x,x)

def linear_regression(y,x=None):
    if x==None:
        x=range(len(y))
    beta = cov(x,y)/var(x)
    alpha = mean(y) - mean(x)*beta
    return alpha, beta

def estimate_m_sd(x, past_steps=10):
    log_returns=[]
    for i in range(len(x)-past_steps-1,len(x)-1):
        log_returns.append(log(x[i+1]/x[i]))
    m=mean(log_returns)
    sd=var(log_returns)**0.5
    return m, sd

