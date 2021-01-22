import pandas as pd
from NeuroNetworkBa import NeuroNetwork

trainData = pd.read_csv("../Data/2015_2020.csv", sep=',')
testData = pd.read_csv("../Data/2020_2021.csv", sep=',')


n = NeuroNetwork(trainData,testData)
n.manipulateData()
#n.createModel()
