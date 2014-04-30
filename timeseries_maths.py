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

def estimate_mu_sigma(x, past_steps=10):
    log_returns=[]
    for i in range(len(x)-past_steps-1,len(x)-1):
        log_returns.append(log(x[i+1]/x[i]))
    sigma=var(log_returns)**0.5
    mu=mean(log_returns) + (sigma**2)/2
    return mu, sigma

def BS(S,K,r,sigma,T):
    d1=BS_d1(S,K,r,sigma,T)
    d2=BS_d2(S,K,r,sigma,T)
    return phi(d1)*S - phi(d2)*K*exp(-r*T)

def BS_d1(S,K,r,sigma,T):
    out = log(S/K) + (r + (sigma**2)/2)*(T)
    out /= sigma*sqrt(T)
    return out

def BS_d2(S,K,r,sigma,T):
    return BS_d1(S,K,r,sigma,T) - sigma*sqrt(T)

def erf(x):
    # Error function
    # Magic approximation!
    a1 =  0.254829592
    a2 = -0.284496736
    a3 =  1.421413741
    a4 = -1.453152027
    a5 =  1.061405429
    p  =  0.3275911

    t = 1/(1 + p*abs(x))
    y = 1 - (((((a5*t + a4)*t) + a3)*t + a2)*t + a1)*t*exp(-x*x)

    return y if x>0 else -y

def phi(x):
    # Cumulative normal distribution
    return (1+erf(x/sqrt(2)))/2