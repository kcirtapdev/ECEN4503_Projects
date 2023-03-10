# Random Signals
# Project 3
# Patrick Laverty

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

samples = 10000

# generate random x
x = np.random.uniform(-1,1,samples)
y = np.random.uniform(-1,1,samples)


### PART 1
# Joint PDF
joint_pdf = []
for i in range(0,samples):
    if x[i]**2+y[i]**2 < 1:
        joint_pdf.append(1/np.pi)
    else:
        joint_pdf.append(0)

plt.figure("Joint PDF")
plt.title("Joint PDF")
plt.hist2d(x, y, bins=(100, 100), weights=joint_pdf, cmap="Reds")
plt.colorbar()
plt.show()

### PART 2
# Analytical Maginal PDF of X:
marginal_x = []
for i in range(0,samples):
    marginal_x.append((2 * np.sqrt(1 - x[i] ** 2)) / np.pi)

plt.figure("Marginal PDF of X")
plt.title("Marginal PDF of X")
plt.hist(x, 100, weights=marginal_x)
plt.show()

## PART 3
# New random y bounded by -0.01 < y < 0.01
y_new = np.random.uniform(-0.01,0.01,samples)

# Generate new PDF
joint_pdf_new = []
for i in range(0,samples):
    if x[i]**2+y_new[i]**2 < 1:
        joint_pdf_new.append(1/np.pi)
    else:
        joint_pdf_new.append(0)

# Analytical Marginal PDF of y = 0
marginal_y = []
for i in range(0,samples):
    marginal_y.append((2 * np.sqrt(1)) / np.pi)

# Analytical Conditional PDF of x given y = 0
conditional_x = []
for i in range(0,samples):
    conditional_x.append(joint_pdf_new[i] / marginal_y[i])

plt.figure("Analytical Conditional PDF of X given Y = 0")
plt.title("Analytical Conditional PDF of X given Y = 0")
plt.hist(x, weights=conditional_x, bins=100)
plt.show()