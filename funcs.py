def minMasse(objList, maxMasse):
    objList = sorted(objList, key = lambda obj: obj["masse"])
    masseRest = maxMasse
    res = []
    value = 0
    for obj in objList:
        if obj["masse"] <= masseRest:
            res.append(obj)
            value += obj["valeur"]
        else:
            break
    return res, value

def maxVal(objList, maxMasse):
    objList = sorted(objList, key = lambda obj: obj["valeur"], reverse=True)
    masseRest = maxMasse
    res = []
    value = 0
    for obj in objList:
        if obj["masse"] <= masseRest:
            res.append(obj)
            value += obj["valeur"]
    return res, value

def ratio(objList, maxMasse):
    res = []
    value = 0
    masseRest = maxMasse
    for obj in objList:
        obj["ratio"] = obj["valeur"] / obj["masse"]
    objList = sorted(objList, key = lambda obj: obj["ratio"], reverse=True)
    for obj in objList:
        if obj["masse"] <= masseRest:
            res.append(obj)
            value += obj["valeur"]
    return res, value

def glouton(objList, maxMasse):
    minMasseres = minMasse(objList, maxMasse)[1]
    maxValres = maxVal(objList, maxMasse)[1]
    ratiores = ratio(objList, maxMasse)[1]

    return max(minMasseres, maxValres, ratiores)