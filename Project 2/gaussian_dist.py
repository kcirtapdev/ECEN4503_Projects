# Random Signals
# Project 2
# Patrick Laverty

import matplotlib.pyplot as mplt
import numpy as np
import random as rd
import scipy.stats as st

i = 10000 # amt of random variables

#xpoints = np.random.normal(0, 1, i)
#ypoints = np.random.normal(0, 1, i)

xpoints = []
ypoints = []
for j in range(0,i):
    xpoints.append(rd.randint(1,i))
    ypoints.append(rd.randint(1,i))

## creating Z and theta
Z = []
for j in range(0,i):
    Z.append(np.sqrt(xpoints[j] ** 2 + ypoints[j] ** 2) + np.pi)

theta = []
for j in range(0,i):
    theta.append(abs(1 / np.tan(ypoints[j]/xpoints[j])))


# Now that we have Z and Theta values
## We can continue with plotting each distribution
##############
# Plotting Z #
##############
mu_Z = np.mean(Z) # mean
mode_Z = np.sqrt(2 / np.pi) * mu_Z # mode
sigma_Z = np.std(Z) # standard deviation of Z
####

mplt.subplot(2,4,2)
## Gausian Density Distribution
# This part was not coded by but rather was found online,
# because it makes a great histogram I decided to use this for the first part to create a histogram.
# Credits: https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html
gdist_vars_Z = np.random.normal(mu_Z, sigma_Z, i) # Create i values of guassian distributed random variables
count_Z, bins_Z, ignored_Z = mplt.hist(gdist_vars_Z, 50, density=True, label="Gaussian")
dist_Z = 1 / (sigma_Z * np.sqrt(2 * np.pi)) * np.exp( -(bins_Z - mu_Z) ** 2 / (2 * sigma_Z ** 2))
mplt.plot(bins_Z, dist_Z, linewidth=2, color='r') # Plot Z Probability Density Function Curve
mplt.title("Gaussian Distribution")

## Plot Z Value Distribution
mplt.subplot(2,4,1)
mplt.hist(Z, 50, density=True, label="Z Values")
mplt.title("Z Value Distribution (No Function)")
mplt.plot(bins_Z, dist_Z, linewidth=2, color='r') # Plot Z Probability Density Function Curve

## Binomial Density Distributon
bdist_vars_Z = np.random.binomial(Z, 1, i)
mplt.subplot(2,4,3)
mplt.hist(bdist_vars_Z, 50, density=True, label="Binomial")
mplt.plot(bins_Z, dist_Z, linewidth=2, color='r') # Plot Z Probability Density Function Curve
mplt.title("Binomial Distribution")

## Rayleigh Density Distribution
rdist_vars_Z = np.random.rayleigh(mode_Z, i)
mplt.subplot(2,4,4)
mplt.hist(rdist_vars_Z, 50, density=True, label="Rayleigh")
mplt.plot(bins_Z, dist_Z, linewidth=2, color='r') # Plot Z Probability Density Function Curve
mplt.title("Rayleigh Distribution")

## Poisson Density Distribution
pdist_vars_Z = np.random.poisson(Z, len(Z))
mplt.subplot(2,4,5)
mplt.hist(pdist_vars_Z, 50, density=True, label="Poisson")
mplt.plot(bins_Z, dist_Z, linewidth=2, color='r') # Plot Z Probability Density Function Curve
mplt.title("Poisson Distribution")

## Laplacian Density Distribution
ldist_vars_Z = np.random.laplace(Z, mode_Z, i)
mplt.subplot(2,4,6)
mplt.hist(ldist_vars_Z, 50, density=True, label="Laplacian")
mplt.plot(bins_Z, dist_Z, linewidth=2, color='r') # Plot Z Probability Density Function Curve
mplt.title("Laplacian Distribution")

## Exponential Density Distribution
edist_vars_Z = np.random.exponential(Z, len(Z))
mplt.subplot(2,4,7)
mplt.hist(edist_vars_Z, 50, density=True, label="Exponential")
mplt.plot(bins_Z, dist_Z, linewidth=2, color='r') # Plot Z Probability Density Function Curve
mplt.title("Exponential Distribution")

