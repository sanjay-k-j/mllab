import pandas as pd

data = pd.read_csv("/content/sample_data/EconomyCar.csv", header=None)


number_of_attributes=len(data.columns)-1

S=[list('0'*number_of_attributes)]
G=[list('?'*number_of_attributes)]

print(S)
print(G)

def consistancy_of_G(instance,hypothesisSet):
  newG=[]
  print("instance:",instance)
  for h in hypothesisSet:
    print("h consistancy:",h)
    consistant=True
    for ind in range(len(h)):
      if h[ind]=='?':
        continue
      if h[ind]!=instance[ind]:
        consistant=False
        #print(h[ind],":",instance[ind])
        break
    if consistant==True:
      newG.append(h)
      print("neWG consistancy:", newG)
  
  return newG


def consistancy_of_S(instance,hypothesisSet):
  newS=[]
  for h in hypothesisSet:
    consistant=False
    for ind in range(len(h)):
      if h[ind]=='0':
        continue
      if h[ind]!=instance[ind]:
        consistant=True
        break
    if consistant==True:
      newS.append(h)
  return newS

for index, row in data.iterrows():
  
  if row[len(row)-1] == 'Yes':
    G=consistancy_of_G(row, G)
    print("afterconsistency",G)
    for ind in range(len(S[0])):
      if S[0][ind]=='0':
        S[0][ind]=row[ind]
      elif S[0][ind] != row[ind]:
        S[0][ind]='?'
      else:
        pass
  else:
    S=consistancy_of_S(row,S)
    newG=list()
    more_General=list()
    for ind in range(number_of_attributes):
      for h in G:
       newh=list(h)
       print("h:",h,len(G))
       if h[ind]=='?':
         if row[ind]!=S[0][ind]:
           newh[ind]=S[0][ind]
           newG.append(newh)
           more_General.append(h) 
           
      
      #print("addnew",newG)
    generalHypothesisRemovalList=list()
#    for generalhypothesis in more_General:
#      for nextSpecializationHypothesis in newG:
#        if generalhypothesis==nextSpecializationHypothesis:
#          print("same list")
#          generalHypothesisRemovalList.append(nextSpecializationHypothesis)
    print("moreGeneralList:",more_General)
    print("newList:",newG)
#    print("generalHypothesisRemovalList:",generalHypothesisRemovalList)
    for generalhypothesis in more_General:
      if generalhypothesis in newG:
        print("present")
        newG.remove(generalhypothesis)

    G=newG
  print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^VERSION SPACE^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
  print(row)
  print(S)
  print(G)
  print("--------------------------------------------------------------------------------------------")