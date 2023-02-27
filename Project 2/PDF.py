# Random Signals
# Project 2
# Patrick Laverty

import matplotlib.pyplot as mplt
import numpy as np
import scipy.stats as stats

i = 10000 # amt of random variables
mean = 0
variance = 1
standardDeviation = np.sqrt(variance)

xpoints = s = np.random.normal(mean,standardDeviation,i)
ypoints = s = np.random.normal(mean,standardDeviation,i)

## creating Z and theta
Z = []
for j in range(0,i):
    Z.append(np.sqrt(xpoints[j] ** 2 + ypoints[j] ** 2))
Zmode = stats.mode(Z, keepdims=False).mode

## creating Theta values
theta = []
for j in range(0,i):
    theta.append(np.arctan(ypoints[j]/xpoints[j]) + np.pi)
Tmode = stats.mode(theta, keepdims=False).mode

## Plot Z Value Distribution
mplt.subplot(2,8,1)
mplt.hist(Z, 100, label="Z Values")
mplt.title("Z Value Distribution")

## Binomial Density Distributon
bdist_vars_Z = np.random.binomial(Z, 1, i)
mplt.subplot(2,8,2)
mplt.hist(bdist_vars_Z, 100, density=True, label="Binomial")
mplt.title("Binomial Distribution")

## Poisson Density Distribution
pdist_vars_Z = np.random.poisson(Z, len(Z))
mplt.subplot(2,8,3)
mplt.hist(pdist_vars_Z, 100, density=True, label="Poisson")
mplt.title("Poisson Distribution")

## Laplacian Density Distribution
ldist_vars_Z = np.random.laplace(Z, Zmode, i)
mplt.subplot(2,8,4)
mplt.hist(ldist_vars_Z, 100, density=True, label="Laplacian")
mplt.title("Laplacian Distribution")

## Plot Rayleigh Distribution
rdist_vars_Z = np.random.rayleigh(Zmode, i)
mplt.subplot(2,8,5)
mplt.hist(rdist_vars_Z, 100, density=True, label="Rayleigh", color='red')
mplt.title("Rayleigh Distribution")

## Exponential Density Distribution
edist_vars_Z = np.random.exponential(Z, len(Z))
mplt.subplot(2,8,6)
mplt.hist(edist_vars_Z, 100, density=True, label="Exponential")
mplt.title("Exponential Distribution")

## Uniform Density Distribution
udist_vars_Z = np.random.uniform(0, Z[i-1], i)
mplt.subplot(2,8,7)
mplt.hist(udist_vars_Z, 100, density=True, label="Uniform")
mplt.title("Uniform Distribution")

## Guassian Density Distribution
gdist_vars_Z = np.random.normal(mean, standardDeviation, i)
mplt.subplot(2,8,8)
mplt.hist(gdist_vars_Z, 100, density=True, label="Gaussian (Normal)")
mplt.title("Gaussian Distribution")



### Theta distributions:
## Plot Theta Value Distribution
mplt.subplot(2, 8, 9)
mplt.hist(theta, 100, label="Theta Values")
mplt.title("Theta Value Distribution")

## Binomial Density Distributon
bdist_vars_T = np.random.binomial(theta, 1, i)
mplt.subplot(2,8,10)
mplt.hist(bdist_vars_T, 100, density=True, label="Binomial")
mplt.title("Binomial Distribution")

## Poisson Density Distribution
pdist_vars_T = np.random.poisson(theta, len(theta))
mplt.subplot(2,8,11)
mplt.hist(pdist_vars_T, 100, density=True, label="Poisson")
mplt.title("Poisson Distribution")

## Laplacian Density Distribution
ldist_vars_T = np.random.laplace(theta, Tmode, i)
mplt.subplot(2,8,12)
mplt.hist(ldist_vars_T, 100, density=True, label="Laplacian")
mplt.title("Laplacian Distribution")

## Plot Rayleigh Distribution
rdist_vars_T = np.random.rayleigh(Tmode, i)
mplt.subplot(2,8,13)
mplt.hist(rdist_vars_T, 100, density=True, label="Rayleigh")
mplt.title("Rayleigh Distribution")

## Exponential Density Distribution
edist_vars_T = np.random.exponential(theta, len(theta))
mplt.subplot(2,8,14)
mplt.hist(edist_vars_T, 100, density=True, label="Exponential")
mplt.title("Exponential Distribution")

## Uniform distribution
udist_vars_T = np.random.uniform(0, theta[i-1], i)
mplt.subplot(2,8,15)
mplt.hist(udist_vars_T, 100, density=True, label="Uniform", color='red')
mplt.title("Uniform Distribution")

## Gaussian Density Distribution
gdist_vars_T = np.random.normal(mean, standardDeviation, i)
mplt.subplot(2,8,16)
mplt.hist(gdist_vars_T, 100, density=True, label="Gaussian (Normal)")
mplt.title("Gaussian Distribution")


mplt.show()

print(np.allclose(Z, rdist_vars_Z))