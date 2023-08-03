import pandas as pd
from pgmpy.models import BayesianModel
from pgmpy.estimators import MaximumLikelihoodEstimator,BayesianEstimator
from pgmpy.estimators import PC

data = pd.read_csv("/content/sample_data/heart.csv",sep=',')
data.head(6)

c = PC(data)
structure = c.estimate()
print(structure.edges())

model = BayesianModel(structure.edges())

model.fit(data,estimator=MaximumLikelihoodEstimator)

from pgmpy.inference import VariableElimination
infer = VariableElimination(model)
q = infer.query(variables=['cp','target'],evidence={'sex':0,'exang':1})
print(q)

