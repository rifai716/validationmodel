import knn

def error(k,data):
    error = 0
    outKnn = []
    for i in range(0, len(data)):
        # +1 digunakan untuk menambahkan data hasil knn untuk menghindari data test sebagai data training
        # yang hasil jarak = 0.0 maka tidak dihitung tetapi pembandingnya sebanyak k inisiasi
        outKnn = a(k+1,data,data[i]) 
        print(outKnn)
        print("-- ERROR : %f"%(hError(k,data[i],outKnn))) 
        error += hError(k,data[i],outKnn) # untuk perhitungan error menggunakan k inisiasi
    print("--------------------------------------")
    return (1/len(data))*error

def a(k,dtraining,dtes):
    return knn.knn(k,dtraining,dtes)

def hError(k,test,knn):
    error = 0
    arr = []
    for i in range(0, len(knn)):
        arr.append(knn[i]['class'][len(knn[i]['class'])-1])
    uniqueList = set(arr)
    # print(uniqueList)
    count = 0
    if len(uniqueList) == 1 :
        error = 0
    elif len(uniqueList) > 1 :
        for i in range(0, len(knn)):
            # print("%s -- %s"%(knn[i]['class'][len(knn[i]['class'])-1],test[len(test)-1]))
            if (knn[i]['class'][len(knn[i]['class'])-1] is test[len(test)-1]):
                count += 1

    error = (1/k)*count
    return error
    