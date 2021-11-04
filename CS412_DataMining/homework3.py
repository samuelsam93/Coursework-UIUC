from collections import defaultdict
from itertools import combinations

def get_sequences(seq_db, min_sup):
  
  with open(seq_db) as f:
    db = f.readlines()

  # process lines from file into list of strings
  for i in range(len(db)):
    db[i] = db[i][db[i].find('<')+1:db[i].find('>')]

  freq_dict = apriori(seq_db, min_sup)

  # # create dict of 1-itemsets
  # one_item_sets = {}
  # for i in range(len(db)):
  #   for j in range(len(db[i])):
  #     if (db[i][j] not in one_item_sets):
  #       one_item_sets[db[i][j]] = 1
  #     else:
  #       one_item_sets[db[i][j]] += 1

  # # initialize dict Fk with frequent 1-itemsets 
  # Fk = {}
  # for key in one_item_sets:
  #   if one_item_sets[key] >= min_sup:
  #     Fk[key] = one_item_sets[key]

  # # While loop to search for frequent patterns
  # while (len(Fk) > 0):

  #   for i in range(len(db)):
  #     for j in range(len(db[i])):
  #       if (db[i][j] not in one_item_sets):
  #         one_item_sets[db[i][j]] = 1
  #       else:
  #         one_item_sets[db[i][j]] += 1

  # print(Fk)
  # freq_dict = 1
  
  return freq_dict

def getItemSetFromList(itemSetList):
  tempItemSet = set()
  for itemSet in itemSetList:
    for item in itemSet:
      tempItemSet.add(frozenset(item))

  return tempItemSet

def getItemsWithMinSup(itemSet, itemSetList, minSup, globalItemSetWithSup):
  freqItemSet = set()
  localItemSetWithSup = defaultdict(int)
  
  for item in itemSet:
    for itemSet in itemSetList:
      if item.issubset(itemSet):
        globalItemSetWithSup[item] += 1
        localItemSetWithSup[item] += 1

  for item, supCount in localItemSetWithSup.items():
    if supCount >= minSup:
      freqItemSet.add(item)

  return freqItemSet

def getUnion(itemSet, length):
  return set([i.union(j) for i in itemSet for j in itemSet if len(i.union(j)) == length])

def prune(candidateSet, prevFreqSet, length):
  tempCandySet = candidateSet.copy()
  for item in candidateSet:
    subsets = combinations(item, length)
    for subset in subsets:
      if (frozenset(subset) not in prevFreqSet):
        tempCandySet.remove(item)
        break

  return tempCandySet

def apriori(seq_db, min_sup):
  C1ItemSet = getItemSetFromList(seq_db)

  globalFreqItemSet = dict()

  globalItemSetWithSup = defaultdict(int)

  L1ItemSet = getItemsWithMinSup(C1ItemSet, seq_db, min_sup, globalItemSetWithSup)

  currentLSet = L1ItemSet
  k = 2

  while(currentLSet):
    globalFreqItemSet[k-1] = currentLSet
    candidateSet = getUnion(currentLSet, k)
    candidateSet = prune(candidateSet, currentLSet, k-1)
    currentLSet = getItemsWithMinSup(candidateSet, seq_db, min_sup, globalItemSetWithSup)
    k += 1

  print(globalFreqItemSet)

  return globalFreqItemSet

get_sequences('/home/sam/SAM/School/Coursework-UIUC/CS412_DataMining/example_input.txt', 2)