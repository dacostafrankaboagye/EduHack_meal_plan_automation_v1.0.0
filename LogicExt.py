

dataList = []
eachData = []



with open('formattedDB.txt', 'r') as fdb:
    tempList = fdb.readlines()
    print(tempList)
    for i in range(len(tempList)):
        if tempList[i] == "==\n":
           idx = i
           print(idx)
           for j in range(4):
               idx = idx + 1
               print(tempList[idx])
        #    for j in range(4):
        #        idx=idx +1
        #        eachData.append(tempList[idx])
        #    idx = 0
           

#print(dataList)