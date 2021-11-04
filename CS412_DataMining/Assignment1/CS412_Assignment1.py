import numpy as np
from numpy.core.numeric import Infinity
from scipy import stats
import scipy as sp
import statistics as s

#importing data from files
scores = np.genfromtxt(fname='CS_412_Fall21_Assignment1/data.online.scores.txt')
libraries = np.genfromtxt(fname='CS_412_Fall21_Assignment1/data.libraries.inventories.txt')

# problem 1
print('PROBLEM 1: \n')
mtmax = np.amax(scores, 0)[1]
print('a. Max Score on Midterms', mtmax)

mtmin = np.amin(scores, 0)[1]
print('b. Min Score on Midterms', mtmin)

mtquarts = np.quantile(scores, (0.25, 0.5, 0.75), 0)[:,1]
print('c. Q1 on Midterms', mtquarts[0])
print('   Median on Midterms', mtquarts[1])
print('   Q3 on Midterms', mtquarts[2])

mtmean = np.mean(scores, 0)[1]
print('d. Mean Score on Midterms', mtmean)

mtmode = s.multimode(scores[:,1])
print('e. Mode for Midterms', mtmode)

mtvar = np.var(scores, 0)[1]
print('f. Variance of Midterm Scores', mtvar)

# problem 3
print('\n\nPROBLEM 3: \n')
zscores = stats.zscore(scores)
mtzvar = np.var(zscores, 0)[1]
print('a. Variance of Midterm Scores', mtvar)
print('   Variance of Midterm Scores with zscoring', mtzvar)

z90 = (90-mtmean)/(np.sqrt(mtvar))
print('b. Score of 90 on a midterm with z-normalization:', z90)

corrcoef = np.corrcoef([scores[:,1], scores[:,2]])
print('c. Midterm to Finals Correlation Coefficient:\n', corrcoef)

zcorrcoef = np.corrcoef([zscores[:,1], scores[:,2]])
print('d. Z-scored Midterm to Finals Correlation Coefficient:\n', zcorrcoef)

# covariance = np.cov([scores[:,1], scores[:,2]])
# print('e. Covariance between Midterms and Finals', covariance)


# independent check of correlation coefficient and covariance equations
finalmean = np.mean(scores, 0)[2]
midtermstd = np.sqrt(mtvar)
finalstd = np.sqrt(np.var(scores, 0)[2])

bigsum = 0
for i in scores:
  bigsum+=(i[1]-mtmean)*(i[2]-finalmean)

rab = bigsum/(1000*finalstd*midtermstd)
covab = bigsum/1000

print(' double checking d', rab)
print('e. Covariance of midterm and final:', covab)

# Problem 4
minkh1 = sp.spatial.distance.minkowski(libraries[1][1:101], libraries[2][1:101], p=1)
minkh2 = sp.spatial.distance.minkowski(libraries[1][1:101], libraries[2][1:101], p=2)
minkhinf = sp.spatial.distance.minkowski(libraries[1][1:101], libraries[2][1:101], p=Infinity)

print('a. Minkoski distances')
print('    i. h=1: ', minkh1)
print('    i. h=2: ', minkh2)
print('    i. h=inf: ', minkhinf)

cossim = 1 - sp.spatial.distance.cosine(libraries[1][1:101], libraries[2][1:101])
print('b. Cosine similarity between CML and CBL', cossim)

def kl_divergence(p, q):
  return np.sum(np.where(p != 0, p * np.log(p / q), 0))


pCML = libraries[1][1:101]/np.sum(libraries[1][1:101])
pCBL = libraries[2][1:101]/np.sum(libraries[2][1:101])

KLdivweb = kl_divergence(pCML, pCBL)
KLdivRE = sp.special.rel_entr(pCML, pCBL)
KLdivKL = sp.special.kl_div(pCML, pCBL)

print('c. Kiebler Elves divergence using rel_entr    ', np.sum(KLdivRE))
print('c. Kiebler Elves divergence using kl_div      ', np.sum(KLdivKL))
print('c. Kiebler Elves divergence using web function', KLdivweb)

nKLdivweb = kl_divergence(pCBL, pCML)
nKLdivRE = sp.special.rel_entr(pCBL, pCML)
nKLdivKL = sp.special.kl_div(pCBL, pCML)

print('check ----------')
print('c. Kiebler Elves divergence using rel_entr    ', np.sum(nKLdivRE))
print('c. Kiebler Elves divergence using kl_div      ', np.sum(nKLdivKL))
print('c. Kiebler Elves divergence using web function', nKLdivweb)