import numpy as np
from scipy import stats

scores = np.genfromtxt(fname='data.online.scores.txt')

mtmax = np.amax(scores, 0)[1]
print('Max Score on Midterms', mtmax)

mtmin = np.amin(scores, 0)[1]
print('Min Score on Midterms', mtmin)

mtquarts = np.quantile(scores, (0.25, 0.5, 0.75), 0)[:,1]
print('Q1 on Midterms', mtquarts[0])
print('Median on Midterms', mtquarts[1])
print('Q3 on Midterms', mtquarts[2])

mtmean = np.mean(scores, 0)[1]
print('Mean Score on Midterms', mtmean)

mtmode = stats.mode(scores[:,1], 0)[0][0]
print('Mode for Midterms', mtmode)

mtvar = np.var(scores, 0)[1]
print('Variance of Midterm Scores', mtvar)