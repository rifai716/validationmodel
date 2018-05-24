import knn
import LooCrossValidation

# Attribut Data
#    1. sepal length in cm
#    2. sepal width in cm
#    3. petal length in cm
#    4. petal width in cm
#    5. class: 
#       -- Iris Setosa
#       -- Iris Versicolour
#       -- Iris Virginica

k = 5
dataTraining    = []

data = open('iris.data.txt','r')

for d in data :
    # print(d.split('\n')[0].split(','))
    # m = l[0].split(',') #this one of another way
    dataTraining.append(d.split('\n')[0].split(',')) #own , join some another step

# coba = ['5.9', '3.0', '5.1', '1.8']
# print(knn.knn(5,dataTraining,coba))

print("ERROR TOTAL : %f %%"%(LooCrossValidation.error(k,dataTraining)*100))
print("--------------------------------------")