## Uniform Density Distribution
udist_vars_Z = np.random.uniform(0, Z[i-1], i)
mplt.subplot(2,4,8)
mplt.hist(udist_vars_Z, 50, density=True, label="Uniform")
mplt.plot(bins_Z, dist_Z, linewidth=2, color='r') # Plot Z Probability Density Function Curve
mplt.title("Uniform Distribution")


mplt.suptitle("Z Values in each distribution function compared to Gaussian distribution (Red Line)")
mplt.show()

##################
# Plotting Theta #
##################
mu_T = np.mean(theta) # mean
mode_T = np.sqrt(2 / np.pi) * mu_T # mode
sigma_T = np.std(theta)
####

mplt.subplot(2,4,2)
## Gausian Density Distribution
# This part was not coded by but rather was found online,
# because it makes a great histogram I decided to use this for the first part to create a histogram.
# Credits: https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html
gdist_vars_T = np.random.normal(mu_T, sigma_T, i) # Create i values of guassian distributed random variables
count_T, bins_T, ignored_T = mplt.hist(gdist_vars_T, 50, density=True, label="Gaussian")
dist_T = 1 / (sigma_T * np.sqrt(2 * np.pi)) * np.exp( -(bins_T - mu_T) ** 2 / (2 * sigma_T ** 2))
mplt.plot(bins_T, dist_T, linewidth=2, color='r') # Plot T Probability Density Function Curve
mplt.title("Gaussian Distribution")

## Plot T Value Distribution
mplt.subplot(2,4,1)
mplt.hist(theta, 50, density=True, label="T Values")
mplt.title("Theta Value Distribution (No Function)")
mplt.plot(bins_T, dist_T, linewidth=2, color='r') # Plot T Probability Density Function Curve

## Binomial Density Distributon
bdist_vars_T = np.random.binomial(theta, 1, i)
mplt.subplot(2,4,3)
mplt.hist(bdist_vars_T, 50, density=True, label="Binomial")
mplt.plot(bins_T, dist_T, linewidth=2, color='r') # Plot T Probability Density Function Curve
mplt.title("Binomial Distribution")

## Rayleigh Density Distribution
rdist_vars_T = np.random.rayleigh(mode_T, i)
mplt.subplot(2,4,4)
mplt.hist(rdist_vars_T, 50, density=True, label="Rayleigh")
mplt.plot(bins_T, dist_T, linewidth=2, color='r') # Plot T Probability Density Function Curve
mplt.title("Rayleigh Distribution")

## Poisson Density Distribution
pdist_vars_T = np.random.poisson(theta, len(theta))
mplt.subplot(2,4,5)
mplt.hist(pdist_vars_T, 50, density=True, label="Poisson")
mplt.plot(bins_T, dist_T, linewidth=2, color='r') # Plot T Probability Density Function Curve
mplt.title("Poisson Distribution")

## Laplacian Density Distribution
ldist_vars_T = np.random.laplace(theta, mode_T, i)
mplt.subplot(2,4,6)
mplt.hist(ldist_vars_T, 50, density=True, label="Laplacian")
mplt.plot(bins_T, dist_T, linewidth=2, color='r') # Plot T Probability Density Function Curve
mplt.title("Laplacian Distribution")

## Exponential Density Distribution
edist_vars_T = np.random.exponential(theta, len(theta))
mplt.subplot(2,4,7)
mplt.hist(edist_vars_T, 50, density=True, label="Exponential")
mplt.plot(bins_T, dist_T, linewidth=2, color='r') # Plot T Probability Density Function Curve
mplt.title("Exponential Distribution")

## Uniform Density Distribution
udist_vars_T = np.random.uniform(0, theta[i-1], i)
mplt.subplot(2,4,8)
mplt.hist(udist_vars_T, 50, density=True, label="Uniform")
mplt.plot(bins_T, dist_T, linewidth=2, color='r') # Plot T Probability Density Function Curve
mplt.title("Uniform Distribution")


mplt.suptitle("Theta Values in each distribution function compared to Gaussian distribution (Red Line)")
mplt.show()
