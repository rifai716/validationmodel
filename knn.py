import math

def knn(k, dtraining, dtest):
    obj = []
    for i in range(0,len(dtraining)):
        out = hitungJarak(dtraining[i],dtest)
        obj.append({
            'class' : dtraining[i],
            'jarak' : out
        })
    out = urutkan(obj,'jarak')
    return out[0:k]

def hitungJarak(a,b):
    total = 0
    for i in range(0, len(a)-1):
        total += math.pow(float(a[i])-float(b[i]),2)
    return math.sqrt(total)

def urutkan(arr,key):
    end = len(arr) - 1
    while end != 0:
        for i in range(end):
            if arr[i][key] > arr[i + 1][key]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        end = end - 1
    return arr